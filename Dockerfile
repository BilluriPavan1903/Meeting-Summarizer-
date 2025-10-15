# Use lightweight Python image
FROM python:3.10-slim

# Install system dependencies (FFmpeg required for Whisper)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Hugging Face listens on 7860)
EXPOSE 7860

# Command to start the Flask app
CMD ["python", "app.py"]