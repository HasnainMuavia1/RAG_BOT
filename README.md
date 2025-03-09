# RAG Bot

A Retrieval-Augmented Generation chatbot built with HTML, CSS, JavaScript, Bootstrap for the frontend and Flask for the backend.

## Description

This application allows users to interact with a chatbot that can answer questions based on their own documents. The RAG (Retrieval-Augmented Generation) architecture enables the bot to retrieve relevant information from user-provided documents and generate accurate, contextual responses.

## Features

- Interactive chat interface
- Document-based knowledge retrieval
- Support for PDF documents
- Responsive design with Bootstrap
- Real-time response generation

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/HasnainMuavia1/RAG_BOT
cd rag-bot
```

### 2. Create a virtual environment

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Adding Your Documents

1. Locate the `data` folder in the project root directory
2. Add your PDF documents to this folder
3. The bot will automatically process and index these documents for retrieval

## Running the Application

### 1. Start the Flask server

```bash
flask run
```
or
```bash
python app.py
```

### 2. Access the web interface

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. Type your question in the chat input field
2. Press Enter or click the Send button
3. The bot will retrieve information from your documents and generate a response
4. Continue the conversation as needed

## Troubleshooting

### Common Issues:

- **Documents not being recognized**: Ensure your PDFs are in the correct format and placed in the `data` folder
- **Server won't start**: Check that all dependencies are installed and the virtual environment is activated
- **Slow responses**: Large or numerous documents may require more processing time

## Project Structure

```
rag-bot/
├── app.py                 # Flask application entry point
├── templates/             # HTML templates
├── data/                  # Store your PDF documents here
└── venv/                  # Virtual environment (created during setup)
```

## License

[Hasnain Muavia]

## Acknowledgements

- Flask
- Bootstrap
- [Any other libraries or resources used]
