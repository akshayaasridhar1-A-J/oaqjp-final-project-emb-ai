"""
server.py
Flask web application server for Emotion Detection System.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector, format_emotion_output

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze emotion from query parameter textToAnalyze.

    Returns:
        JSON response with emotion scores or error message.
    """
    text_to_analyze = request.args.get(
        "textToAnalyze", ""
    ).strip()

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({
            "error":   True,
            "message": "Invalid text! Please try again!",
        }), 400

    formatted_output = format_emotion_output(result)

    return jsonify({
        "error":            False,
        "anger":            result["anger"],
        "disgust":          result["disgust"],
        "fear":             result["fear"],
        "joy":              result["joy"],
        "sadness":          result["sadness"],
        "dominant_emotion": result["dominant_emotion"],
        "formatted_output": formatted_output,
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
