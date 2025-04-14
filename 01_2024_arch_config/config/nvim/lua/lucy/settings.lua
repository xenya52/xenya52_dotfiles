-- Zeilennummern
vim.wo.number = true

-- System-Clipboard verwenden
vim.o.clipboard = 'unnamedplus'


-- Beim Wiederöffnen einer Datei zur letzten Position springen
vim.api.nvim_command([[au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal! g`\"" | endif]])


-- Einrückung mit 4 Spaces als Standard
vim.o.tabstop = 4
vim.o.softtabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true


-- Aktuelle Einrückung fortführen
vim.o.smartindent = true


-- Undo-Historie abspeichern
vim.opt.undofile = true
