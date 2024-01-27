import streamlit as st
import pandas as pd
import sqlalchemy as sa

engine = sa.create_engine("mysql+pymysql://root:dxftk286@localhost:3306/pets")
df = pd.read_sql_query(sql="SELECT * FROM mytable", con=engine)
st.dataframe(df)