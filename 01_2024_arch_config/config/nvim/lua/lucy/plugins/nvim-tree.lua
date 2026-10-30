return {
  'kyazdani42/nvim-tree.lua',
  dependencies = {
     -- Add file icons.
    'kyazdani42/nvim-web-devicons',
  },
  config = function()
    require('nvim-tree').setup({
      view = {
        width = 40,
      },
    })

    -- Use sf to toggle the file tree.
    vim.keymap.set("n", "<leader>sf", ":NvimTreeToggle<CR>")

    -- Jump to the current file, then center the view (zz).
    vim.keymap.set("n", "<leader>jf", ":NvimTreeFindFile<CR>zz")
  end
}

