" NerdTree Config
" Open with ctrl+n
map <C-n> :NERDTreeToggle<CR>

" Switch between different windows by their direction
no <C-j> <C-w>j|
no <C-j> <C-w>k|
no <C-j> <C-w>l|
no <C-j> <C-w>h|

" Show hidden files
let NERDTreeShowHidden=1

" Closes after opening a file
let NERDTreeQuitOnOpen=1
