from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re
import json

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key or not api_key.startswith("AIza"):
    raise ValueError("GOOGLE_API_KEY not found or invalid.")

# Initialize LangChain model 
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Prompt Template
prompt_template = PromptTemplate.from_template("""
Extract the following from this meeting transcript:
1. A 2–3 sentence summary.
2. A list of key decisions.
3. A structured list of action items with task, owner (if available), and deadline (if available).

Return only valid JSON in the following format:
{{
  "summary": "...",
  "decisions": ["..."],
  "actionItems": [{{"task": "...", "owner": "...", "due": "..."}}]
}}

Meeting Transcript:
{meeting_text}
""")

# Output parser
output_parser = StrOutputParser()

# LangChain Expression Chain
model= prompt_template | llm | output_parser

# Flask App
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Gemini Meeting Summarizer is Running</h1>"

@app.route("/process_meeting", methods=["POST"])
def process_meeting():
    try:
        # Getting input
        if request.content_type == "application/json":
            data = request.get_json()
            meeting_text = data.get("text")
        elif 'file' in request.files:
            file = request.files["file"]
            meeting_text = file.read().decode("utf-8")
        else:
            meeting_text = request.get_data(as_text=True)

        if not meeting_text:
            return jsonify({"error": "Meeting text is empty. Provide input as raw text, JSON, or .txt file."}), 400

        # Run model
        response = model.invoke({"meeting_text": meeting_text})

        # Attempt to parse as JSON if needed
        try:
            parsed_output = json.loads(response)
        except json.JSONDecodeError:
            # Clean Markdown code block if present
            cleaned = re.sub(r"^```json|```$", "", response.strip(), flags=re.MULTILINE).strip()
            parsed_output = json.loads(cleaned)

        return jsonify(parsed_output), 200

    except json.JSONDecodeError as e:
        return jsonify({"error": "Failed to parse JSON response.", "raw": response}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
