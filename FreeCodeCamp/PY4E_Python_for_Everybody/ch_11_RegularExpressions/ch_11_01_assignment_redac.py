# See README.md for assignment brief.
# Wanted to try my hand at a redacted version of the code.

import re

print(sum([int(i) for i in re.findall('[0-9]+',open("regex_sum_941919.txt").read())]))
