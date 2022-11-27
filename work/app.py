from turtle import width 
import streamlit as st 
import pandas as pd 
import numpy as np 
# import leafmap 
import datetime 
from PIL import Image 
import plotly.express as px 
import matplotlib.pyplot as plt

data = pd.read_csv('2014-2016.csv') 
data2 = pd.read_csv('Merged_Features.csv') 
df = pd.read_csv("DELTA_new.csv") 


def main_page():
    st.sidebar.markdown("# Main page")
    st.subheader("TEAM - AZTECH ALURE")   
    st.write("PREDICTION OF TOTAL ELECTRON COUNT WITH VARIATION OF WEATHER SPACE PARAMETERS")    
    st.write("PS ID - SS612")    
    col1, col2 = st.columns((1,1))            
    with col1:   
        img = Image.open('p3.png')   
        nimg = img.resize((150, 150))   
        st.image(nimg)    
            
    with col2:      
        img3 = Image.open('p1.png')   
        nimg = img3.resize((400,200))   
        st.image(nimg) 
    col1, col2 = st.columns(2) 
    


    st.write("Statistical Analysis of Input variables") 
    st.write(data.describe()) 
    



def page2():
            st.markdown('Day Varitions of Input variable') 

            if st.checkbox('line chart'):     
                 
                map = px.line(x ='DAY', y= 'f10.7_index', data_frame=data, title = 'DAY and f10.7_index') 
                st.write(map)  
                 
                map = px.line(x ='DAY', y= 'Kp index  ', data_frame=data, title = 'Kp index and Day') 
                st.write(map)  

                map = px.line(x ='DAY', y= 'R (Sunspot No.)  ', data_frame=data, title = 'Sunspot No. and Day') 
                st.write(map)   
                
                map = px.line(x ='DAY', y= ' Dst-index, nT ', data_frame=data, title = 'Dst index and Day') 
                st.write(map)   
                
                map = px.line(x ='DAY', y= 'ap_index, nT ', data_frame=data, title = 'Ap index and Day') 
                st.write(map)   
            
                map = px.line(x ='DAY', y= 'AE-index, nT', data_frame=data, title = 'Ar index and Day') 
                st.write(map)   
    
            if st.checkbox('scatter chart'):
                map1 = px.scatter(x ='DAY', y= 'f10.7_index', data_frame=data, title = 'DAY and f10.7_index') 
                st.write(map1) 

                map1 = px.scatter(data, x ='DAY', y= 'Kp index  ') 
                st.write(map1)  

                map1 = px.scatter(data, x ='DAY', y= 'R (Sunspot No.)  ') 
                st.write(map1)  

                map1 = px.scatter(data, x ='DAY', y= ' Dst-index, nT ') 
                st.write(map1)   

                map1 = px.scatter(data, x ='DAY', y= 'ap_index, nT ') 
                st.write(map1)   

                map1 = px.scatter(data, x ='DAY', y= 'AE-index, nT') 
                st.write(map1)   





    
   
def page3():
             st.markdown('Hourly Varitions of Input variable') 
             if st.checkbox('Box chart'):     
                 
                map = px.box(x ='HOUR', y= 'f10.7_index', data_frame=data, title = 'DAY and f10.7_index') 
                st.write(map)  
                 
                map = px.box(x ='HOUR', y= 'Kp index  ', data_frame=data, title = 'Kp index and Day') 
                st.write(map)  

                map = px.box(x ='HOUR', y= 'R (Sunspot No.)  ', data_frame=data, title = 'Sunspot No. and Day') 
                st.write(map)   
                
                map = px.box(x ='HOUR', y= ' Dst-index, nT ', data_frame=data, title = 'Dst index and Day') 
                st.write(map)   
                
                map = px.box(x ='HOUR', y= 'ap_index, nT ', data_frame=data, title = 'Ap index and Day') 
                st.write(map)   
            
                map = px.box(x ='HOUR', y= 'AE-index, nT', data_frame=data, title = 'Ar index and Day') 
                st.write(map)   
    
             if st.checkbox('scatter chart'):
                map1 = px.scatter(x ='HOUR', y= 'f10.7_index', data_frame=data, title = 'DAY and f10.7_index') 
                st.write(map1) 

                map1 = px.scatter(data, x ='HOUR', y= 'Kp index  ') 
                st.write(map1)  

                map1 = px.scatter(data, x ='HOUR', y= 'R (Sunspot No.)  ') 
                st.write(map1)  

                map1 = px.scatter(data, x ='HOUR', y= ' Dst-index, nT ') 
                st.write(map1)   

                map1 = px.scatter(data, x ='HOUR', y= 'ap_index, nT ') 
                st.write(map1)   

                map1 = px.scatter(data, x ='HOUR', y= 'AE-index, nT') 
                st.write(map1)   


def page4():
            st.markdown('Tec data variation with time') 
            st.write('Data Visualisation for Tec variations ') 
            map = px.scatter(data2,'timestamp','Tec') 
            st.write(map)

            st.write('Data Visualisation for Tec variations ') 
            fig, ax = plt.subplots(figsize=(20, 5))
            map = px.line(data2,'timestamp','Tec') 
            st.write(map)

def page5():
    
    st.write("TEC variation of Normal day") 
    
    map = px.line(x = 'HOUR', y = 'TEC1', data_frame=df) 
    st.write(map) 
    
    st.write("TEC variation of Disturb day") 
    map1 = px.line(x = 'HOUR', y = 'TEC2', data_frame=df) 
    st.write(map1)

    df['d']= df['TEC1']-df['TEC2']
    st.write("TEC DIFFERENCE between normal day and Disturb day") 
    map2 = px.line(x = 'HOUR', y = 'd', data_frame=df) 
    st.write(map2)

page_names_to_funcs = {
    "HOME Page": main_page,
    "Day Varitions of Input variable": page2,
    "Hourly Varitions of Input variable": page3,
    "Tec data variation": page4,
    "Tec data variation on different days": page5,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()