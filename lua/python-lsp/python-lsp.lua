-- npm i -g pyright

-- require'lspconfig'.pyright.setup{ on_attach=require'completion'.on_attach }
require'lspconfig'.pyright.setup {
    cmd = {"/home/lexson/.local/share/nvim/lspinstall/python/node_modules/.bin/pyright-langserver", "--stdio"},
    on_attach = require'completion'.on_attach,
}
--[[
require'lspconfig'.pyright.setup{
    cmd = { "pyright-langserver", "--stdio" },
    on_attach = require'compe'.on_attach
}
]]--
