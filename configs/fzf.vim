" fzf configure

let g:fzf_layout = {'window': { 'width': 0.8, 'height': 0.8 }}

nnoremap <silent> <leader>b :Buffers<CR>
nnoremap <C-p> :GFiles<CR>
nnoremap <leader>p :Files<CR>
nnoremap <silent> <leader>fm :Marks<CR>
nnoremap <silent> <leader>rt :VimRTP<CR>
let $FZF_DEFAULT_OPTS = '--reverse'
