import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    
    def test_joy_case(self):
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'],'joy')

    def test_anger_case(self):
        self.assertEqual(emotion_detector('I am really mad about this')['dominant_emotion'],'anger')
    def digust_case(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'],'digust')
    def test_sadness_case(self):
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'],'sadness')
    def test_fear_case(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'],'fear')

if "__name__" == "__main__":
    unittest.main()