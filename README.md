# 📝 Meeting Summarizer API (Python + Node.js)

This repository contains two separate implementations of a **Meeting Summarizer API** that extracts structured insights from meeting transcripts using **Google Gemini API**.
- 🐍 Python (Flask)
- 🟢 Node.js (Express)

Both versions leverage **Google Gemini 1.5 Flash** to extract structured insights from meeting transcripts:

- ✅ A concise summary
- ✅ Key decisions made
- ✅ Action items (task, owner, deadline)

---

## 📂 Project Structure

- /python → Python Flask Langchain implementation
- /node → Node.js Express implementation
- /data → Sample input transcript files

```yaml

Each implementation includes its own:
- API setup
- Route to accept meeting transcript
- Gemini API integration
- Sample output

---

## ✨ Features

- Accepts transcript input in:
  - 🧾 Raw text
  - 🧠 JSON body
  - 📁 Uploaded `.txt` file
- Uses **Gemini 1.5 Flash** model for summarization
- Returns clean and structured **JSON output**
- API documentation & Postman-ready examples

---

## 📊 Sample Output Format

```json
{
  "summary": "The team discussed project deadlines and assigned tasks.",
  "decisions": [
    "Final review scheduled for Sept 15"
  ],
  "actionItems": [
    {
      "task": "Create slide deck",
      "owner": "Alex",
      "due": "Sept 10"
    }
  ]
}

```

## 📦 Install & Run

Each implementation has its **own README** with complete installation and usage instructions.

---

## 📦 Setup Instructions

> 🛠️ Follow the setup and run instructions in the respective folder’s README:

- [Python Flask Setup Guide →](./python/README.md)
- [Node.js Express Setup Guide →](./node/README.md)

Each README includes:
- Installation steps
- Running the local development server
- Testing the `/process_meeting` API route using Postman or curl

---


## 🧪 Example Datasets
Two sample transcript files are included under the /data directory:

example1.txt — Sample meeting transcript with clear responsibilities

example2.txt — A longer, real-world style meeting log

data_json.txt - Use the content of the file , if the transcript data is already structured in JSON format.

You can use these files to test the API by uploading via Postman or passing the text as input.


