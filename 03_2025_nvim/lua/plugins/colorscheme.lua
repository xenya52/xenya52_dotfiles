return {
  -- Füge das Farbschema-Plugin hinzu
  { "nikolvs/vim-sunbather" },

  -- Konfiguriere LazyVim, um sunbather als colorscheme zu verwenden
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "sunbather",
    },
  },
}
