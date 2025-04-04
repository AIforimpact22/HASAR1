import streamlit as st
import pandas as pd
from handle import run_query  # Updated import

def status_page():
    st.markdown("""
    <style>
        .status-header {
            color: #2c3e50;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
            padding-bottom: 1rem;
            border-bottom: 2px solid #f0f2f6;
        }
        .search-container {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .order-card {
            border: 1px solid #e6e9ed;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            background-color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }
        .order-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.12);
        }
        .order-title {
            color: #2c3e50;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .order-details {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }
        .detail-item {
            margin: 5px 0;
            font-size: 0.9rem;
        }
        .detail-label {
            font-weight: 600;
            color: #2d3436;
        }
        .detail-value {
            color: #576574;
        }
        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        .status-pending {
            background-color: #ffeaa7;
            color: #d35400;
        }
        .status-processing {
            background-color: #81ecec;
            color: #00a8ff;
        }
        .status-shipped {
            background-color: #55efc4;
            color: #00b894;
        }
        .status-delivered {
            background-color: #a3cb38;
            color: #fff;
        }
        .status-cancelled {
            background-color: #ff7675;
            color: #fff;
        }
        .view-button {
            background-color: #3498db;
            color: white;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s ease;
        }
        .view-button:hover {
            background-color: #2980b9;
        }
        .no-results {
            text-align: center;
            padding: 30px;
            background-color: #f8f9fa;
            border-radius: 10px;
            color: #7f8c8d;
        }
    </style>
    
    <h1 class='status-header' style='color: #2C536C;'>Order Status & History</h1>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='search-container'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #FFA500;'>Find Your Orders</h2>", unsafe_allow_html=True)

        # Force the logged-in user's email if available
        user_email = st.experimental_user.email if (st.experimental_user and st.experimental_user.is_logged_in) else ""

        # We keep the same identifier logic but prefill and disable the input
        identifier = st.text_input(
            "Email",
            placeholder="Enter your email address",
            value=user_email,
            disabled=True,  # user can't change it
            help="Your sign-in email is auto-filled"
        )

        view_clicked = st.button("View Orders", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if view_clicked:
        if identifier:
            with st.spinner("Fetching your orders..."):
                query = """
                SELECT tree_name, customer_full_name, quantity, amount, address, status, note
                FROM payments
                WHERE email = %s
                ORDER BY status;
                """
                results = run_query(query, (identifier,))

            if results:
                st.success(f"Found {len(results)} orders for {identifier}")

                for idx, order in enumerate(results):
                    status_class = "status-pending"  # Default
                    if order['status'].lower() == 'processing':
                        status_class = "status-processing"
                    elif order['status'].lower() == 'shipped':
                        status_class = "status-shipped"
                    elif order['status'].lower() == 'delivered':
                        status_class = "status-delivered"
                    elif order['status'].lower() == 'cancelled':
                        status_class = "status-cancelled"

                    st.markdown(f"""
                    <div class="order-card">
                        <div class="order-title">Order #{idx+1}: {order['tree_name']}</div>
                        <span class="status-badge {status_class}">{order['status']}</span>
                        <div class="order-details">
                            <p class="detail-item">
                                <span class="detail-label">Customer:</span>
                                <span class="detail-value">{order['customer_full_name']}</span>
                            </p>
                            <p class="detail-item">
                                <span class="detail-label">Quantity:</span>
                                <span class="detail-value">{order['quantity']}</span>
                            </p>
                            <p class="detail-item">
                                <span class="detail-label">Amount:</span>
                                <span class="detail-value">{order['amount']} IQD</span>
                            </p>
                            <p class="detail-item">
                                <span class="detail-label">Delivery Address:</span>
                                <span class="detail-value">{order['address']}</span>
                            </p>
                        </div>
                        <div style="margin-top: 15px;">
                            <p class="detail-item">
                                <span class="detail-label">Note:</span>
                                <span class="detail-value">{order['note'] if order['note'] else 'No additional notes'}</span>
                            </p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="no-results">
                    <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#7f8c8d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="8" y1="12" x2="16" y2="12"></line>
                    </svg>
                    <h3>No Orders Found</h3>
                    <p>We couldn't find any orders associated with this email.</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Please enter your email to view your orders.")

def main():
    st.set_page_config(
        page_title="Order Status",
        page_icon="🌳",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    status_page()

if __name__ == "__main__":
    main()
