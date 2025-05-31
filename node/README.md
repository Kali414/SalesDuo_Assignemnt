# 📝 Gemini Meeting Summarizer API (Node.js + Express)

An API powered by **Google Gemini (1.5 Flash)** built with **Node.js and Express**. It summarizes meeting transcripts and extracts:

- ✅ A 2–3 sentence summary  
- ✅ Key decisions  
- ✅ Structured action items (task, owner, deadline)

---

## 🚀 Features

- Accepts input via:
  - Raw text
  - JSON body (`{ "text": "..." }`)
  - Uploaded `.txt` file
- Returns clean, structured **JSON output**
- Works with Postman or `curl`
- Built-in error handling

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-meeting-summarizer-node.git
cd gemini-meeting-summarizer-node


2. Install Dependencies
```bash
npm install

3. Create .env File
In the root directory, create a .env file:

``` ini
GOOGLE_API_KEY=your_google_gemini_api_key
⚠️ Your key should start with AIza...

4. Start the Server
```bash
node index.js

Server runs at:

```arduino
http://localhost:5000/

🧪 API Usage
🔗 Endpoint
```bash
POST http://localhost:5000/process_meeting

✅ Supported Input Formats
1. Raw Text
In Postman:
Body → raw → Text
Paste your meeting content

Example:

```pgsql
The team finalized the launch timeline. Sarah will create the launch assets by July 5.

2. JSON Input
In Postman:
Body → raw → JSON

Example:

```json
{
  "text": "Kickoff call - June 3\nNext review on June 10\nRiya to send slides by June 8"
}
3. File Upload (.txt)
In Postman:
Body → form-data
Key: file, Type: File, choose a .txt file

✅ Sample Output
```json
{
  "summary": "The team discussed the kickoff and scheduled the next review meeting. Riya is responsible for sending the slides before the deadline.",
  "decisions": [
    "Next review scheduled for June 10"
  ],
  "actionItems": [
    {
      "task": "Send slides",
      "owner": "Riya",
      "due": "June 8"
    }
  ]
}
🔍 Health Check
Visit:

```arduino
http://localhost:5000/

Response:

```html
<h1>Gemini Meeting Summarizer is Running</h1>
📁 File Structure
``` bash
├── index.js             # Main Express server
├── .env                 # Your Gemini API key
├── package.json         # Node project config
└── README.md            # Project documentation
