return {
  -- Füge das Farbschema-Plugin hinzu
  { "nikolvs/vim-sunbather" },

  -- Konfiguriere LazyVim, um sunbather als colorscheme zu verwenden
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "sunbather",
    },
    config = function(_, opts)
      require("lazyvim").setup(opts)

      -- Überschreibe die Farben für Ordner und verschiedene Icons
      vim.cmd("highlight Directory guifg=#EDA3B1")
    end,
  },
}
