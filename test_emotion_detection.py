import unittest

from EmotionDetection.emotion_detection import emotion_detector


test_cases = {
    'I am glad this happened': 'joy',
    'I am really mad about this': 'anger',
    'I feel disgusted just hearing about this': 'disgust',
    'I am so sad about this': 'sadness',
    'I am really afraid that this will happen': 'fear',
}

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        for text, emotion in test_cases.items():
            self.assertEqual(emotion_detector(text)['dominant_emotion'], emotion)

unittest.main()