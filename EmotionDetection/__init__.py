"""
EmotionDetection Package
========================
A Python package that provides emotion analysis of customer
feedback text using the IBM Watson NLP Emotion Prediction API.

Usage
-----
    from EmotionDetection import emotion_detector
    from EmotionDetection import format_emotion_output

    result = emotion_detector("I love this product")
    print(result["dominant_emotion"])
    print(format_emotion_output(result))

Author  : Akshayaa A S
Version : 1.0.0
"""
from .emotion_detection import emotion_detector        # noqa: F401
from .emotion_detection import format_emotion_output   # noqa: F401

__version__ = "1.0.0"
__author__  = "Akshayaa A S"
__all__     = ["emotion_detector", "format_emotion_output"]
