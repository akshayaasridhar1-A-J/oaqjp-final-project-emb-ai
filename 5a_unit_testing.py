"""Unit tests for the EmotionDetection package."""
import unittest
from EmotionDetection import emotion_detector, format_emotion_output


class TestEmotionDetector(unittest.TestCase):
    """Tests for emotion_detector() function."""

    def test_emotion_joy(self):
        """Joy text returns joy as dominant emotion."""
        result = emotion_detector(
            "I am so happy I am doing this."
        )
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_anger(self):
        """Anger text returns anger as dominant emotion."""
        result = emotion_detector(
            "I am absolutely furious! This is unacceptable!"
        )
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_disgust(self):
        """Disgust text returns disgust as dominant emotion."""
        result = emotion_detector(
            "I feel disgusted. This is revolting and repulsive."
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_fear(self):
        """Fear text returns fear as dominant emotion."""
        result = emotion_detector(
            "I am terrified and very scared and anxious."
        )
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_emotion_sadness(self):
        """Sadness text returns sadness as dominant emotion."""
        result = emotion_detector(
            "I am deeply saddened. It is a miserable experience."
        )
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_blank_input_dominant_none(self):
        """Blank input returns dominant_emotion as None."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

    def test_blank_input_scores_none(self):
        """Blank input returns all scores as None."""
        result = emotion_detector("")
        for emotion in ["anger", "disgust", "fear", "joy", "sadness"]:
            with self.subTest(emotion=emotion):
                self.assertIsNone(result[emotion])

    def test_format_valid_output(self):
        """format_emotion_output returns correct string format."""
        result    = emotion_detector("I love this product.")
        formatted = format_emotion_output(result)
        self.assertIn("'anger':",         formatted)
        self.assertIn("'disgust':",       formatted)
        self.assertIn("'joy':",           formatted)
        self.assertIn("dominant emotion", formatted)

    def test_format_null_output(self):
        """format_emotion_output on null returns error string."""
        result    = emotion_detector("")
        formatted = format_emotion_output(result)
        self.assertEqual(
            formatted,
            "Invalid text! Please try again!"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
