# inventory_helpers.py
from handle import run_query

def fetch_addresses():
    query = "SELECT DISTINCT address FROM Nurseries;"
    return [row["address"] for row in run_query(query) or []]

def fetch_packaging_types(selected_tree):
    if selected_tree != "All":
        query = "SELECT DISTINCT packaging_type FROM Nursery_Tree_Inventory WHERE tree_common_name = %s;"
        return [row["packaging_type"] for row in run_query(query, (selected_tree,)) or []]
    else:
        query = "SELECT DISTINCT packaging_type FROM Nursery_Tree_Inventory;"
        return [row["packaging_type"] for row in run_query(query) or []]

def fetch_height_range(selected_tree):
    if selected_tree != "All":
        height_range_query = (
            "SELECT MIN(min_height) as min_val, MAX(max_height) as max_val "
            "FROM Nursery_Tree_Inventory WHERE tree_common_name = %s;"
        )
        return run_query(height_range_query, (selected_tree,))
    else:
        height_range_query = (
            "SELECT MIN(min_height) as min_val, MAX(max_height) as max_val "
            "FROM Nursery_Tree_Inventory;"
        )
        return run_query(height_range_query)
