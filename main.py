import streamlit as st
import plotly.express as px
import pandas as pd
import nltk
from pathlib import Path
from streamlit_option_menu import option_menu
from threading import Thread, Event
from utils import generate_insights, speak_insights, stop_event
import os
import tempfile
from streamlit_chat import message
from pandasai import SmartDataframe # SmartDataframe for interacting with data using LLM
from pandasai.llm.local_llm import LocalLLM

DB_FAISS_PATH = "vectorstore/db_faiss"




def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model = "llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.0
    )
    return llm

def streamlit_ui():
    with st.sidebar:
        choice = option_menu('Navigation', ['Home', 'Data analysis'], default_index=0)

    if choice == 'Home':
        st.title("Hi, Welcome to DataQuest \n We Make Data Exploration Easier Using LLM")
        st.video("the stream.mp4")

    elif choice == 'Data analysis':
        st.title("Data Analysis Dashboard")
                # Function to chat with CSV data
        def chat_with_csv(df,query):
            # Initialize LocalLLM with Meta Llama 3 model
            llm = LocalLLM(
            api_base="http://localhost:11434/v1",
            model="llama3")
            # Initialize SmartDataframe with DataFrame and LLM configuration
            pandas_ai = SmartDataframe(df, config={"llm": llm})
            # Chat with the DataFrame using the provided query
            result = pandas_ai.chat(query)
            return result

        # Set layout configuration for the Streamlit page
        
        # Set title for the Streamlit application
        st.title("Multiple-CSV ChatApp powered by LLM")

        # Upload multiple CSV files
        input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)

        # Check if CSV files are uploaded
        if input_csvs:
            # Select a CSV file from the uploaded files using a dropdown menu
            selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
            selected_index = [file.name for file in input_csvs].index(selected_file)

            #load and display the selected csv file 
            st.info("CSV uploaded successfully")
            data = pd.read_csv(input_csvs[selected_index])
            st.dataframe(data.head(3),use_container_width=True)

            #Enter the query for analysis
            st.info("Chat Below")
            input_text = st.text_area("Enter the query")

            #Perform analysis
            if input_text:
                if st.button("Chat with csv"):
                    st.info("Your Query: "+ input_text)
                    result = chat_with_csv(data,input_text)
                    st.success(result)

                            

if __name__ == "__main__":
    streamlit_ui()
