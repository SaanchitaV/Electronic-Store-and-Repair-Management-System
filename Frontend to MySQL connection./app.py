import streamlit as st
from create import create_item,create_user
from database import create_table_user,create_table_item,create_table_purchase,create_table_repair
from delete import delete_user, delete_item
from update import update_user, update_item,update_repair,update_purchase
from read import read_user, read_item,read_purchase,read_repair
from charts import buttons


def main():
    st.title("Electronic store and repair management ")
    menu = ["Add user", "Read user", "Update user", "Remove user","Add item", "Read item", "Update item", "Remove item","View Charts"]
        
    choice = st.sidebar.radio(
            "User and Item Menu",
             key = "Add User",
             options = menu,
        )    
    create_table_user()
    create_table_item()
    create_table_repair()
    create_table_purchase()
    if choice == "Add user":
        st.subheader("Enter user Details:")
        create_user()
    elif choice == "Add item":
        st.subheader("Enter item Details:")
        create_item()
    elif choice == "Remove user":
        st.subheader("Delete created users")
        delete_user()
    elif choice == "Remove item":
        st.subheader("Delete created items")
        delete_item()
    elif choice == "Update user":
        st.subheader("Enter user Details:")
        update_user()
    elif choice == "Update item":
        st.subheader("Enter item Details:")
        update_item()
    elif choice == "Read user":
        st.subheader("Read user details")
        read_user()
    elif choice == "Read item":
        st.subheader("Read item details")
        read_item()
    elif choice == "View Charts":
        st.subheader("Visualizations")
        buttons()



if __name__ == main():
    main()
