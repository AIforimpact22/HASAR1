import streamlit as st

def sidebar_menu():
    # Apply custom CSS for the sidebar
    st.markdown("""
    <style>
        /* Force the sidebar background to white */
        [data-testid="stSidebar"] {
            background-color: white;
        }
        .sidebar-header {
            color: #2c3e50;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 700;
            margin-bottom: 1.5rem;
            padding-bottom: 0.75rem;
            border-bottom: 2px solid #f0f2f6;
            text-align: center;
        }
        .sidebar-menu-item {
            background-color: white;
            color: #2c3e50;
            border: 1px solid #e6e9ed;
            border-radius: 8px;
            padding: 12px 15px;
            margin-bottom: 10px;
            text-align: left;
            font-weight: 500;
            transition: all 0.3s ease;
            width: 100%;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .sidebar-menu-item:hover {
            background-color: #f8f9fa;
            border-color: #cbd3da;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            transform: translateY(-2px);
        }
        .sidebar-menu-item-active {
            background-color: #3498db;
            color: white;
            border: 1px solid #2980b9;
        }
        .sidebar-menu-item-active:hover {
            background-color: #2980b9;
            color: white;
        }
        .sidebar-logo {
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-divider {
            margin: 20px 0;
            border: none;
            height: 1px;
            background-color: #e6e9ed;
        }
        .sidebar-bottom {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9rem;
            color: #666;
        }
        .sidebar-bottom a {
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
        }
        .sidebar-bottom a:hover {
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Display the HASAR logo
    st.sidebar.markdown("""
    <div class="sidebar-logo">
    """, unsafe_allow_html=True)
    st.sidebar.image("https://raw.githubusercontent.com/Hakari-Bibani/photo/refs/heads/main/logo/hasar.png", width=230)  # Adjust width as needed
    st.sidebar.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state if not exists
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Home"
    
    # Create sidebar menu buttons with active state styling
    def styled_button(label, key, active_page, icon):
        active = st.session_state.selected_page == active_page
        style = "sidebar-menu-item-active" if active else "sidebar-menu-item"
        if st.sidebar.button(f"{icon} {label}", key=key, use_container_width=True, help=f"Go to {label} page"):
            st.session_state.selected_page = active_page
            st.session_state.purchase_mode = False  # Reset purchase mode when changing page
        st.sidebar.markdown(f"<script>document.querySelectorAll('button')[document.querySelectorAll('button').length-1].className = '{style}';</script>", unsafe_allow_html=True)
    
    # Add icons to the buttons
    styled_button("Home", "home_button", "Home", "🏠")
    styled_button("Status", "status_button", "Status", "📊")
    styled_button("Contact", "contact_button", "Contact", "📞")
    styled_button("About", "about_button", "About", "ℹ️")
    
    return st.session_state.selected_page
    
if __name__ == "__main__":
    sidebar_menu()
