# Empathy Engine

Empathy Engine is an AI-powered system that detects emotions in text and generates emotionally expressive speech using neural text-to-speech.

The system analyzes user input, detects emotional tone using a transformer-based emotion classifier, and modulates speech synthesis parameters such as pitch, rate, and emphasis to produce natural expressive speech.

---

## Features

- Emotion detection using GoEmotions (27 emotion classes)
- Emotion-to-speech style mapping
- Dynamic pitch and speech rate modulation
- SSML emphasis and pauses for emotional realism
- Neural speech synthesis using Google Cloud Text-to-Speech
- Simple interactive web interface using Flask

---

## Architecture

                +----------------------+
                |     User Input       |
                |  (Text Sentence)    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Emotion Detection   |
                |   GoEmotions BERT    |
                |   (27 emotions)      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Emotion Mapping      |
                | 27 emotions ->       |
                | speech styles        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Voice Controller     |
                | pitch scaling        |
                | rate scaling         |
                | SSML emphasis        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Google Neural TTS    |
                | (Neural2-J voice)    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Audio Output (.mp3) |
                +----------------------+

---

## Tech Stack

- Python
- Flask
- HuggingFace Transformers
- PyTorch
- Google Cloud Text-to-Speech
- HTML / CSS

---

## Installation

Clone the repository:

git clone https://github.com/Priyakrith_PS/empathy-engine.git

cd empathy-engine

## Install dependencies:

pip install -r requirements.txt

- Place your Google Cloud service account JSON file in the project root.

- Then run the application:

python app.py

Open in browser:

http://localhost:5000/

---

---

## Example Inputs

Joy: I am extremely excited about this opportunity!

Sadness: I feel very disappointed today.

Anger: This situation is extremely frustrating!

Surprise: Wait... what just happened?!

---
## Demo

![Empathy Engine Demo](screenshot.png)


## Future Improvements

- Real-time speech streaming
- Emotion detection from voice input
- More expressive voice synthesis models
- Multilingual emotional speech generation

---

## Author

Priyakrith P S
priyakrith.ps@gmail.com
+91 - 6282376117
