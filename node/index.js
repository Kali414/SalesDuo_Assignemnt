const express = require('express');
const multer = require('multer');
const bodyParser = require('body-parser');
const fs = require('fs');
const dotenv = require('dotenv');
const { GoogleGenerativeAI } = require('@google/generative-ai');

// Load environment variables
dotenv.config();

const apiKey = process.env.GOOGLE_API_KEY;
if (!apiKey || !apiKey.startsWith("AIza")) {
  throw new Error("GOOGLE_API_KEY not found or invalid.");
}

// Configure Gemini model
const genAI = new GoogleGenerativeAI(apiKey);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

// Express app setup
const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(bodyParser.text());
app.use(bodyParser.json());

const extractMeetingMinutes = async (meetingText) => {
  const prompt = `
Extract the following from this meeting transcript:
1. A 2–3 sentence summary.
2. A list of key decisions.
3. A structured list of action items with task, owner (if available), and deadline (if available).

Return only valid JSON like:
{
  "summary": "...",
  "decisions": ["..."],
  "actionItems": [{"task": "...", "owner": "...", "due": "..."}]
}

Meeting Transcript:
${meetingText}
`;

  try {
    const result = await model.generateContent(prompt);
    const text = result.response.text().trim();

    // Remove Markdown JSON wrapper if present
    const cleaned = text.replace(/```json|```/g, '').trim();

    return JSON.parse(cleaned);
  } catch (err) {
    throw new Error(`Failed to parse Gemini response: ${err.message}`);
  }
};

// Home route
app.get('/', (req, res) => {
  res.send('<h1>Gemini Meeting Summarizer is Running</h1>');
});

// POST endpoint
app.post('/process_meeting', upload.single('file'), async (req, res) => {
  let meetingText = null;

  try {
    // JSON input
    if (req.is('application/json') && req.body.text) {
      meetingText = req.body.text;
    }
    // Raw text
    else if (req.is('text/plain')) {
      meetingText = req.body;
    }
    // .txt file upload
    else if (req.file) {
      meetingText = fs.readFileSync(req.file.path, 'utf-8');
      fs.unlinkSync(req.file.path); // cleanup file
    }

    if (!meetingText || meetingText.trim().length === 0) {
      return res.status(400).json({ error: "Meeting text is empty. Provide input as raw text, JSON, or a .txt file." });
    }

    const result = await extractMeetingMinutes(meetingText);
    res.status(200).json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
