from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types
import os
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure Google AI API
from dotenv import load_dotenv
import os

load_dotenv()  # .env file load karne ke liye
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"response": "Please provide a message."})
        
        # Use Google AI API for response
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=user_message
            )
            ai_response = response.text
        except Exception as api_error:
            # Fallback if API fails
            ai_response = f"I understand your message: '{user_message}'. This is a simulated response as the AI service is currently unavailable. Error: {str(api_error)}"
        
        return jsonify({"response": ai_response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        content_type = data.get('type', 'article')
        topic = data.get('topic', '')
        tone = data.get('tone', 'professional')
        
        prompt = f"Write a {tone} {content_type} about '{topic}'. Make it engaging and informative."
        
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            generated_content = response.text
        except Exception as api_error:
            generated_content = f"Here would be a {tone} {content_type} about '{topic}'. API Error: {str(api_error)}"
        
        return jsonify({"content": generated_content})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/code-help', methods=['POST'])
def code_help():
    try:
        data = request.get_json()
        language = data.get('language', 'python')
        task = data.get('task', '')
        
        prompt = f"Write {language} code for: {task}. Provide clean, well-commented code."
        
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            code_response = response.text
        except Exception as api_error:
            code_response = f"# {language} code for: {task}\n# API temporarily unavailable. Error: {str(api_error)}"
        
        return jsonify({"code": code_response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analyze-data', methods=['POST'])
def analyze_data():
    try:
        data = request.get_json()
        data_input = data.get('data', '')
        analysis_type = data.get('analysis_type', 'general')
        
        prompt = f"Analyze this data from a {analysis_type} perspective: {data_input}. Provide key insights and recommendations."
        
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            analysis_result = response.text
        except Exception as api_error:
            analysis_result = f"Analysis of the provided data would appear here. API Error: {str(api_error)}"
        
        return jsonify({"analysis": analysis_result})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "WhaThink AI API is running"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
