vim.g.mapleader = " "

-- Toggle Nvim Tree
vim.keymap.set("n", "<C-n>", vim.cmd.NvimTreeToggle)

-- Save with CTRL S
vim.keymap.set("n", "<C-s>", ":w<CR>")
vim.keymap.set("i", "<C-s>", "<Esc>:w<CR>")

vim.keymap.set("n", "<C-q>", ":qa<CR>")
vim.keymap.set("i", "<C-q>", "<Esc>:q<CR>")

