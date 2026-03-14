def get_voice_parameters(style, confidence):

    params = {

        "joyful": {
            "rate": 1.2,
            "pitch": 1.2,
            "volume": 1.0
        },

        "warm_positive": {
            "rate": 1.05,
            "pitch": 1.1,
            "volume": 0.9
        },

        "curious": {
            "rate": 1.0,
            "pitch": 1.15,
            "volume": 0.9
        },

        "sad": {
            "rate": 0.85,
            "pitch": 0.8,
            "volume": 0.8
        },

        "angry": {
            "rate": 1.15,
            "pitch": 1.25,
            "volume": 1.0
        },

        "fearful": {
            "rate": 1.1,
            "pitch": 1.2,
            "volume": 0.9
        },

        "surprised": {
            "rate": 1.25,
            "pitch": 1.3,
            "volume": 1.0
        },

        "neutral": {
            "rate": 1.0,
            "pitch": 1.0,
            "volume": 0.9
        }
    }

    base = params.get(style, params["neutral"])

    # scale intensity with confidence
    scale = 0.5 + confidence

    return {
        "rate": base["rate"] * scale,
        "pitch": base["pitch"] * scale,
        "volume": base["volume"]
    }