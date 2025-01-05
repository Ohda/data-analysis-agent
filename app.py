import os
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"

import streamlit as st

st.set_page_config(page_title="Data Visualisation", page_icon="📊", layout="wide")

data_visualisation_page = st.Page("./Pages/python_visualisation_agent.py",title="Data Visualisation", icon="📊")

pg = st.navigation(
    {
        "Visualisation Agent": [data_visualisation_page]
    }
)

pg.run()