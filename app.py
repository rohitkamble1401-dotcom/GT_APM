from pathlib import Path

import pandas as pd
#import plotly.graph_objects as go
import streamlit as st
from spider_plot import create_spider_plot

st.title("Tryout public webpage")

data_file = Path(__file__).with_name("GT_CC_data.xlsx")
df = pd.read_excel(data_file)

timestamp_column = "Timestamp"
tt_columns = [
    f"TY-GT101-1702.PV__TT{number:02d}"
    for number in range(1, 18)  
]
st.write(tt_columns)

spider_plot_button = st.button("Create Spider Plot")
create_spider_plot(df,tt_columns)     
