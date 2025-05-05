import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("hello Stream lit")
st.write("this is a simple text")

##create a simple dataframe
df = pd.DataFrame({'First column':[1,2,3,4],'second column':[10,20,30,40]})

### display the data frame
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
