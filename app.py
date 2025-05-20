
import streamlit as st
from chatbot import get_buyer_by_identifier, answer_query

st.set_page_config(page_title="Real Estate Chatbot", layout="centered")
st.title("🏠 Real Estate Preference Chatbot")

st.markdown("### Enter your **name** or **phone number** to begin:")

user_id = st.text_input("Name or Phone")
if user_id:
    buyer = get_buyer_by_identifier(user_id)
    if buyer:
        st.success(f"Hi {buyer['name']}! You can now ask me questions like:")
        st.code("What is my budget?\nWhat is my purpose for buying the property?\nWhat type of property am I looking for?\nWhat are my location Preperences?\nGive me extra details about me..")

        query = st.text_input("Ask a question")
        if query:
            response = answer_query(buyer, query)
            st.markdown(f"**🤖 Chatbot:** {response}")
    else:
        st.error("No matching buyer profile found.")
