import streamlit as st 
import google.generativeai as genai
import os
from dotenv import load_dotenv
#Load the Environment
load_dotenv()
genai.configure(api_key=os.getenv("Manoj-Api-Key"))

st.title("Image to text Application")
user_input=st.text_input("Input Prompt:")

uploaded_file=st.file_uploader("upload the image..",
                          type=["jpg","jpeg","png"])

# Display the image on the page
from PIL import Image
img=""
if uploaded_file is not None:
    img=Image.open(uploaded_file)
    st.image(img,"uploaded_image",use_column_width=True)
    
#function for evaluating the image and annotating it
def gemini_response(user_input,img):
    model=genai.GenerativeModel("gemini-1.5-flash")
    if user_input!="":
        response=model.generate_content([user_input,img])
    else:
        response=model.generate_content(img)
    return response.text
#Create the submit button and map it
submit=st.button("Submit")

if submit:
    response=gemini_response(user_input=user_input,img=img)
    st.subheader("The Response is:")
    st.write(response)