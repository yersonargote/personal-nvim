call plug#begin('~/.config/nvim/plugged')

" Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Themes
" Gruvbox
Plug 'morhetz/gruvbox'

" Autopair
Plug 'jiangmiao/auto-pairs'

" Parenthesis and color
Plug 'luochen1990/rainbow'

" NerdTree
Plug 'scrooloose/nerdtree'

" Coc-Completion
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Ale
Plug 'dense-analysis/ale'

" Visual indent
Plug 'Yggdroot/indentLine'

" Telescope
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

" Tree-sitter
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'nvim-treesitter/playground'

" FZF
Plug 'junegunn/fzf', { 'do': { -> fzf#install()  }  }
Plug 'junegunn/fzf.vim'
Plug 'airblade/vim-rooter'

" Nvim lsp
" Plug 'neovim/nvim-lspconfig'
" Plug 'kabouzeid/nvim-lspinstall'
" Plug 'hrsh7th/nvim-compe'
" Plug 'nvim-lua/completion-nvim'

call plug#end()
