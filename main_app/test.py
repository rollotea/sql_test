import streamlit as st

# Initialize connection.
conn = st.connection('mysql', url="mysql://root:dxftk286@localhost:3306/pets")

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
