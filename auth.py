# auth.py
import streamlit as st

def handle_authentication():
    """Displays a custom login screen and triggers Google OAuth if the user is not logged in."""
    if not st.experimental_user.is_logged_in:
        # Add custom CSS - adjust heights to prevent scrolling
        st.markdown(
            """
            <style>
                /* Hide Streamlit default elements to maximize space */
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                
                /* Adjust main container height and remove padding */
                .main .block-container {
                    padding-top: 0;
                    padding-bottom: 0;
                    max-width: 100%;
                }
                
                /* Login container with auto height */
                .login-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    height: auto;
                    text-align: center;
                    padding-top: 10vh; /* Reduced top padding */
                }
                
                .login-logo {
                    margin-bottom: 1.5rem;
                }
                
                .login-heading {
                    font-family: sans-serif;
                    font-weight: 600;
                    font-size: 1.5rem;
                    margin: 1rem 0;
                    color: #333;
                }
                
                .login-message {
                    color: #666;
                    margin-bottom: 1.5rem;
                }
                
                /* Streamlit button overrides */
                div.stButton > button:first-child {
                    background-color: white;
                    color: #444;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 0.5rem 1rem;
                    font-size: 16px;
                    font-weight: 500;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
                    transition: all 0.2s ease;
                }
                
                div.stButton > button:hover {
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    background-color: #fafafa;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        
        # Use a container for better spacing control
        with st.container():
            # Create login container with columns for centering
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                # Login container with built-in top padding
                st.markdown('<div class="login-container">', unsafe_allow_html=True)
                
                # Logo - fixed with the URL you provided
                st.markdown(
                    f'<div class="login-logo"><img src="https://raw.githubusercontent.com/Hakari-Bibani/photo/refs/heads/main/logo/hasar1.png"></div>',
                    unsafe_allow_html=True
                )
                
                # Heading
                st.markdown('<h2 class="login-heading">Sign in to your HASAR account</h2>', unsafe_allow_html=True)
                
                # Message - shortened
                st.markdown('<p class="login-message">Please sign in with your Google account</p>', unsafe_allow_html=True)
                
                # Close container
                st.markdown('</div>', unsafe_allow_html=True)
                
                # The clickable "Log in with Google" button
                st.button("Log in with Google", on_click=st.login, use_container_width=True)

        # Stop execution until user is logged in
        st.stop()

    # If logged in, we do NOT show the user's email or a welcome message
    # The logout button is placed at the bottom of the sidebar in app.py
