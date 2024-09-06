# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:23:44 2024

@author: yash
"""

import streamlit as st
import WebAppForCustomerSegmentation as WebApp
import About

#create the menu
st.sidebar.title('Menu')
Page_user = st.sidebar.selectbox(

'Choice',['Prediction for Customer Segmentation','About the author'] 
 
)

#change the pages
if Page_user == 'Prediction for Customer Segmentation':
    WebApp.code()
    
if Page_user == 'About the author':
    About.info()