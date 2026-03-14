from transformers import pipeline

# Load GoEmotions model
emotion_classifier = pipeline(
    "text-classification",
    model="monologg/bert-base-cased-goemotions-original",
    top_k=None
)

def detect_emotion(text: str):
    """
    Detect emotion from input text using GoEmotions model.
    Returns:
        emotion_label (str)
        confidence_score (float)
    """

    predictions = emotion_classifier(text)[0]

    # find highest scoring emotion
    top_emotion = max(predictions, key=lambda x: x["score"])

    emotion_label = top_emotion["label"]
    confidence = float(top_emotion["score"])

    return emotion_label, confidence