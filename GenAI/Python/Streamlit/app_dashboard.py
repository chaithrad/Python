import streamlit as st

st.title("Simple Sales Dashboard")

st.write("View monthly sales data using the dashboard below.")

months = ["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November", "December"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000,
    "May": 1800,
    "June": 2200,
    "July": 2500,
    "August": 3000,
    "September": 2800,
    "October": 3200,
    "November": 3500,
    "December": 4000    
}

selected_month = st.selectbox("Select a month:", months)

selected_sales = sales[selected_month]

st.metric(
    label=f"Sales for {selected_month}",
    value=f"₹{selected_sales}"
)

st.subheader("Monthly Sales")

st.bar_chart(list(sales.values()))