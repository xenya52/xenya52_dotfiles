local c = {
  bg = "#17171B",
  panel = "#1D1D22",
  raised = "#26262C",
  fg = "#EDA3B1",
  bright = "#F8D3DC",
  muted = "#AD8996",
  accent = "#D977A9",
  pink = "#F1A1CF",
  magenta = "#D78BDF",
  rose = "#F2B7A9",
  red = "#E77B87",
}
local function mode(color)
  return {
    a = { fg = c.bg, bg = color, gui = "bold" },
    b = { fg = c.bright, bg = c.raised },
    c = { fg = c.fg, bg = c.panel },
  }
end
return {
  normal = mode(c.accent),
  insert = mode(c.pink),
  visual = mode(c.magenta),
  replace = mode(c.red),
  command = mode(c.rose),
  terminal = mode(c.pink),
  inactive = {
    a = { fg = c.muted, bg = c.panel },
    b = { fg = c.muted, bg = c.panel },
    c = { fg = c.muted, bg = c.panel },
  },
}
