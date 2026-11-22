"""Count the ten most frequent words in a UTF-8 file. Case is ignored and ties follow first appearance."""
import argparse
import re
from collections import Counter
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('file', type=Path)
a = p.parse_args()

words = re.findall(r"[^\W_]+(?:['’][^\W_]+)*", a.file.read_text(encoding='utf-8').casefold())
for word, count in Counter(words).most_common(10):
    print(count, word)
