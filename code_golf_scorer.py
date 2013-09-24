import os
import re

class CodeGolfScorer:
    
    def score(self, filename):
        with open(filename, 'r') as f:
	    contents = f.read()
	    contents_without_whitespace = re.sub(r'\s', '', contents)
	    return len(contents_without_whitespace)
