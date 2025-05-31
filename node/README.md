# Gemini Meeting Summarizer API (Node.js + Express)

An API powered by **Google Gemini (1.5 Flash)** built with **Node.js and Express**. It summarizes meeting transcripts and extracts:

- ✅ A 2–3 sentence summary  
- ✅ Key decisions  
- ✅ Structured action items (task, owner, deadline)

---

##  Features

- Accepts input via:
  - Raw text
  - JSON body (`{ "text": "..." }`)
  - Uploaded `.txt` file
- Returns clean, structured **JSON output**
- Works with Postman or `curl`
- Built-in error handling

---

##  Setup Instructions

### 1. Clone the Repository

```
git clone https:https://github.com/Kali414/SalesDuo_Assignemnt.git
cd SalesDuo_Assignemnt
cd node
```

---

### 2. Install Dependencies
```
npm install
```

### 3. Create .env File
In the root directory, create a .env file:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```
⚠️ Your key should start with AIza...

### 4. Start the Server

```
node index.js
```

Server runs at:
```
http://localhost:5000/
```



### API Usage Endpoint
```
POST http://localhost:5000/process_meeting
```

##  Supported Input Formats
### 1. Raw Text
In Postman:
- Body → raw → Text
-Paste your meeting content

Example:
The team finalized the launch timeline. Sarah will create the launch assets by July 5.

### 2. JSON Input
In Postman:
-Body → raw → JSON

Example:
```json
{
  "text": "Kickoff call - June 3\nNext review on June 10\nRiya to send slides by June 8"
}
```

### 3. File Upload (.txt)
In Postman:
- Body → form-data
- Key: file, Type: File, choose a .txt file

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
```

## Health Check
Visit:
```
http://localhost:5000/
```

### Response:
```
<h1>Gemini Meeting Summarizer is Running</h1>
```

##  File Structure
```
├── index.js             # Main Express server
├── .env                 # Your Gemini API key
├── package.json         # Node project config
└── README.md            # Project documentation
```
