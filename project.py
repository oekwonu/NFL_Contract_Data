import altair as alt
import pandas as pd
import streamlit as st
import numpy as np 

nfl_df = pd.read_csv("nfl_data.csv")
st.cache_data = nfl_df

st.title("NFL & Collegiate Data")
st.markdown(''' 
            Information about NCAA Draft History, NFL Players + Contracts.
            
            *Updated 2022*
            ''')

tab1, tab2= st.tabs(['College Draft Data', 'NFL Player + Contract Data'])

with tab1: 
    st.sidebar.header("Select a College to Display its Draft History")
    college_value = st.sidebar.multiselect('Select College(s):', nfl_df['College'])
   
    filtered_college_list = nfl_df[nfl_df['College'].isin(college_value)]

    st.dataframe(filtered_college_list,use_container_width=True  , column_order=("Player", "College", "Position", "Draft Year", "Draft Team", "Draft Round", "Draft Overall",) )

    draft_chart = alt.Chart(filtered_college_list, title = "# of Draft Picks by College (Visualization)").mark_bar().encode(
        x = 'College',
        y = alt.Y('Otc Id:Q', title="# of Draft Picks", axis=alt.Axis(labels = False)), tooltip= 'College', color = 'College'
    )
    st.altair_chart(draft_chart, use_container_width= True)


with tab2: 
    st.sidebar.header("Select a Player to Display their Information")
    player_list = st.sidebar.multiselect("Select Player(s):", nfl_df['Player'])
    filtered_player_list = nfl_df[nfl_df['Player'].isin(player_list)]

    st.dataframe(filtered_player_list, use_container_width= True, column_order=("Player", "College", "Position", "Value", "Year Signed", "Team", "Years", "Draft Year", "Draft Team", "Draft Round", "Draft Overall") )
