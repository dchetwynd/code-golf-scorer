import os
import re
import sys

class CodeGolfScorer:
    
    def score(self, filename):
        with open(filename, 'r') as f:
	    contents = f.read()
	    contents_without_whitespace = re.sub(r'\s', '', contents)
	    return len(contents_without_whitespace)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("You must provide a filename argument")

    scorer = CodeGolfScorer()
    character_count = scorer.score(sys.argv[1])

    print "The file has %d characters" % character_count
