import streamlit as st 

with st.form("form key"):
    st.write("What would you like to order")
    appetizers_val = st.selectbox("Appetizers", options=["choice1", "choice2", "choice3"])
    main_course_val = st.selectbox("Main Course", options=["choice1", "choice2", "choice3"])
    dessert_val = st.selectbox("Dessert", options=["choice1", "choice2", "choice3"])
    checkbox_val = st.checkbox("Are you bringing your own wine?")
    date_val = st.date_input("When are you comming?")
    hours_val = st.time_input("At what time are you comming?")
    text_area = st.text_area("Any allergies?", height=100)
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    # if submitted:
    #     st.write(
    #             "appetizers", appetizers_val, 
    #             "main_course", main_course_val,
    #             "dessert", dessert_val,
    #             "checkbox", checkbox_val,
    #             "date", date_val,
    #             "hours", hours_val,
    #             "text_area", text_area
    #             )

st.write(f"""
        Your order summary:

        Appetizers: {appetizers_val}

        Main course: {main_course_val}

        Dessert: {dessert_val}

        Are you bringing your own wine?: {"yes" if checkbox_val else "no"}

        Comming Date: {date_val}

        Hours: {hours_val}

        Allergies: {text_area}
         """)
