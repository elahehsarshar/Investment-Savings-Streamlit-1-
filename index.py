import streamlit as st


# defining a function for calculating the number of apartments someone will have at a given age
def apt_numbers():
    # Inputs
    age_now = st.number_input("Enter your current age: ")
    age_retire = st.number_input("Enter your desired retirement age: ")
    years_savings = age_retire - age_now

    savings_per_month = st.number_input("Enter your monthly savings: ")
    apt_price = st.number_input("Enter the price of the apartment: ")
    rent = st.number_input("Enter the monthly rent of the apartment: ")
    loan_years = st.number_input("Enter the number of years for the loan: ")

    num_apartments = 0
    monthly_loan_payment = 0

    if st.button("Calculate"):
        # Calculate the time it takes to buy the first apartment
        time_to_buy = 0
        total_savings = 0
        while total_savings < apt_price * 0.2:
            total_savings = total_savings + savings_per_month
            time_to_buy = time_to_buy + 1
            if time_to_buy % 12 == 0:
                years_savings = years_savings - 1

        st.write("It will take ", int(time_to_buy / 12), "years and", time_to_buy % 12,
                 "months to buy your first apartment.")

        # Calculate the number of apartments someone can buy
        while years_savings >= 0:
            total_savings = savings_per_month * years_savings * 12
            if total_savings >= apt_price * 0.2:
                num_apartments = num_apartments + 1
                remaining_loan = (num_apartments * apt_price) - total_savings
                monthly_loan_payment = remaining_loan / (loan_years * 12)
                saving_per_month = savings_per_month + rent - monthly_loan_payment
            years_savings = years_savings - 1

        st.write("You can buy", num_apartments, "apartments until you retire.")


# Main program
st.title("Apartment Calculator")
st.write("This app will calculate the number of apartments you can buy until you retire.")
apt_numbers()
