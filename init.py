# init.py - Initialize workspace with custom .vimrc

import os
import subprocess

assert os.path.exists(".vimrc")

if os.name == "nt":
    print '[~] windows detected - no windows functionality has been added yet... '
    sys.exit(1)
else:
    cmds = ['cp .vimrc ~/.vimrc',
            'mkdir -p ~/.vim/autoload ~/.vim/bundle &&  \
             curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim']

    print '[~] unix!'
    for cmd in cmds:
        print '[bash] %s' % cmd
        subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)
