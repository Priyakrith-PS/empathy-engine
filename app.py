from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request
from modules.emotion_detector import detect_emotion
from modules.emotion_mapper import map_emotion_to_style
from modules.tts_engine import generate_audio

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    audio_file = None
    emotion = None
    style = None
    confidence = None   # <-- add this

    if request.method == "POST":

        text = request.form["text"]

        emotion, confidence = detect_emotion(text)

        style = map_emotion_to_style(emotion)

        audio_file = generate_audio(text, style, confidence)

    return render_template(
        "index.html",
        audio_file=audio_file,
        emotion=emotion,
        style=style,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)