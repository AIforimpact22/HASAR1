import streamlit as st
from handle import run_query
import style

def set_purchase_for_tree(tree_common_name):
    """
    Query to select the nursery with the highest stock for the given tree,
    then set purchase variables in session_state.
    """
    query = """
    SELECT nti.tree_common_name, nti.quantity_in_stock, nti.price
    FROM Nursery_Tree_Inventory AS nti
    WHERE nti.tree_common_name = %s
    ORDER BY nti.quantity_in_stock DESC
    LIMIT 1;
    """
    result = run_query(query, (tree_common_name,))
    if result:
        row = result[0]
        st.session_state.purchase_tree = row["tree_common_name"]
        st.session_state.available_quantity = row["quantity_in_stock"]
        st.session_state.unit_price = row["price"]
        st.session_state.purchase_mode = True
        if hasattr(st, "experimental_rerun"):
            st.experimental_rerun()

def render_tree_card_html(row):
    """
    Returns an HTML snippet for a tree card, including:
      - Photo, Growth Rate, Stock
      - Price, Height, Shape, Watering, Soil, Origin, Root, Leaf
      - Address
    """
    return f"""
    <div class="tree-card" style="margin:10px;padding:10px;border:1px solid #e6e9ed;border-radius:10px;background:#fff;box-shadow:0 4px 12px rgba(0,0,0,0.08);font-size:0.9rem;">
        <div style="text-align:center;margin-bottom:8px;position:relative;">
            <a href="{row['photo_url']}" target="_blank">
                <div style="width:100%;height:120px;overflow:hidden;border-radius:8px;display:flex;justify-content:center;align-items:center;">
                    <img src="{row['photo_url']}" alt="{row['common_name']}"
                         style="height:100%;width:auto;object-fit:cover;transition:transform 0.3s ease;">
                </div>
            </a>
        </div>
        <h3 style="margin:4px 0;text-align:center;color:#2C536C;">{row['common_name']}</h3>
        <div style="text-align:center;margin-bottom:8px;">
            <span style="color:#5DADE2;">Growth Rate: {row['growth_rate']} cm/yr</span> |
            <span style="color:#5DADE2;">Stock: {row['quantity_in_stock']}</span>
        </div>
        <hr style="margin:8px 0;border-color:#e6e9ed;">
        <div style="line-height:1.3;">
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Price:</strong> {row['price']} IQD
            </p>
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Height:</strong> {row['min_height']} - {row['max_height']} cm /
                <strong>Shape:</strong> {row['shape']}
            </p>
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Watering:</strong> {row['watering_demand']} /
                <strong>Soil:</strong> {row['soil_type']}
            </p>
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Origin:</strong> {row['origin']} /
                <strong>Root:</strong> {row['root_type']}
            </p>
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Leaf:</strong> {row['leafl_type']}
            </p>
            <p style="margin:2px 0;white-space:nowrap;">
                <strong>Available at:</strong> {row['address']}
            </p>
        </div>
    </div>
    """

def display_all_trees():
    # Apply global styles (from your style module)
    style.apply_global_styles()
    
    # Remove the forced green color in .stButton so it's consistent with others
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    :root {
        --background-light: #f7f9fc;
        --text-dark: #2c3e50;
        --text-muted: #6c757d;
        --primary-green: #2ecc71;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background-color: var(--background-light);
    }
    
    .tree-collection {
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08);
        padding: 30px;
        margin-top: 20px;
    }
    
    .tree-card {
        background-color: white;
        border-radius: 16px;
        border: 1px solid #e9ecef;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        margin-bottom: 24px;
    }
    
    .tree-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        border-color: var(--primary-green);
    }
    
    .tree-card:hover img {
        transform: scale(1.1);
    }
    
    .tree-details {
        padding: 20px;
        text-align: center;
    }
    
    .tree-details h4 {
        color: var(--text-dark);
        font-weight: 600;
        margin-bottom: 10px;
    }
    
    .empty-state {
        background-color: var(--background-light);
        border-radius: 16px;
        padding: 60px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header (unchanged)
    st.markdown(
        """
        <div style='border: 2px solid #007BFF; border-radius: 12px; padding: 20px; margin-bottom: 30px;'>
            <div class='text-center mb-5'>
                <h1 style='color: var(--text-dark); font-weight: 700; font-size: 2.5rem;'>
                    🌳 Tree Nursery Collection
                </h1>
                <p style='color: var(--text-muted); font-size: 1.1rem;'>
                    Sustainable Solutions for Environmental Restoration
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Query to fetch ALL tree records (including duplicates at different addresses)
    query = """
    SELECT
        nti.quantity_in_stock,
        nti.price,
        nti.min_height,
        nti.max_height,
        t.growth_rate,
        nti.tree_common_name AS common_name,
        t.shape,
        t.watering_demand,
        p.photo_url,
        t.origin,
        t.soil_type,
        t.root_type,
        t.leafl_type,
        n.address
    FROM Nursery_Tree_Inventory nti
    JOIN Trees t ON nti.tree_common_name = t.common_name
    JOIN photos p ON t.common_name = p.common_name
    JOIN Nurseries n ON nti.nursery_name = n.nursery_name
    ORDER BY nti.quantity_in_stock DESC;
    """
    results = run_query(query)
    
    if results:
        # Container for the tree collection
        st.markdown("<div class='tree-collection'>", unsafe_allow_html=True)
        
        # Display in rows of TWO columns
        for i in range(0, len(results), 2):
            cols = st.columns(2)
            for j in range(2):
                idx = i + j
                if idx < len(results):
                    tree = results[idx]
                    with cols[j]:
                        # Render the card as HTML
                        st.markdown(render_tree_card_html(tree), unsafe_allow_html=True)

                        # Purchase button: uses the default color
                        st.button(
                            f"Purchase {tree['common_name']}",
                            key=f"sr_purchase_{idx}",
                            on_click=set_purchase_for_tree,
                            args=(tree['common_name'],)
                        )
        
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div class='empty-state'>
                <h3 style='color: var(--text-dark); margin-bottom: 15px;'>
                    No Trees Available
                </h3>
                <p style='color: var(--text-muted);'>
                    Our nursery is momentarily restocking. 
                    Check back soon for our latest collection.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    display_all_trees()
