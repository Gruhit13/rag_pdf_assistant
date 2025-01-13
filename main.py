from dotenv import load_dotenv
load_dotenv()

import os

from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.readers.file import PDFReader
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import streamlit as st

class QuizQuestion(BaseModel):
    question: str = Field(..., description="Quiz question")
    options: List[str] = Field(..., description="List of 4 options for this question. Out of which one is correct")
    answer: int = Field(..., description="The correct option for the question [0, 1, 2, 3] mapping to 4 options provided")
    
class ModelResponse(BaseModel):
    is_quiz: bool = Field(..., description="True if current response is quiz question else False")
    answer: str = Field(..., description="It will be N/A if the user has asked to generate quiz question else it will answer to user's question")
    quiz_questions: Optional[List[QuizQuestion]] = Field(..., description="If is_quiz is True then this will be the list of quiz questions else it will be N/A.")


st.set_page_config(
    page_title="Chat with the PDF Assistant", 
    page_icon="🦙", layout="centered", 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("Chat with the PDF Assistant")
st.markdown("Powered by Groq and LlamaIndex 💬🦙.")

@st.cache_resource(show_spinner=False)
def update_llama_index_settings():
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    sllm = Groq(model="llama-3.3-70b-versatile").as_structured_llm(output_cls=ModelResponse)
    print("Llama-index Setting updated")
    return sllm

# Calling the cached resources once
SLLM = update_llama_index_settings()

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me question about anything."
        }
    ]

if "enable_chat" not in st.session_state:
    st.session_state.enable_chat = False

def on_file_upload():
    upload_file = st.session_state.get('pdf_file', None)
    print("File Uploaded: ", upload_file)
    
    if upload_file is not None:
        with open(upload_file.name, 'wb') as w:
            w.write(upload_file.getvalue())

        pdf_reader = PDFReader()
        docs = pdf_reader.load_data(file=Path(upload_file.name))

        print("Embed Model loaded successfully")
        index = VectorStoreIndex.from_documents(docs, show_progress=True)
        chat_engine = index.as_chat_engine(
            similarity_top_k=4,
            chat_mode="condense_plus_context",
            llm=SLLM,
            context_prompt=(
                "You are an experience Professor with years of experience"
                "You generated either MEANINGFUL quiz questions or provide answer to user's query."
                "Here are the relevant documents for context:\n"
                "{context_str}"
                "Whatever you do you always stay adhere to strict response structure provided to you."
                "NOTE: if you generate quiz please exclude questions related to Charts, Figures, Tables, etc things"
                "Make sure that the question you answer and quiz you generate and throughly accurate and not hallucinated."
            )
        )

        st.session_state['chat_engine'] = chat_engine
        st.session_state.enable_chat = True
        print("Session has been set")
        st.toast("File has been processed successfully", icon=":material/thumb_up:")
    else:
        del st.session_state.chat_engine
        st.session_state.enable_chat = False

with st.sidebar:
    st.file_uploader(
        label="Chose a file to upload",
        key="pdf_file",
        type="pdf",
        on_change=on_file_upload
    )

if st.session_state.enable_chat:
    if prompt := st.chat_input("Ask a question."):
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

    if st.session_state.messages[-1]['role'] != 'assistant' and prompt is not None:
        with st.chat_message("assistant"):
            response = st.session_state.chat_engine.chat(prompt)
            response_obj = ModelResponse.model_validate_json(response.response)
            
            if response_obj.is_quiz:
                st.session_state['quiz_questions'] = response_obj.quiz_questions
                st.write("Created quiz. Check the quiz page")
                message = {"role": "assistant", "content": "Created quiz. Check the quiz page"}
            else:
                st.write(response_obj.answer)
                message = {"role": "assistant", "content": response_obj.answer}
            
            st.session_state.messages.append(message)