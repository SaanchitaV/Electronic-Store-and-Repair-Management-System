import streamlit as st
from database import add_data_user,add_data_item,add_data_purchase,add_data_repair

def create_user():
   col1, col2 = st.columns(2)
   with col1:
      user_id = st.text_input("User Id:")
      user_gender = st.text_input("Gender:")
      user_age = st.text_input("Age:")
      user_name = st.text_input("Name:")
   with col2:
      user_phone = st.text_input("Phone:")
      user_mail=st.text_input("Mail:")
      user_address=st.text_input("Address:")
      user_feedback = st.text_input("Feedback:")
   if st.button("Add user"):
      add_data_user(user_id,user_gender,user_age,user_name,user_phone,user_mail,user_address,user_feedback)
      st.success("Successfully added user: {}".format(user_name))
   
def create_item():
   col1, col2 = st.columns(2)
   with col1:
      item_id = st.text_input("Item Id:")
      item_type = st.text_input("Item Type:")
      item_brand =st.text_input("Brand:")
      item_warranty=st.text_input("Warranty:")
   with col2:
      item_repair_code = st.text_input("Repair Code:")
      item_version = st.text_input("Version:")
      item_supplier = st.text_input("Supplier:")
   if st.button("Add item"):
      add_data_item(item_id,item_type,item_brand,item_warranty,item_repair_code,item_version,item_supplier)
      st.success("Successfully added item: {}".format(item_type))



