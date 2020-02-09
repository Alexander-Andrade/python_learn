import unittest
from remove_vowel_extension import RemoveVowelExtension
from word_processor import WordProcessor


class TestRemoveVowelExtension(unittest.TestCase):

    def test_cleanup(self):
        wp = WordProcessor()
        self.assertEqual(wp.process('if you going to San Francisco'), 'f  gng t Sn Frncsc')


if __name__ == '__main__':
    unittest.main()
