import pandas as pd
import streamlit as st
from database import view_all_user,get_user,edit_user_data,get_purchase,edit_purchase_data
from database import view_all_item,get_item,edit_item_data,get_repair,edit_repair_data,view_all_repair,view_all_purchase

def update_user():
 result = view_all_user()
 df = pd.DataFrame(result, columns=['user_id','user_gender','user_age','user_name','user_phone','user_mail','user_address','user_feedback'])
 with st.expander("Current users"):
    st.dataframe(df)
 list_of_users = [i[3] for i in view_all_user()]
 selected_user = st.selectbox("user to Edit", list_of_users)
 selected_result = get_user(selected_user)
 if selected_result:
    user_id = selected_result[0][0]
    user_gender = selected_result[0][1]
    user_age = selected_result[0][2]
    user_name = selected_result[0][3]
    user_phone= selected_result[0][4]
    user_mail=selected_result[0][5]
    user_address=selected_result[0][6]
    user_feedback=selected_result[0][7]
    col1, col2 = st.columns(2)
    with col1:
        new_user_id = st.text_input("User Id:",user_id)
        new_user_gender = st.text_input("Gender:",user_gender)
        new_user_age = st.text_input("Age:",user_age)
        new_user_name = st.text_input("Name:",user_name)
    with col2:
        new_user_phone=st.text_input("Phone:",user_phone)
        new_user_mail=st.text_input("Mail:",user_mail)
        new_user_address=st.text_input("Address:",user_address)
        new_user_feedback=st.text_input("Feedback:",user_feedback)
    if st.button("Update user"):
        edit_user_data(new_user_id, new_user_gender, new_user_age, new_user_name, new_user_phone, new_user_mail, new_user_address, new_user_feedback,user_id, user_gender, user_age, user_name, user_phone,user_mail,user_address,user_feedback)
        st.success("Successfully updated {}".format(user_name))
 result2 = view_all_user()
 df2 = pd.DataFrame(result2, columns=['user_id','user_gender','user_age','user_name','user_phone','user_mail','user_address','user_feedback'])
 with st.expander("Updated data"):
    st.dataframe(df2)

def update_item():
 result = view_all_item()
 df = pd.DataFrame(result, columns=['item_id','item_type','item_brand','item_warranty','item_repair_code','item_version','item_supplier'])
 with st.expander("Current items"):
    st.dataframe(df)
 list_of_items = [i[0] for i in view_all_item()]
 selected_item = st.selectbox("Items to Edit", list_of_items)
 selected_result = get_item(selected_item)
 if selected_result:
    item_id = selected_result[0][0]
    item_type = selected_result[0][1]
    item_brand = selected_result[0][2]
    item_warranty = selected_result[0][3]
    item_repair_code = selected_result[0][4]
    item_version=selected_result[0][5]
    item_supplier=selected_result[0][6]
    col1, col2 = st.columns(2)
    with col1:
        new_item_id = st.text_input("Item id:",item_id)
        new_item_type = st.text_input("Item Type:",item_type)
        new_item_brand=st.text_input("Brand:",item_brand)
        new_item_warranty=st.text_input("Warranty(years):",item_warranty)
    with col2:
        new_item_repair_code = st.text_input("Repair Code:",item_repair_code)
        new_item_version = st.text_input("Version:",item_version)
        new_item_supplier = st.text_input("Supplier:",item_supplier)
       
    if st.button("Update items"):
        edit_item_data(new_item_id, new_item_type, new_item_brand, new_item_warranty, new_item_repair_code, new_item_version, new_item_supplier,item_id, item_type, item_brand, item_warranty, item_repair_code, item_version, item_supplier)
        st.success("Successfully updated {},{}".format(new_item_id, new_item_type))
 result2 = view_all_item()
 df2 = pd.DataFrame(result2, columns=['item_id','item_type','item_brand','item_warranty','item_repair_code','item_version','item_supplier'])
 with st.expander("Updated data"):
    st.dataframe(df2)


