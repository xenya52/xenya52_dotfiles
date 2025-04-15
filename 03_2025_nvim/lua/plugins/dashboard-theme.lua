return {
  {
    "goolord/alpha-nvim",
    opts = function(_, opts)
      local dashboard = require("alpha.themes.dashboard")

      -- WICHTIG: dashboard.layout muss erhalten bleiben!
      opts.layout = dashboard.config.layout
      opts.opts = dashboard.config.opts
      opts.section = dashboard.section

      return opts
    end,
  },
}
