import os, sys
try:
    __import__("_DEVIL_").login()
except exception as e:
    exit(str(e)) 