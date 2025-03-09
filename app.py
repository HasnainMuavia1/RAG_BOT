from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import os

app = Flask(__name__)

# Settings control global defaults
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Groq(model="llama3-70b-8192", api_key="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")

# Initialize the RAG system
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json['message']
        response = query_engine.query(user_message)
        return jsonify({'response': str(response)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 