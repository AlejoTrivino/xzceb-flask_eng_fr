import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_engtofr(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french(None),"")        
    
    def test_frtoeng(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english(None),"")              

if __name__ == '__main__':
    unittest.main()