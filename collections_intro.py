from collections import ChainMap
from collections import defaultdict
import os


def check_collections():
    d = defaultdict(lambda: "Not present")
    d['a'] = 1
    print(d['b'])
    pass
