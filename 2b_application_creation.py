"""
2b_application_creation.py
===========================
Shows the application was imported and tested without errors.

Author : Akshayaa A S
Date   : 2026-10-14
"""
from EmotionDetection.emotion_detection import emotion_detector


def run_tests():
    """Run all emotion detection tests and print results."""
    print("=" * 60)
    print("  EmotionDetection Application Import and Test")
    print("=" * 60)
    print()

    input1 = "I am so happy I am doing this."
    result1 = emotion_detector(input1)
    print("Test 1 - Input  :", input1)
    print("Test 1 - Output :", result1)
    print()

    input2 = "I am really mad about this."
    result2 = emotion_detector(input2)
    print("Test 2 - Input  :", input2)
    print("Test 2 - Output :", result2)
    print()

    input3 = "i feel disgusted just hearing about this"
    result3 = emotion_detector(input3)
    print("Test 3 - Input  :", input3)
    print("Test 3 - Output :", result3)
    print()

    print("=" * 60)
    print("  All tests completed. No errors found.")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
