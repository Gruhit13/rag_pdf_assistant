import streamlit as st

pg = st.navigation([st.Page("main.py", title="PDF Assistant", default=True) , st.Page("./quiz_page.py", title="Quiz", default=False)])
pg.run()