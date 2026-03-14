def map_emotion_to_style(emotion):

    mapping = {

        "joy":"joyful",
        "amusement":"joyful",
        "excitement":"joyful",

        "admiration":"warm_positive",
        "approval":"warm_positive",
        "gratitude":"warm_positive",
        "love":"warm_positive",
        "pride":"warm_positive",
        "optimism":"warm_positive",

        "curiosity":"curious",
        "realization":"curious",

        "anger":"angry",
        "annoyance":"angry",
        "disapproval":"angry",

        "sadness":"sad",
        "grief":"sad",
        "disappointment":"sad",
        "remorse":"sad",

        "fear":"fearful",
        "nervousness":"fearful",

        "surprise":"surprised",

        "neutral":"neutral"
    }

    return mapping.get(emotion,"neutral")