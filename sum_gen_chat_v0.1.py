#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import streamlit_authenticator as stauth
#----------------------------------------
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import io
import os
import json
import time
import base64
import tempfile
import requests
import warnings
from PIL import Image
from random import randint
from io import BytesIO
warnings.filterwarnings("ignore")
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
#import custom_style()
#image = Image.open('Image_Clariant.png')
st.set_page_config(page_title="Summarization | Generation | Translation | Chatbot | v0.1",
                   layout="wide",
                   initial_sidebar_state="auto",)
#----------------------------------------
st.title("Summarization | Generation | Translation | Chatbot | v0.1")
st.markdown('Developed by : <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>', 
            unsafe_allow_html=True)
st.info('**Disclaimer : :blue[Thank you for visiting the app] |  Click the :blue[sidebar] to follow the instructions to start the applications.**', icon="ℹ️")
#----------------------------------------
# Set the background image
#----------------------------------------
#st.divider()

#---------------------------------------------------------------------------------------------------------------------------------
### Main App
#---------------------------------------------------------------------------------------------------------------------------------
st.sidebar.header("Input", divider='blue')
st.sidebar.info('Please choose from the following options and follow the instructions to start the application.', icon="ℹ️")
action_type = st.sidebar.radio("**:blue[Choose the action]**", ["Information", "Summarization","Generation","Translation","Chatbot",])
st.sidebar.divider()
#-------------------------------------------------------------------
if action_type == "Information" :

    stats_expander = st.expander("**:blue[Description]**", expanded=True)
    with stats_expander:

        col1, col2 = st.columns((0.4,0.6))
        with col1:
            st.subheader("**App Information**", divider='blue')
            st.info('''
                    **This app is developed to do the following course of actions :**
                   
                    - **Summarization**     - It can summarize the different types of documents.
                    - **Generation**        - It can generate contexts (text/image) based on your input prompt. 
                    - **Translation**       - It can translate the input prompt to the chossen language.
                    - **Chatbot**           - It can can give answers based on your queries or thoughts.
                ''')
        
        with col2:
            st.subheader("**Definition | LLM hyperparameters**", divider='blue')
            st.info('''
    
                - **LLM**           - 'Large language Model (LLM)' used for analysis.
                - **Max Tokens**    - the maximum number of tokens that the model can process at once, the maximum length of the prompt and the output of the model.
                - **Temparature**   - a parameter that controls the randomness and creativity of a large language model's (LLM) responses. 
                - **top_p**         - it sets a threshold such that only the words with probabilities greater than or equal to the threshold will be included (sets a cumulative probability threshold).
                - **top_k**         - it is used to limit the number of choices for the next predicted word or token.         
                ''')


#-------------------------------------------------------------------    
if action_type == "Summarization" :
    data_source = st.sidebar.radio("**:blue[Select the file type]**", ["PDF","PPT","Word","Excel/CSV","Image"])
    st.sidebar.divider()    
    data_location = st.sidebar.radio("**:blue[Select the source]**", ["File upload","AWS S3"])
       