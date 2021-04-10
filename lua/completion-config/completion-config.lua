-- vim.cmd('set completeopt=menuone, noinsert, noselect')
-- vim.cmd("let g.completion_matching_strategy_list = ['extact', 'substring', 'fuzzy']")

require'lspconfig'.pyrigth.setup{ 
    cmd = { "pyright-langserver", "--stdio" },
    on_attach=require'completion'.on_attach }
