import unittest
from plugin_registration.word_processor import WordProcessor


class TestRemoveVowelExtension(unittest.TestCase):

    def test_cleanup(self):
        wp = WordProcessor()
        self.assertEqual(wp.process('if you going to San Francisco'), 'f  gng t Sn Frncsc')


if __name__ == '__main__':
    unittest.main()
