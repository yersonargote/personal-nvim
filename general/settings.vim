syntax on

set encoding=UTF-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set number
set relativenumber
set cursorline
set showmatch
set expandtab
set smartcase
set autoindent
set smartindent
set clipboard^=unnamed
set clipboard+=unnamedplus
set signcolumn=yes
set nowrap
set scrolloff=26

set undofile
set undodir=~/.config/nvim/undodir/

set termguicolors
set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

" Map escape to ii
:imap ii <Esc>

" Change leader to space
let mapleader=" "

" Copy to clipboard
vnoremap <leader>y "+y
vnoremap <leader>Y "+yg_
