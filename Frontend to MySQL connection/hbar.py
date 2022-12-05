from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:Skanda&2008@localhost/electronic_shop_and_repair_management_364")

import pandas as pd
from PIL import Image
import streamlit as st

def create_hbar():
    query="SELECT item_brand,COUNT( * ) number FROM item GROUP BY item_brand"
    df = pd.read_sql(query,my_conn)
    #print(df)
    lb= [row for row in df['item_brand']] # Labels of graph
    plt=df.plot.barh(title="Item Brands",y='number',x='item_brand')
    fig = plt.get_figure()
    fig.savefig("./hbarchart.png")


    image = Image.open('./hbarchart.png')

    st.image(image, caption='Horizontal Bar Chart')


