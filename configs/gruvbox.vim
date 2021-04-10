"-----------------------------------------------------------------------------
" Gruvbox

let g:gruvbox_contrast_dark='hard'
if exists('+termguicolors')
    let &t_8t = "/<Esc>[38;2;%lu;%lu%lum]"
    let &t_8b = "/<Esc>[48;2;%lu;%lu%lum]"
endif
let g:gruvbox_invert_selection='0'

colorscheme gruvbox
set background=dark
"set background=light

highlight Normal guibg=none

"-----------------------------------------------------------------------------
