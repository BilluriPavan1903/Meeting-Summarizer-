# 🎧 AI-Powered Audio Summarizer  

An intelligent web application that automatically converts meeting or lecture audio files into **concise, structured summaries**.  
Built using **Python, Flask, Whisper, Google Gemini API**, and **FFmpeg**, the system provides real-time transcription and summarization through a clean web interface.

---

## 🚀 Features  

- 🎙️ **Speech-to-Text Conversion:**  
  Utilizes **OpenAI Whisper** to transcribe audio files into text with high accuracy.  

- 🧠 **AI-Powered Summarization:**  
  Integrates **Google Gemini API** to summarize transcripts into key decisions, action items, and highlights.  

- 🌐 **Flask-Based Backend:**  
  Handles audio uploads, transcription, and summarization seamlessly.  

- ⚙️ **FFmpeg Integration:**  
  Converts uploaded files to supported formats automatically.  

- 💻 **Responsive Frontend:**  
  Simple and interactive web interface built using **HTML, CSS, and JavaScript**.  

- ☁️ **Deployable on Railway / Render / Heroku:**  
  Designed for cloud deployment with minimal setup.

---

The Sample Result:
<img width="1860" height="866" alt="image" src="https://github.com/user-attachments/assets/dd558f0c-6004-4b1b-84b8-f443bb1a1be3" />

the sample video how to use for testing :
https://drive.google.com/file/d/1Oelm2eI97_Eq14SDUZLBd7VtnC6ZY8EJ/view?usp=sharing



## 🧩 Tech Stack  

| Component | Technology Used |
|------------|----------------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, JavaScript |
| Speech Recognition | OpenAI Whisper |
| NLP Model | Google Gemini API |
| Audio Processing | FFmpeg |


---



🧠 Example Output

Input:

A 5-minute meeting audio file discussing project timelines.

Output:
Key Decisions: Project deadline extended to next quarter.
Action Items: Team to submit revised schedule by Friday.
Summary: Meeting focused on project delays and timeline adjustments.

# 1️⃣ Clone the Repository
git clone https://github.com/BilluriPavan1903/Meeting-Summarizer-.git
cd Meeting-Summarizer

# 2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Add your Google Gemini API key
set GEMINI_API_KEY=your_google_gemini_api_key   # Windows
export GEMINI_API_KEY=your_google_gemini_api_key  # macOS/Linux

# 5️⃣ Run the App
python app.py



📞 Contact
👤 B. Pavan Srinivasa Rao
📧 billuripavan891@gmail.com
📱 +91 70137 99733















