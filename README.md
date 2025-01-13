# RAG-based PDF Assistant

## Overview
The RAG-based PDF Assistant is a powerful application designed to simplify interaction with document-based content. By leveraging the capabilities of **Llama-Index**, this application creates a seamless experience for exploring, querying, and testing knowledge from PDF documents. With features like a context-aware chat engine and quiz generation, users can easily extract insights and deepen their understanding of any PDF content.

---

## Features

### 1. **Document to Chat Engine**
- The app ingests a PDF document and processes it into smaller, manageable chunks.
- It uses these document chunks to create a **chat engine** that allows users to ask questions about the content.
- The chat engine retrieves relevant sections of the document and provides precise answers in context to the PDF.

### 2. **Quiz Creation**
- The app can generate quizzes based on:
  - The entire PDF content.
  - A specific topic within the document.
- This feature allows users to test their knowledge interactively.

## **Interactive Screencast**
https://github.com/user-attachments/assets/abdde424-e052-4032-8615-b7c1f8a518a2



---

## Advantages

### **Enhanced Learning**
- Users can ask specific questions about the content and get accurate, context-aware answers, making learning more efficient.

### **Knowledge Testing**
- The ability to generate quizzes helps users assess their understanding of the material.

### **Time-Saving**
- Eliminates the need to manually search through lengthy PDFs by providing direct access to relevant sections.

### **Customizable Experience**
- Offers tailored quiz generation based on user-selected topics, ensuring a personalized learning experience.

---

## How It Works

1. **Upload PDF**: Users upload their PDF file to the app.
2. **Document Chunking**: The app processes the PDF into smaller, meaningful chunks using **Llama-Index**.
3. **Chat Engine Creation**: A chat engine is built based on the processed document.
4. **Interactive Features**:
   - **Ask Questions**: Users can query the chat engine for answers.
   - **Generate Quizzes**: Users can request a quiz for the entire document or a specific topic.
5. **Engage and Learn**: Users interact with the chat engine or quiz to enhance their knowledge.

---

## Getting Started

### Prerequisites
- Ensure you have Python installed.

### Run the Application
1. Clone this repository:
   ```bash
   git clone git@github.com:Gruhit13/rag_pdf_assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rag_pdf_assistant
   ```
3. install the required libraries
   ```
   pip install -r requirement.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and interact with the application.

---

## Future Enhancements
- **Multi-document Support**: Allow chat engines to query across multiple PDFs.
- **Enhanced Quiz Options**: Add more quiz types and difficulty levels.
- **Mobile Support**: Develop a mobile-friendly interface for on-the-go learning.

---

## Contributing
We welcome contributions! Feel free to submit issues and pull requests to improve the application.

---
