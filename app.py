import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="QuCreate Streamlit Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Interactive Loan Amortization Visualizer")
st.divider()

# Introduction Section
st.markdown("""
    ## Understanding Loan Amortization

    **Loan amortization** is the process of paying off a loan over time through regular payments. 
    Each payment is divided into two parts: **principal** and **interest**. 
    Initially, a larger portion of your payment goes towards interest, and as time goes on, more of it goes towards the principal. 
    This application helps you visualize this process.

    **Key Financial Concepts:**

    - **Principal:** The original loan amount.
    - **Interest:** The cost of borrowing money, expressed as an annual percentage rate (APR).
    - **Loan Term:** The duration over which the loan is repaid, typically in years.
    - **Fixed Payments:**  In most amortizing loans, payments are fixed, meaning you pay the same amount each period.

    **The Amortization Process:**

    This visualizer follows these steps to generate the amortization schedule:

    1.  **Calculate the Periodic Payment:**  Uses a standard formula to determine your fixed monthly payment.
    2.  **Determine Payment Components:** For each payment, calculate the interest portion based on the outstanding principal and the principal portion as the remainder of the payment.
    3.  **Update Loan Balance:**  Reduce the outstanding balance by the principal portion of the payment.
    4.  **Iterate Through the Loan Term:** Repeat steps 2 and 3 for each payment period until the loan is fully paid.

    Experiment with different loan parameters in the sidebar to see how they affect your amortization schedule!
    """)

st.sidebar.header("Loan Parameters")

principal = st.sidebar.number_input("Principal Amount", min_value=1000.0, value=100000.0, step=1000.0, format="%.2f")
annual_interest_rate = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
loan_term_years = st.sidebar.slider("Loan Term (Years)", min_value=1, max_value=30, value=30, step=1)

monthly_interest_rate = annual_interest_rate / 1200  # Annual rate to monthly rate (and percentage to decimal)
loan_term_months = loan_term_years * 12

# Monthly Payment Calculation
if monthly_interest_rate > 0:
    monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-loan_term_months)))
else:
    monthly_payment = principal / loan_term_months # In case of 0% interest

# Amortization Schedule Calculation
amortization_schedule = []
remaining_balance = principal
cumulative_principal = 0
cumulative_interest = 0

for month in range(1, loan_term_months + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment

    if principal_payment > remaining_balance: # To handle the last payment correctly
        principal_payment = remaining_balance
        monthly_payment = interest_payment + principal_payment # Recalculate monthly payment for the last month to avoid overpayment

    remaining_balance -= principal_payment
    cumulative_principal += principal_payment
    cumulative_interest += interest_payment

    amortization_schedule.append({
        "Month": month,
        "Monthly Payment": monthly_payment,
        "Principal Payment": principal_payment,
        "Interest Payment": interest_payment,
        "Remaining Balance": remaining_balance,
        "Cumulative Principal": cumulative_principal,
        "Cumulative Interest": cumulative_interest
    })

amortization_df = pd.DataFrame(amortization_schedule)

# --- Visualizations ---
st.subheader("Amortization Schedule")
st.dataframe(amortization_df, column_config={
   "Monthly Payment": st.column_config.NumberColumn(format="%.2f"),
   "Principal Payment": st.column_config.NumberColumn(format="%.2f"),
   "Interest Payment": st.column_config.NumberColumn(format="%.2f"),
   "Remaining Balance": st.column_config.NumberColumn(format="%.2f"),
   "Cumulative Principal": st.column_config.NumberColumn(format="%.2f"),
   "Cumulative Interest": st.column_config.NumberColumn(format="%.2f")
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Payment Breakdown Over Time")
    payment_breakdown_data = amortization_df[["Month", "Principal Payment", "Interest Payment"]].set_index("Month")
    st.line_chart(payment_breakdown_data, height=400, use_container_width=True)
    st.markdown("""
        **Line Chart Interpretation:**
        This chart visualizes how your monthly payment is divided between principal and interest over the life of the loan. 
        Notice how initially, interest payments are higher, but as you progress through the loan term, principal payments increase while interest payments decrease. 
        This is the core concept of loan amortization.
        """)

with col2:
    st.subheader("Cumulative Payments")
    cumulative_payment_data = amortization_df[["Month", "Cumulative Principal", "Cumulative Interest"]].set_index("Month")
    st.bar_chart(cumulative_payment_data, height=400, use_container_width=True)
    st.markdown("""
        **Bar Chart Interpretation:**
        This chart shows the cumulative principal and interest paid over time. 
        It highlights the total amount you've paid towards reducing the loan principal and the total interest paid to the lender up to any given month. 
        You can observe how the cumulative interest grows initially, then the growth rate slows down as more payments are made towards principal.
        """)

st.subheader("Key Loan Summary")
col3, col4, col5 = st.columns(3)
col3.metric("Monthly Payment", f"${monthly_payment:.2f}")
col4.metric("Total Principal Paid", f"${amortization_df['Cumulative Principal'].iloc[-1]:.2f}")
col5.metric("Total Interest Paid", f"${amortization_df['Cumulative Interest'].iloc[-1]:.2f}")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
