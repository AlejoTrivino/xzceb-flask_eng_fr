import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_engtofr(self):
        self.assertEqual(english_to_french(None),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    
    def test_frtoeng(self):
        self.assertEqual(french_to_english(None),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")        

if __name__ == '__main__':
    unittest.main()