import streamlit as st
import sqlite3
import os
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'session_logs.db')

def get_logs():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()
    return df

def main():
    st.title("BLACKBOX VoiceWatch Dashboard")
    st.write("View logged voice transactions and detected glitches.")
    
    df = get_logs()
    if df.empty:
        st.write("No logs available.")
    else:
        st.dataframe(df)

if __name__ == "__main__":
    main()
