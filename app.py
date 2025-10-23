from flask import Flask, render_template, request, jsonify
import whisper
import os
import google.generativeai as genai
import json
import re

<<<<<<< HEAD
# 🔑 Configure Gemini API key
genai.configure(api_key="AIzaSyA7JSfancr3R2mJzTUnt9P6iUw5gcS8w1U")
=======
# 🔑 Set your Gemini API key
genai.configure(api_key="Replace with your key")

>>>>>>> 168480b9a95b93663470c690958bb83505ce2b30

app = Flask(__name__)

# ✅ Load Whisper model once (important for performance)
whisper_model = whisper.load_model("tiny")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        # ✅ Receive uploaded audio file
        audio = request.files.get('audio')
        if not audio:
            return jsonify({"error": "No audio file uploaded"}), 400

        os.makedirs("uploads", exist_ok=True)
        file_path = os.path.join("uploads", audio.filename)
        audio.save(file_path)
        print(f"✅ File received: {file_path}")

        # ✅ Step 1: Transcribe audio
        result = whisper_model.transcribe(file_path)
        transcript = result.get("text", "")
        print("✅ Transcription complete")

        # ✅ Step 2: Generate meeting summary
        summary_prompt = f"""
        You are an AI meeting assistant.
        Summarize the following meeting transcript into a concise and coherent summary, capturing the main points and discussions.
        Keep it clear and easy to read.

        Transcript:
        {transcript}
        """

        gemini_model = genai.GenerativeModel("gemini-2.5-pro")
        response = gemini_model.generate_content(summary_prompt)
        summary_output = response.text.strip() if response and response.text else "No summary generated."

        # ✅ Step 3: Extract decisions & action items
        analysis_prompt = f"""
        You are an AI meeting assistant.
        Analyze the following meeting transcript and extract three things clearly:

        1. Key Decisions – List of decisions finalized.
        2. Action Items – List of actionable tasks with responsible persons and deadlines (if mentioned).

        Return the output in structured JSON format like this:
        {{
          "decisions": ["..."],
          "action_items": [
            {{"task": "...", "assigned_to": "...", "deadline": "..."}}
          ]
        }}

        Transcript:
        {transcript}
        """

        analysis_response = gemini_model.generate_content(analysis_prompt)
        raw_output = analysis_response.text if analysis_response and analysis_response.text else "{}"
        clean_output = re.sub(r"^```json\s*|```$", "", raw_output, flags=re.MULTILINE).strip()

        try:
            parsed_output = json.loads(clean_output)
        except json.JSONDecodeError:
            print("⚠️ Could not parse JSON, returning empty structure.")
            parsed_output = {"decisions": [], "action_items": []}

        # ✅ Return everything to frontend
        return jsonify({
            "transcript": transcript,
            "summary": summary_output,
            "decisions": parsed_output.get("decisions", []),
            "action_items": parsed_output.get("action_items", [])
        })

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host -"0.0.0.0",debug=True)
