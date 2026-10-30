return {
  {
    "goolord/alpha-nvim",
    opts = function(_, opts)
      local dashboard = require("alpha.themes.dashboard")

      -- Keep dashboard.layout intact.
      opts.layout = dashboard.config.layout
      opts.opts = dashboard.config.opts
      opts.section = dashboard.section

      return opts
    end,
  },
}
