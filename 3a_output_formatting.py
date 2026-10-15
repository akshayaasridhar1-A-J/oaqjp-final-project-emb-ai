"""
emotion_detection.py
Core module to detect emotions using Watson NLP API.
"""
import json
import requests

WATSON_NLP_URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

REQUEST_HEADERS = {
    "grpc-metadata-mm-model-id": (
        "emotion_aggregated-workflow_lang_en_stock"
    ),
    "Content-Type": "application/json",
}

EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]


def emotion_detector(text_to_analyse):
    """
    Detect emotions in text using Watson NLP API.

    Args:
        text_to_analyse (str): Customer feedback text.

    Returns:
        dict: Emotion scores and dominant emotion.
    """
    if not text_to_analyse or not text_to_analyse.strip():
        return _build_null_response()

    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(
        url=WATSON_NLP_URL,
        headers=REQUEST_HEADERS,
        json=payload,
        timeout=10,
    )

    if response.status_code == 400:
        return _build_null_response()

    response.raise_for_status()

    response_data = json.loads(response.text)

    try:
        emotion_scores = (
            response_data["emotionPredictions"][0]["emotion"]
        )
    except (KeyError, IndexError) as exc:
        raise ValueError(
            "Unexpected JSON structure in Watson NLP response."
        ) from exc

    result = {
        "anger":   emotion_scores.get("anger",   0.0),
        "disgust": emotion_scores.get("disgust", 0.0),
        "fear":    emotion_scores.get("fear",    0.0),
        "joy":     emotion_scores.get("joy",     0.0),
        "sadness": emotion_scores.get("sadness", 0.0),
    }

    result["dominant_emotion"] = max(
        EMOTIONS, key=lambda emotion: result[emotion]
    )

    return result


def format_emotion_output(result):
    """
    Format emotion result dict into a readable string.

    Args:
        result (dict): Output from emotion_detector().

    Returns:
        str: Formatted emotion summary string.
    """
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


def _build_null_response():
    """
    Build a null response for blank or invalid input.

    Returns:
        dict: All emotion values set to None.
    """
    null_dict = {emotion: None for emotion in EMOTIONS}
    null_dict["dominant_emotion"] = None
    return null_dict
