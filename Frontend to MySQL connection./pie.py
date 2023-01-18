"""import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt"""

"""import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",
                               password="Skanda&2008", database="Electronic_shop_and_repair_management_364")
c = mydb.cursor()"""

from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:Skanda&2008@localhost/electronic_store_management")

"""def get_m_size():
    c.execute('SELECT COUNT(user_gender) FROM user WHERE user_gender="Male"')
    data = c.fetchone()
    return data 

def get_f_size():
    c.execute('SELECT COUNT(user_gender) FROM user WHERE user_gender="Female"')
    data = c.fetchone()
    return data

labels = 'Male','Female'
m_size = get_m_size()
f_size = get_f_size()
sizes = [m_size,f_size]

fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=None, labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')

st.pyplot(fig1)
"""
import pandas as pd
from PIL import Image
import streamlit as st

def create_pie():
    query="SELECT item_type,COUNT( * ) n FROM item GROUP BY item_type"
    df = pd.read_sql(query,my_conn)
    #print(df)
    lb= [row for row in df['item_type']] # Labels of graph
    plt=df.plot.pie(title="Items ",y='n',labels=lb,autopct='%1.2f%%')
    fig = plt.get_figure()
    fig.savefig("./piechart.png")


    image = Image.open('./piechart.png')

    st.image(image, caption='Pie Chart')

