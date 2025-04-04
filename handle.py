# handle.py
import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st

def get_connection():
    try:
        # Fetch the connection string from the Streamlit secrets file
        connection_string = st.secrets["postgres"]["connection_string"]
        conn = psycopg2.connect(connection_string, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        st.error("Error connecting to the database.")
        raise e

def run_query(query, params=None):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(query, params)
        try:
            results = cur.fetchall()
        except psycopg2.ProgrammingError:
            results = None
    conn.commit()
    conn.close()
    return results

def execute_query(query, params=None):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(query, params)
    conn.commit()
    conn.close()
