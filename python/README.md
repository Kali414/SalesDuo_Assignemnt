#  Gemini Meeting Summarizer API

A Flask-based API powered by Google Gemini (1.5 Flash) that extracts meaningful insights from meeting transcripts and returns:

- ✅ A concise summary
- ✅ Key decisions
- ✅ Structured action items (with task, owner, and deadline)

---

##  Features

- Accepts input in multiple formats:
  - Raw text
  - JSON body
  - Uploaded `.txt` file
- Returns structured **JSON output**
- Built-in error handling for clean responses
- Easily testable with Postman or curl

---

##  Setup Instructions

## 1. Clone the Repository

```bash
git clone https:https://github.com/Kali414/SalesDuo_Assignemnt.git
cd SalesDuo_Assignemnt
cd python
```
 
## 2. Create and Configure .env File
Create a .env file in the root directory and add your Google Gemini API Key:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

## 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

## 4. Install Requirements
```bash
pip install -r requirements.txt
```

## 5. Run the Flask Server
```bash
python app.py
```

---

## 6. API Usage with Postman Endpoint
```bash
POST http://localhost:5000/process_meeting
```


## 7. Supported Input Formats
### 1. Raw Text (Text Body)
In Postman:
- Go to Body → select raw
- Set Text as format
- Paste meeting content

Example Input:

``` pgsql
The team finalized the launch timeline. Sarah will create the launch assets by July 5.
```

### 2. JSON Input
In Postman:
- Go to Body → raw
- Select JSON format
  
Example Input:
```json

{
  "text": "Kickoff call - June 3\nDecided to hold next review on June 10\nRiya to send slides by June 8"
}
```

### 3. File Upload (.txt)
In Postman:
- Go to Body → form-data
- Key: file, Type: File
- Upload a .txt file with meeting content



## ✅ Sample Output (JSON)
``` json
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

---
## 8. Health Check
Test if the server is running by visiting:

``` arduino
http://localhost:5000/
```

You should see:
```html
<h1>Gemini Meeting Summarizer is Running</h1>
```

---

## 9. File Structure
```
├── app.py               # Main Flask application
├── .env                 # Environment file for Gemini API key
├── requirements.txt     # Python dependencies
└── README.md            # This documentation file
```
