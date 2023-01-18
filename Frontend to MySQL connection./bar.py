from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:Skanda&2008@localhost/electronic_store_management")

import pandas as pd
from PIL import Image
import streamlit as st

def create_bar():
    query="SELECT item_type,COUNT( * ) number FROM purchase GROUP BY item_type"
    df = pd.read_sql(query,my_conn)
    print(df)
    lb= [row for row in df['item_type']] # Labels of graph
    plt=df.plot.bar(title="Items Purchased",y='number',x='item_type',figsize=(15,10))
    fig = plt.get_figure()
    fig.savefig("./barchart.png")


    image = Image.open('./barchart.png')

    st.image(image, caption='Bar Chart')

create_bar()