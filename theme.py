import streamlit as st

def set_theme():
    """
    Sets the Streamlit theme with a minimalistic and neutral design.
    """
    st.markdown("""
    <style>
    /* Primary Color: Updated values remain */
    :root {
        --primary: #b0cde0;             /* Blue shade for buttons and highlights */
        --secondary: #34495e;           /* Dark blue-gray for text and secondary elements */
        --accent: #f8f9fa;              /* Light off-white for backgrounds */
        --background: #ffffff;          /* White background for main content */
        --text: #2c3e50;                /* Dark text for readability */
        --sidebar-bg: #ffffff;          /* White for sidebar background */
        --label: #3498db;               /* Blue for labels and inputs */
        --hover-glow: 0 0 8px grey;      /* Grey glow for hover effects (other elements) */
    }

    /* Apply custom font (Roboto as an example) */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Roboto', sans-serif !important;
    }

    /* Minimalistic and modern styling */
    .stApp {
        background-color: var(--background);
        color: var(--text);
    }

    /* Sidebar background and styling */
    .css-1d391kg, .css-1d391kg > div {
        background-color: var(--sidebar-bg) !important;
    }

    /* Blue font for labels */
    label {
        color: var(--label) !important;
        font-weight: bold !important;
    }

    /* Better-looking input boxes with rounded corners and soft green glow on hover/focus */
    input, textarea, select {
        border-radius: 12px !important;
        border: 1px solid #e6e9ed !important;
        padding: 8px 12px !important;
        transition: box-shadow 0.3s ease, border-color 0.3s ease !important;
        color: var(--label) !important;
    }
    input:hover, textarea:hover, select:hover {
        border-color: #27ae60 !important;
        box-shadow: 0 0 8px rgba(39, 174, 96, 0.5) !important;
    }
    input:focus, textarea:focus, select:focus {
        border-color: #27ae60 !important;
        box-shadow: 0 0 8px rgba(39, 174, 96, 0.5) !important;
    }

    /* Improved button UX: color change on hover with a green border */
    .stButton button {
        background-color: var(--primary) !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        font-weight: bold !important;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease !important;
        border: none !important;
    }
    .stButton button:hover {
        background-color: #a0bcd8 !important;  /* Slightly darker shade on hover */
        transform: scale(1.05) !important;
        box-shadow: var(--hover-glow) !important;
        border: 2px solid #27ae60 !important;  /* Green border on hover */
    }

    /* Tabs styling */
    .stTabs [role="tab"] {
        border-radius: 50px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        color: var(--secondary) !important;
        background-color: var(--background) !important;
        border: 1px solid #808080 !important;
        transition: color 0.3s ease, box-shadow 0.3s ease !important;
    }
    .stTabs [role="tab"]:hover {
        color: var(--primary) !important;
        box-shadow: var(--hover-glow) !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #d3d3d3 !important;
        color: black !important;
        border-bottom: 2px solid #27ae60 !important;  /* Green border when selected */
    }

    /* Cards */
    .tree-card {
        border: 1px solid #e6e9ed;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .tree-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.12);
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .tree-card {
            padding: 15px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
