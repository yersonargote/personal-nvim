"-----------------------------------------------------------------------------
" ALE

" Use virtual text
let g:ale_virtualtext_cursor=1

" No errors in ariline
" let g:airline#extensions#ale#enabled=1

" Use ALE with COC
let g:ale_display_lsp=1

let g:ale_linters = {
   \'python':['pylint', 'flake8']
   \}

let g:ale_fixers = {
   \'python':['autopep8', 'yapf'],
   \'javascript':['prettier', 'eslint'],
   \'typescript':['prettier'],
   \'css':['prettier', 'eslint']
   \}
let g:ale_fix_on_save=1
" Press F10 to fix
nmap <F10> :ALEFix<CR>

" How navigate between errors
nmap <silent> <C-k> <Plug>(ale_previous_wrap)
nmap <silent> <C-j> <Plug>(ale_next_wrap)
