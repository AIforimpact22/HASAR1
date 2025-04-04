# app.py
import streamlit as st
import theme
import style
from auth import handle_authentication
from sidebar import sidebar_menu

st.set_page_config(
    page_title="Tree Nursery Collection",
    page_icon="🌳"
)

# Apply your global theme and styles
theme.set_theme()
style.apply_global_styles()

# CSS override for all buttons (including sidebar logout and purchase buttons)
st.markdown(
    """
    <style>
    /* Override button text to use normal case */
    div[data-testid="stSidebar"] .stButton button,
    .stButton > button {
        text-transform: none !important;
        letter-spacing: normal !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 1) Handle Google authentication
handle_authentication()

# 2) Render your sidebar menu (pages)
selected_page = sidebar_menu()

# 3) Place a large vertical spacer, then the Logout button at the bottom
st.sidebar.markdown("<div style='flex:1;'></div>", unsafe_allow_html=True) 
if st.sidebar.button("Logout", key="logout_bottom"):
    st.logout()

# 4) Page content logic:
if "purchase_mode" not in st.session_state:
    st.session_state.purchase_mode = False

if st.session_state.purchase_mode:
    import purchase
    purchase.purchase_page()
else:
    if selected_page == "Home":
        import search
        search.home_page()

        from search_results import display_all_trees
        st.divider()
        display_all_trees()

    elif selected_page == "Status":
        import status
        status.status_page()

    elif selected_page == "Contact":
        import contact_page
        contact_page.show_contact()

    elif selected_page == "About":
        import about_page
        about_page.show_about()

# 5) Footer on all pages
style.show_footer()
