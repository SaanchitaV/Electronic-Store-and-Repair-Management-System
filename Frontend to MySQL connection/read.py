import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_user,view_all_item,view_all_purchase,view_all_repair

def read_user():
 result = view_all_user()
 
 df = pd.DataFrame(result, columns=['user_id','user_gender','user_age','user_name','user_phone','user_mail','user_address','user_feedback']) 
 with st.expander("View all users"):
    st.dataframe(df)

def read_item():
 result = view_all_item()
 df = pd.DataFrame(result, columns=['item_id','item_type','item_brand','item_warranty','item_repair_code','item_version','item_supplier']) 
 with st.expander("View all items"):
    st.dataframe(df)

def read_repair():
 result = view_all_repair()
 df = pd.DataFrame(result, columns=['user_id','item_id','item_type','purchase_id','date_of_purchase','date_of_service','item_repair_code','item_warranty','item_warranty_status']) 
 with st.expander("View all repairs"):
    st.dataframe(df)

def read_purchase():
 result = view_all_purchase()
 df = pd.DataFrame(result, columns=['user_id','user_name','item_id','item_type','purchase_id','date_of_purchase','purchase_amt']) 
 with st.expander("View all purchases"):
    st.dataframe(df)