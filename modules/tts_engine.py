from google.cloud import texttospeech
from google.oauth2 import service_account


# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    "ivory-setup-490213-t2-3668870161f2.json"
)

client = texttospeech.TextToSpeechClient(credentials=credentials)


def generate_audio(text, style, confidence, filename="static/audio/output.mp3"):

    style_map = {
        "joyful": (5, 1.1),
        "warm_positive": (3, 1.05),
        "curious": (3, 1.0),
        "sad": (-3, 0.9),
        "angry": (6, 1.1),
        "fearful": (4, 1.05),
        "surprised": (7, 1.15),
        "neutral": (0, 1.0)
    }

    pitch_base, rate_base = style_map.get(style, (0, 1.0))

    # intensity scaling using confidence
    scale = 0.8 + (confidence * 0.4)

    pitch = f"{pitch_base * scale}st"

    rate_value = rate_base * scale

    # clamp rate to avoid unnatural speed
    rate_value = max(0.85, min(rate_value, 1.25))
    rate = str(rate_value)

    # Emotion-specific SSML behavior
    if style == "sad":

        ssml = f"""
        <speak>
            <break time="300ms"/>
            <prosody pitch="{pitch}" rate="{rate}">
                {text}
            </prosody>
        </speak>
        """

    elif style == "surprised":

        ssml = f"""
        <speak>
            <break time="150ms"/>
            <prosody pitch="{pitch}" rate="{rate}">
                {text}
            </prosody>
        </speak>
        """

    elif style == "angry":

        ssml = f"""
        <speak>
            <prosody pitch="{pitch}" rate="{rate}">
                <emphasis level="strong">{text}</emphasis>
            </prosody>
        </speak>
        """

    elif style == "joyful":

        ssml = f"""
        <speak>
            <prosody pitch="{pitch}" rate="{rate}">
                <emphasis level="moderate">{text}</emphasis>
            </prosody>
        </speak>
        """

    else:

        ssml = f"""
        <speak>
            <prosody pitch="{pitch}" rate="{rate}">
                {text}
            </prosody>
        </speak>
        """

    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-J"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(filename, "wb") as out:
        out.write(response.audio_content)

    return filename