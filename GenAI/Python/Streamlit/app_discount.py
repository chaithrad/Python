import streamlit as st

st.title("Price Calculator")

price = st.number_input("Enter product price:", min_value=0.0)

discount = st.slider("Select discount percentage:", 0, 50, 0)

if st.button("Calculate"):
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    st.success(f"Final Price: ₹{final_price:.2f}")

    st.write("Original Price:", price)
    st.write("Discount:", f"{discount}%")

    table_data = [
        ["Before", "After"],
        [price, final_price]
    ]

    st.table(table_data)
    