def update_repair():
 result = view_all_repair()
 df = pd.DataFrame(result, columns=['user_id','item_id','item_type','purchase_id','date_of_purchase','date_of_service','item_repair_code','item_warranty','item_warranty_status'])
 with st.expander("Current items"):
    st.dataframe(df)
 list_of_items = [i[1] for i in view_all_repair()]
 selected_item = st.selectbox("Items to Edit", list_of_items)
 selected_result = get_repair(selected_item)
 if selected_result:
    user_id = selected_result[0][0]
    item_id = selected_result[0][1]
    item_type = selected_result[0][2]
    purchase_id = selected_result[0][3]
    date_of_purchase = selected_result[0][4]
    date_of_service=selected_result[0][5]
    item_repair_code=selected_result[0][6]
    item_warranty = selected_result[0][7]
    item_warranty_status = selected_result[0][8]
    col1, col2 = st.columns(2)
    with col1:
        new_user_id = st.text_input("User id:",user_id)
        new_item_id = st.text_input("Item id:",item_id)
        new_item_type=st.text_input("Item:",item_type)
        new_purchase_id=st.text_input("Purchase Id",purchase_id)
        new_date_of_purchase = st.text_input("Date of Purchase:",date_of_purchase)
    with col2:
        new_date_of_service = st.text_input("Date of service:",date_of_service)
        new_item_repair_code = st.text_input("Repair Code:",item_repair_code)
        new_item_warranty = st.text_input("Warranty:",item_warranty)
        new_item_warranty_status = st.text_input("Warranty Status:",item_warranty_status)
       
    if st.button("Update"):
        edit_repair_data(new_user_id,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_date_of_service,new_item_repair_code,new_item_warranty,new_item_warranty_status,user_id,item_id,item_type,purchase_id,date_of_purchase,date_of_service,item_repair_code,item_warranty,item_warranty_status)
        st.success("Successfully updated {},{}".format(new_item_id, new_item_repair_code))
 result2 = view_all_repair()
 df2 = pd.DataFrame(result2, columns=['user_id','item_id','item_type','purchase_id','date_of_purchase','date_of_service','item_repair_code','item_warranty','item_warranty_status'])
 with st.expander("Updated data"):
    st.dataframe(df2)


def update_purchase():
 result = view_all_purchase()
 df = pd.DataFrame(result, columns=['user_id','user_name','item_id','item_type','purchase_id','date_of_purchase','purchase_amt'])
 with st.expander("Current items"):
    st.dataframe(df)
 list_of_items = [i[2] for i in view_all_purchase()]
 selected_item = st.selectbox("Items to Edit", list_of_items)
 selected_result = get_purchase(selected_item)
 if selected_result:
    user_id = selected_result[0][0]
    user_name = selected_result[0][1]
    item_id = selected_result[0][2]
    item_type = selected_result[0][3]
    purchase_id = selected_result[0][4]
    date_of_purchase=selected_result[0][5]
    purchase_amt=selected_result[0][6]
    col1, col2 = st.columns(2)
    with col1:
        new_user_id = st.text_input("User id:",user_id)
        new_user_name = st.text_input("User name:",user_name)
        new_item_id=st.text_input("Item id:",item_id)
        new_item_type=st.text_input("Item Type",item_type)
    with col2:
        new_purchase_id = st.text_input("Purchase Id:",purchase_id)
        new_date_of_purchase = st.text_input("Date of purchase:",date_of_purchase)
        new_purchase_amt = st.text_input("Purchase Amount:",purchase_amt)
               
    if st.button("Update"):
        edit_purchase_data(new_user_id,new_user_name,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_purchase_amt,user_id,user_name,item_id,item_type,purchase_id,date_of_purchase,purchase_amt)
        st.success("Successfully updated {},{}".format(new_item_id, new_item_type))
 result2 = view_all_purchase()
 df2 = pd.DataFrame(result2, columns=['user_id','user_name','item_id','item_type','purchase_id','date_of_purchase','purchase_amt'])
 with st.expander("Updated data"):
    st.dataframe(df2)