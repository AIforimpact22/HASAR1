# contact_page.py
import streamlit as st
import style

def show_contact():
    """
    Displays the contact information for Hasar Partners.
    """
    # Apply global styles
    style.apply_global_styles()

    # Page title with dark blue color
    st.markdown(
        "<h1 style='color: #00008B;'>📞 Contact Hasar </h1>", 
        unsafe_allow_html=True
    )

    # Contact information
    contact_info = {
        "Website": "🌐 [https://hasar.org](https://hasar.org)",
        "Location": "📍 Erbil, Kurdistan Region of Iraq",
        "Email": "📧 [info@hasar.org](mailto:info@hasar.org)",
        "Phone": "📞 +964 750 843 8872"
    }

    # Display contact information
    for key, value in contact_info.items():
        st.markdown(f"**{key}:** {value}")

    # Additional information
    st.markdown("""
    For collaboration, partnerships, volunteering, or inquiries, feel free to contact us using the provided information. 
    We are always eager to connect with individuals and organizations dedicated to building climate resilience.
    """)

# Optional: Add a main block for standalone execution
if __name__ == "__main__":
    show_contact()
