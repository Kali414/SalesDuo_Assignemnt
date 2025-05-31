from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import re

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Check API key
if not api_key or not api_key.startswith("AIza"):
    raise ValueError("GOOGLE_API_KEY not found or invalid.")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

def extract_meeting_minutes(meeting_text):
    prompt = f"""
Extract the following from this meeting transcript:
1. A 2–3 sentence summary.
2. A list of key decisions.
3. A structured list of action items with task, owner (if available), and deadline (if available).

Return only valid JSON like :
{{
  "summary": "...",
  "decisions": ["..."],
  "actionItems": [{{"task": "...", "owner": "...", "due": "..."}}]
}}

Meeting Transcript:
{meeting_text}
"""

    try:
        response = model.generate_content(prompt)
        text_response = response.text.strip()

        # Strip Markdown code block if exists
        cleaned_text = re.sub(r"^```json|```$", "", text_response.strip(), flags=re.MULTILINE).strip()

        # Parse as JSON directly
        parsed = json.loads(cleaned_text)

        return jsonify(parsed), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse response as JSON", "raw": text_response}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to test if app is running
@app.route("/")
def home():
    return "<h1>Gemini Meeting Summarizer is Running</h1>"

# Endpoint to process meeting input
@app.route("/process_meeting", methods=["POST"])
def process_meeting():
    meeting_text = None

    if request.content_type == "application/json":
        data = request.get_json()
        meeting_text = data.get("text")
        
    elif 'file' in request.files:
        file = request.files["file"]
        meeting_text = file.read().decode("utf-8")
    else:
        meeting_text = request.get_data(as_text=True)

    if not meeting_text:
        return jsonify({"error": "Meeting text is empty.Provide input either as Raw text,JSON text or a .txt file upload."}), 400

    return extract_meeting_minutes(meeting_text)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
