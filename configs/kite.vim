" Kite
" Python, JavaScript
let g:kite_supported_languages=['javascript', 'python']

" Turn off Kite
"let g:kite_supported_languages = []

" Use <c-space> to trigger the completion
if &filetype == "javascript" || &filetype == "python"
    inoremap <c-space> <C-x><C-u>
endif

" Use tab to completion
let g:kite_tab_complete=1
