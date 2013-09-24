import unittest
from code_golf_scorer import CodeGolfScorer
import os

TEST_FILE = "test_file"

class CodeGolfScorerTest(unittest.TestCase):

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        
    def test_ignores_whitespace_characters(self):
	with open(TEST_FILE, 'w') as f:
	    f.write("some words")

	scorer = CodeGolfScorer()
	self.assertEquals(9, scorer.score(TEST_FILE))

    def test_ignores_newline_characters(self):
	with open(TEST_FILE, 'w') as f:
            f.write("some more words\n")

	scorer = CodeGolfScorer()
	self.assertEquals(13, scorer.score(TEST_FILE))

if __name__ == '__main__':
    unittest.main()
