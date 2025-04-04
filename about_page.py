# about_page.py
import streamlit as st
import style

def show_about():
    # Apply global styles
    style.apply_global_styles()

    # Page title with dark blue color
    st.markdown(
        "<h1 style='color: #00008B;'>🌳 About Hasar </h1>", 
        unsafe_allow_html=True
    )

    # About section
    st.markdown("""
    Hasar is a dedicated non-profit organization founded in 2019 to foster climate resilience in the Kurdistan Region. 
    Initiated by **Hawkar Ali Abdulhaq**, an Earth Science Engineer and activist, with the crucial support of **Naz Nawzad Bajgar** (Cihan Bank) and **Gashbin Idris Ali**, we aim to transform lives by strengthening community resilience against climate change.
    """)

    # Mission section with orange color
    st.markdown(
        "<h3 style='color: #FFA500;'>Our Mission</h3>", 
        unsafe_allow_html=True
    )
    st.markdown("""
    We intertwine the futures of communities and corporations through innovative **Climate Resilience Impact Credits**, fostering mutual prosperity and a sustainable future.
    """)

    # Vision section with orange color
    st.markdown(
        "<h3 style='color: #FFA500;'>Our Vision</h3>", 
        unsafe_allow_html=True
    )
    st.markdown("""
    To redefine resilience by empowering **20 million people** across vulnerable regions with sustainable solutions, including:
    - **Water management**
    - **Reforestation**
    - **Soil enhancement**
    - **Socio-economic sustainability**

    We strive to make resilience an integral part of every community, setting global precedents in sustainable living.
    """)

    # Impact section with orange color
    st.markdown(
        "<h3 style='color: #FFA500;'>Our Impact</h3>", 
        unsafe_allow_html=True
    )
    st.markdown("""
    Since our inception, we have:
    - Planted **over 310,000 trees**
    - Implemented innovative **wastewater recycling systems**
    - Created **meaningful employment opportunities**
    - Collaborated with influential organizations, including **UNICEF** and the **KRG government**
    """)

    # Call to action
    st.markdown("""
    We invite collaboration from **volunteers**, **corporations**, **NGOs**, and **authorities** who share our passion for a climate-resilient future.
    """)

    # Contact information
    st.markdown("📧 **Contact us:** [info@hasar.org](mailto:info@hasar.org)")
