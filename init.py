# init.py - Initialize workspace with custom .vimrc

import os
import subprocess

assert os.path.exists(".vimrc")

if os.name == "nt":
    print '[~] windows detected - no windows functionality has been added yet... '
    sys.exit(1)
else:
    print '[~] unix!'
    print '[bash] cp .vimrc ~/.vimrc'
    subprocess.call("cp .vimrc ~/.vimrc", shell=True, stdout=subprocess.PIPE)
