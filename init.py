# init.py - Initialize workspace with custom .vimrc
import os

assert os.path.exists(".vimrc")

if os.name == "nt":
    print 'windows'
else:
    print 'unix!'
