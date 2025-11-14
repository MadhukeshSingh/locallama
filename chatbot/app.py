from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


##prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        # ("system", "You are a helpful assistant that translates {input_language} to {output_language}."),
        ("system", "You are a helpful assistant. Please answer the following question as best you can. If you don't know the answer, just say that you don't know, don't try to make up an answer."),
        ("user", "Question:{question}")
    ]
)

##streamlit app

def main():

    st.title("ChatGPT with Langchain")
    st.page_config(page_title="ChatGPT with Langchain", page_icon=":robot:")
    st.markdown("This is a simple app that uses ChatGPT with Langchain to answer questions.")
    st.header(":green[Ask a question:]")
    st.subheader("Enter your question below and click 'Submit' to get an answer.")
    input_text = st.text_input("Enter your question here:")


    # st.session_state.last_interaction = time.time()


##llm model

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=500, output_parser=StrOutputParser())





if __name__ == "__main__":
    main()
