import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai 
from langchain_community.vectorstores import FAISS #facebook ai index search
from langchain_google_genai import GoogleGenerativeAIEmbeddings


from config import process_pdf

load_dotenv(override=True)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))