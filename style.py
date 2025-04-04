# style.py 
import streamlit as st

def apply_global_styles():
    """
    Applies global styles to the Streamlit app, including headers, cards, and images.
    """
    st.markdown("""
    <style>
    /* Global header styling */
    .main-header {
        color: var(--text);
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f0f2f6;
    }

    /* Tree card styling */
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

    /* Tree image styling */
    .tree-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    /* Tree title styling */
    .tree-title {
        color: var(--text);
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
    }

    /* Additional details styling */
    .tree-details {
        color: #666;
        font-size: 0.95rem;
        text-align: center;
        margin: 5px 0;
    }

    /* Price and stock styling */
    .tree-price {
        color: var(--primary);
        font-weight: bold;
        font-size: 1.1rem;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
        .tree-card {
            padding: 15px;
        }
        .tree-image {
            width: 100px;
            height: 100px;
        }
        .tree-title {
            font-size: 1.1rem;
        }
        .tree-details {
            font-size: 0.9rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_tree_card(tree):
    """
    Renders a tree card with the given tree data.

    Args:
        tree (dict): A dictionary containing tree details (e.g., photo_url, common_name, price, etc.).
    """
    st.markdown(f"""
    <div class="tree-card" style="text-align:center;">
        <img src="{tree['photo_url']}" alt="{tree['common_name']}" class="tree-image">
        <div class="tree-title">{tree['common_name']}</div>
        <p class="tree-details tree-price">Price: {tree['price']} IQD | Stock: {tree['quantity_in_stock']}</p>
        <p class="tree-details">Height: {tree['min_height']} - {tree['max_height']} cm</p>
        <p class="tree-details">Shape: {tree['shape']} | Watering: {tree['watering_demand']}</p>
        <p class="tree-details">Origin: {tree['origin']}</p>
    </div>
    """, unsafe_allow_html=True)

def show_footer():
    """
    Displays a footer on every page with a link to the AI For Impact web app.
    """
    footer_html = """
    <div class="global-footer" style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: transparent; text-align: center; padding: 0.5rem; z-index: 100;">
        <a href="https://aiforimpact.net/" target="_blank" style="color: #2C536C; font-weight: bold; text-decoration: none;">
            Web App developed by 🤖 aiforimpact.net
        </a>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
