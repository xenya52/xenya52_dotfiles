return {
  'nvim-telescope/telescope.nvim', 
  tag = '0.1.6',
  dependencies = { 'nvim-lua/plenary.nvim' },
  config = function ()
    -- Use leader he for help tags.
    vim.keymap.set("n", "<leader>he", ":Telescope help_tags<CR>")

    -- Search in the current file (fi).
    vim.keymap.set("n", "<leader>fi", ":Telescope current_buffer_fuzzy_find<CR>")

    -- Find files (ff).
    vim.keymap.set("n", "<leader>ff", ":Telescope find_files<CR>")

    -- Search file contents with grep (fg).
    vim.keymap.set("n", "<leader>fg", ":Telescope live_grep<CR>")

    -- See the available pickers:
    -- https://github.com/nvim-telescope/telescope.nvim?tab=readme-ov-file#pickers
  end
}

