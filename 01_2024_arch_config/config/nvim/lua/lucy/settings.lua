-- Show line numbers.
vim.wo.number = true

-- Use the system clipboard.
vim.o.clipboard = 'unnamedplus'


-- Restore the cursor position when reopening a file.
vim.api.nvim_command([[au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal! g`\"" | endif]])


-- Use four spaces for indentation by default.
vim.o.tabstop = 4
vim.o.softtabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true


-- Continue the current indentation.
vim.o.smartindent = true


-- Persist undo history.
vim.opt.undofile = true
