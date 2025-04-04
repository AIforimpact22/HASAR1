import streamlit as st
from handle import run_query
from inventory_helpers import fetch_addresses, fetch_packaging_types, fetch_height_range
import style

def set_purchase(row):
    st.session_state.purchase_tree = row["common_name"]
    st.session_state.available_quantity = row["quantity_in_stock"]
    st.session_state.unit_price = row["price"]
    st.session_state.purchase_mode = True
    if hasattr(st, "experimental_rerun"):
        st.experimental_rerun()

def home_page():
    if st.session_state.get("purchase_mode", False):
        return

    style.apply_global_styles()
    st.markdown("<h1 class='main-header' style='color: #2C536C;'>🌳 Tree Nursery Inventory</h1>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='filters-container'>", unsafe_allow_html=True)
        st.markdown("<h2 class='filter-header'>🔍 Search Filters</h2>", unsafe_allow_html=True)

        query_tree_names = "SELECT DISTINCT tree_common_name FROM Nursery_Tree_Inventory;"
        tree_names = [row["tree_common_name"] for row in run_query(query_tree_names) or []]

        col1, col2, col3 = st.columns(3)
        with col1:
            selected_tree = st.selectbox("🌿 Tree Species", ["All"] + tree_names)
        with col2:
            selected_packaging = st.selectbox("📦 Packaging Type", ["All"] + fetch_packaging_types(selected_tree))
        with col3:
            selected_address = st.selectbox("🏡 Address", ["All"] + fetch_addresses())

        height_range = fetch_height_range(selected_tree)
        selected_height_range = None
        if height_range and height_range[0]["min_val"] is not None:
            mn, mx = float(height_range[0]["min_val"]), float(height_range[0]["max_val"])
            st.markdown("<h4 class='slider-header'>📏 Height Range (cm)</h4>", unsafe_allow_html=True)
            selected_height_range = st.slider("", mn, mx, (mn, mx), label_visibility="collapsed")

        search_clicked = st.button("🔍 Search Inventory", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if search_clicked:
        conditions, params = [], []
        if selected_tree != "All":
            conditions.append("nti.tree_common_name = %s"); params.append(selected_tree)
        if selected_packaging != "All":
            conditions.append("nti.packaging_type = %s"); params.append(selected_packaging)
        if selected_address != "All":
            conditions.append("n.address = %s"); params.append(selected_address)
        if selected_height_range:
            conditions.append("nti.max_height >= %s AND nti.min_height <= %s")
            params.extend(selected_height_range)

        where_clause = " AND ".join(conditions) if conditions else "1=1"
        query = f"""
            SELECT nti.quantity_in_stock, nti.price, nti.min_height, nti.max_height,
                   t.growth_rate, nti.tree_common_name as common_name, t.shape, t.watering_demand,
                   p.photo_url, t.origin, t.soil_type, t.root_type, t.leafl_type,
                   n.address
            FROM Nursery_Tree_Inventory nti
            JOIN Trees t ON nti.tree_common_name = t.common_name
            JOIN photos p ON t.common_name = p.common_name
            JOIN Nurseries n ON nti.nursery_name = n.nursery_name
            WHERE {where_clause}
            ORDER BY nti.quantity_in_stock DESC;
        """

        # FIX: Only pass params if there are any placeholders
        if params:
            results = run_query(query, tuple(params))
        else:
            results = run_query(query)

        if results:
            st.success(f"✅ Found {len(results)} trees matching your criteria")
            for i in range(0, len(results), 2):
                cols = st.columns(2)
                for idx in range(2):
                    if i + idx < len(results):
                        row = results[i + idx]
                        with cols[idx]:
                            st.markdown(render_tree_card_html(row), unsafe_allow_html=True)
                            st.button(f"🛒 Purchase {row['common_name']}", key=f"purchase_{i+idx}", on_click=set_purchase, args=(row,), use_container_width=True)
        else:
            st.warning("⚠️ No trees found matching your criteria. Adjust your filters.")

def render_tree_card_html(row):
    return f"""
    <div class="tree-card" style="margin:10px;padding:10px;border:1px solid #e6e9ed;border-radius:10px;background:#fff;box-shadow:0 4px 12px rgba(0,0,0,0.08);font-size:0.9rem;">
        <div style="text-align:center;margin-bottom:8px;">
            <a href="{row['photo_url']}" target="_blank"><img src="{row['photo_url']}" alt="{row['common_name']}" style="width:100%;max-width:120px;border-radius:50%;object-fit:cover;cursor:pointer;"></a>
        </div>
        <h3 style="margin:4px 0;text-align:center;color:#2C536C;">{row['common_name']}</h3>
        <div style="text-align:center;margin-bottom:8px;">
            <span style="color:#5DADE2;">Growth Rate: {row['growth_rate']} cm/yr</span> |
            <span style="color:#5DADE2;">Stock: {row['quantity_in_stock']}</span>
        </div>
        <hr style="margin:8px 0;border-color:#e6e9ed;">
        <div style="line-height:1.3;">
            <p style="margin:2px 0;white-space:nowrap;"><strong>Price:</strong> {row['price']} IQD</p>
            <p style="margin:2px 0;white-space:nowrap;"><strong>Height:</strong> {row['min_height']} - {row['max_height']} cm / <strong>Shape:</strong> {row['shape']}</p>
            <p style="margin:2px 0;white-space:nowrap;"><strong>Watering:</strong> {row['watering_demand']} / <strong>Soil:</strong> {row['soil_type']}</p>
            <p style="margin:2px 0;white-space:nowrap;"><strong>Origin:</strong> {row['origin']} / <strong>Root:</strong> {row['root_type']}</p>
            <p style="margin:2px 0;white-space:nowrap;"><strong>Leaf:</strong> {row['leafl_type']}</p>
            <p style="margin:2px 0;white-space:nowrap;"><strong>Available at:</strong> {row['address']}</p>
        </div>
    </div>
    """

if __name__ == "__main__":
    home_page()
