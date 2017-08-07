" enable syntax highlighting
syntax enable
set background=dark
" colorscheme solarized
execute pathogen#infect()

set number                      " show line numbers

set ts=4                        " set tabs to have 4 spaces

set autoindent                  " indent when moving to the next line while writing code

set textwidth=120               " break lines when line length increases

set expandtab                   " expand tabs into spaces

set tabstop=4                   " use 4 spaces to represent tab

set shiftwidth=4                " when using the >> or << commands, shift lines by 4 spaces

set showmatch                   " show the matching part of the pair for [] {} and ()

let python_highlight_all = 1    " enable all Python syntax highlighting features

set ruler                       " show line and column number

set backspace=indent,eol,start  " make backspaces more powerfulllll
