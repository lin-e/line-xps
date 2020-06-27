" pathogen
execute pathogen#infect()

filetype plugin indent on
syntax on

" powerline for vim
if filereadable(expand("~/etc/vim/.vimplug"))
    source ~/etc/vim/.vimplug
endif

python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup

set laststatus=2
set t_Co=256

" search things
set ignorecase
set smartcase
set incsearch
set hlsearch

" UI things
set number
set cursorline
set wildmenu
set showmatch

set mouse=a
