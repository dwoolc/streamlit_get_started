import streamlit as st
import pandas as pd
import numpy as np

# create a sidebar with title, explainer and editable slider
st.sidebar.title("Sidebar Title")
st.sidebar.write("""This is an example sidebar, with a slider to allow an input to be changed""")

# plot slider to the sidebar, return value from it as x to feed the chart
x = st.sidebar.slider("Slide for a number", 10,20)

# make a df taking the slider val as input for length
chart_data = pd.DataFrame(np.random.randn(x,3), columns=['a','b','c'])

# plot the chart
st.line_chart(chart_data)