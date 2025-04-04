import streamlit as st
import datetime
from handle import execute_query
import style

def purchase_page():
    style.apply_global_styles()
    
    st.markdown("<h1 class='page-title' style='color: #2C536C;'>🌳 Tree Purchase Form</h1>", unsafe_allow_html=True)
    
    if 'purchase_tree' not in st.session_state:
        st.error("⚠️ No tree selected for purchase.")
        return
    
    tree_name = st.session_state.purchase_tree
    available_quantity = st.session_state.available_quantity
    unit_price = st.session_state.unit_price
    
    st.markdown("<div class='section-header'>📝 Order Summary</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Selected Tree:** {tree_name}")
            st.markdown(f"**Available Quantity:** {available_quantity}")
        with col2:
            st.markdown("<span style='color: #000000; font-weight: bold;'>Quantity</span>", unsafe_allow_html=True)
            quantity = st.number_input(
                "Quantity",
                min_value=1,
                max_value=int(available_quantity),
                step=1,
                help="Select the quantity of trees you wish to purchase.",
                label_visibility="collapsed"
            )
            st.markdown(f"<span style='color: #000000; font-weight: bold;'>Total Price:</span> {quantity * float(unit_price):,.2f} IQD", unsafe_allow_html=True)
    
    st.markdown("<div class='section-header' style='color: #3498db; font-weight: bold;'>👤 Customer Information</div>", unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<span style='color: #000000; font-weight: bold;'>Full Name</span>", unsafe_allow_html=True)
            customer_full_name = st.text_input("Full Name", placeholder="Enter your full name", label_visibility="collapsed")
            st.markdown("<span style='color: #000000; font-weight: bold;'>Delivery Address</span>", unsafe_allow_html=True)
            address = st.text_area("Delivery Address", placeholder="Enter your delivery address", label_visibility="collapsed")
        with col2:
            st.markdown("<span style='color: #000000; font-weight: bold;'>WhatsApp Number</span>", unsafe_allow_html=True)
            whatsapp_number = st.text_input("WhatsApp Number", placeholder="Enter your WhatsApp number", label_visibility="collapsed")
            st.markdown("<span style='color: #000000; font-weight: bold;'>Email Address</span>", unsafe_allow_html=True)
            
            # ►►► Automatically fill user's email ◄◄◄
            user_email = st.experimental_user.email if st.experimental_user else ""
            email = st.text_input(
                "Email Address",
                placeholder="Enter your email address",
                label_visibility="collapsed",
                value=user_email
            )
            
            st.markdown("<span style='color: #000000; font-weight: bold;'>Payment Method</span>", unsafe_allow_html=True)
            payment_preference = st.selectbox("Payment Method", ["Cash on Arrival"], help="Select your preferred payment method.", label_visibility="collapsed", disabled=True)
    
    payment_date = datetime.date.today().isoformat()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        order_button = st.button("✅ Place Order", type="primary", use_container_width=True)
        back_button = st.button("🔙 Back to Home", use_container_width=True)
    
    if order_button:
        missing_fields = []
        if not customer_full_name:
            missing_fields.append("Full Name")
        if not address:
            missing_fields.append("Delivery Address")
        if not whatsapp_number:
            missing_fields.append("WhatsApp Number")
        if not email:
            missing_fields.append("Email Address")
        
        if missing_fields:
            st.error(f"⚠️ Please fill in the following field(s): {', '.join(missing_fields)}")
            return
        
        total_price = quantity * float(unit_price)
        
        query = """
        INSERT INTO payments (
            tree_name, customer_full_name, quantity, amount, address,
            whatsapp_number, email, payment_preference, payment_date, status, note
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        try:
            execute_query(query, (
                tree_name, customer_full_name, str(quantity),
                str(total_price), address, whatsapp_number, email,
                payment_preference, payment_date, "Pending", ""
            ))

            st.success("🎉 Order placed successfully!")
            st.balloons()

            st.session_state.purchase_mode = False
            if hasattr(st, "experimental_rerun"):
                st.experimental_rerun()

        except Exception as e:
            st.error(f"❌ Error placing order: {str(e)}")
    
    if back_button:
        st.session_state.purchase_mode = False
        if hasattr(st, "experimental_rerun"):
            st.experimental_rerun()

if __name__ == "__main__":
    purchase_page()
