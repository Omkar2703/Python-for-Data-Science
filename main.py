import pandas as pd
import streamlit as st


st.set_page_config(page_title="Swiggy Dataset Analysis", page_icon="🍔", layout="wide", initial_sidebar_state="expanded")
# Create a sidebar
st.sidebar.header('Swiggy Dataset Analysis')

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your Swiggy dataset CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Sidebar for choosing OLAP operation
    st.sidebar.header('Choose OLAP Operation')
    olap_operation = st.sidebar.radio(" ", ["Roll-up", "Drill-down", "Slice", "Dice", "Pivot"])

    

    # def user_input_features():
    #     delivery_status = st.sidebar.selectbox('Delivery Status', df['DeliveryStatus'].unique())
    #     restaurant_name = st.sidebar.selectbox('Restaurant Name', df['RestaurantName'].unique())
    #     return delivery_status, restaurant_name

    # delivery_status, restaurant_name = user_input_features()

    # OLAP Operations based on user choice

    if olap_operation == "Roll-up":
        # Perform Roll-up operation
        roll_up_data = df.groupby(['DateOfDelivery']).count().reset_index()
        st.write("Roll-up operation result:\n", roll_up_data)

    elif olap_operation == "Drill-down":
        # Perform Drill-down operation
        drill_down_data = df.groupby(['DeliveryStatus', 'RestaurantName']).count().reset_index()
        st.write("\nDrill-down operation result:\n", drill_down_data)

    elif olap_operation == "Slice":
        # Perform Slice operation
        slice_condition = df['DeliveryStatus'] == 'Delivered'
        sliced_data = df[slice_condition]
        st.write("\nSlice operation result:\n", sliced_data)

    elif olap_operation == "Dice":
        # Perform Dice operation
        dice_condition = (df['DeliveryStatus'] == 'Delivered') & (df['MenuItemName'].str.contains('Pizza'))
        diced_data = df[dice_condition]
        st.write("\nDice operation result:\n", diced_data)

    elif olap_operation == "Pivot":
        # Perform Pivot operation
        pivot_data = df.pivot_table(index='RestaurantName', columns='DeliveryStatus', values='CustomerID', aggfunc='count', fill_value=0)
        st.write("\nPivot operation result:\n", pivot_data)

else:
    st.write("Please upload a Swiggy dataset CSV file.")
