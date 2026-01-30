import streamlit as st
import pandas as pd 

#building the sidebar using object notation 
# st.sidebar.title("Finance Flow")

# st.sidebar.write("Personal Dashboard")


page = st.sidebar.radio(
    "Navigation",["Dashboard","Daily Expenses","Monthly Budget",
                  "Savings Goals","Debt Tracker","Insights"]
)

st.sidebar.divider()

st.sidebar.info("Pro Tip")


#building main dashboard layout
if page == "Dashboard":

    st.header("Welcome back")
    st.write("Here is your financial overview for January 2026!")

#building metrics 
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Balance", "$12,450.00", "+12%")
    with col2:
        st.metric("Monthly Expenses","$468.98","-8%")
    with col3:
        st.metric("Total Savings", "$31,300.00","+15%")
    with col4:
        st.metric("Total Debt","$33,700","+5")

    #building the charts row 
    l_col , r_col = st.columns(2)

    with l_col:
        st.subheader("Monthly Spending Trend")
        st.info("A line chart will go here")
    
    with r_col:
        st.subheader("Budget Overview")
        st.write("Food and Dining")
        st.progress(0.7)

        st.write("Transportation")
        st.progress(0.85)

        st.write("Shopping")
        st.progress(0.9)

    st.subheader("Recent Expenses")
    st.write("Grocery shopping - $85.50")

    st.write("Gas - $45.00")

    st.write("Netflix subscription - $15.99 ")

    st.write("Electric bill - $120.00")

    #building the daily expense page layout 
elif page == "Daily Expenses":
    st.header("Daily Expenses")
    st.write("Track your daily expenses")

    #adding "add expense" form #the input layer
    if "daily_expenses" not in st.session_state:
        st.session_state.daily_expenses = []
    
    with st.form("expense form"):
        item = st.text_input("add item")
        amount = st.number_input("add amount(Ghs)")
        submit_button = st.form_submit_button("add expense")

        if submit_button:
            if item == "":
                st.error("Please add an item")
            elif amount <= 0:
                st.error("Please add a valid amount")
            else:
                st.session_state.daily_expenses.append({
                    "Item" : item,
                    "Amount" : amount
                })
                st.success(f"Added {item} for GHS {amount}")

    if st.session_state.daily_expenses: #turning our stored data into a dataframe
       st.subheader("Today's Expenses")

       df= pd.DataFrame(st.session_state.daily_expenses)

       st.dataframe(df, use_container_width= "True")

       total_spent = df["Amount"].sum()
       st.metric("Total spent today(GHS)",f"{total_spent:.2f}")

       st.subheader("Spending Breakdown")
       st.bar_chart(df.set_index("Item")["Amount"])
    else:
        st.write("No expenses added")





    
        





    





