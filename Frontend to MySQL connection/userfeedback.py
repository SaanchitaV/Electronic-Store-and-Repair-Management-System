from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:Skanda&2008@localhost/electronic_shop_and_repair_management_364")

import pandas as pd
from PIL import Image
import streamlit as st

def feedback():
    query="SELECT user_feedback,\
    sum(CASE WHEN user_gender ='Male' THEN 1 ELSE 0 END) as Male,\
    sum(CASE WHEN user_gender ='Female' THEN 1 ELSE 0 END) as Female\
    FROM user group by user_feedback"    
    df = pd.read_sql(query,my_conn)
    plt=df.plot.barh(title="User feedback",x='user_feedback',stacked=True)
    fig = plt.get_figure()
    fig.savefig("./feedback.png")


    image = Image.open('./feedback.png')

    st.image(image, caption='Feedback Chart')

feedback()