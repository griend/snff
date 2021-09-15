import sys

from .hello import hello

print(sys.argv)

if len(sys.argv) == 2:
    hello(sys.argv[1])
else:
    hello()

