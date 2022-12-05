import pandas as pd 
import streamlit as st
from database import delete_user_db,view_all_user,delete_item_db,view_all_item

def delete_user():
    result = view_all_user()
    df = pd.DataFrame(result, columns=['user_id','user_gender','user_age','user_name','user_phone','user_mail','user_address','user_feedback'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_users = [i[3] for i in view_all_user()]
    selected_user= st.selectbox("Deleting record", list_of_users)
    st.warning("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete user record"):
        delete_user_db(selected_user)
        st.success("user record has been deleted successfully")
    new_result = view_all_user()
    df2 = pd.DataFrame(new_result, columns=['user_id','user_gender','user_age','user_name','user_phone','user_mail','user_address','user_feedback'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_item():
    result = view_all_item()
    df = pd.DataFrame(result, columns=['item_id','item_type','item_brand','item_warranty','item_repair_code','item_version','item_supplier'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_items = [i[0] for i in view_all_item()]
    selected_item= st.selectbox("Deleting record", list_of_items)
    st.warning("Do you want to delete ::{}".format(selected_item))
    if st.button("Delete item record"):
        delete_item_db(selected_item)
        st.success("item record has been deleted successfully")
    new_result = view_all_item()
    df2 = pd.DataFrame(new_result, columns=['item_id','item_type','item_brand','item_warranty','item_repair_code','item_version','item_supplier'])
    with st.expander("Updated data"):
        st.dataframe(df2)