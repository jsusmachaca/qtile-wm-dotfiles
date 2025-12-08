vim.defer_fn(function()
  -- vim.cmd("NvimTreeOpen")
end, 100)

local function set_tabstop_based_on_extension()
  local filename = vim.api.nvim_buf_get_name(0)
  local ext = filename:match("^.+%.([^%.]+)$")

  local settings = {
    go = { expandtab = false, tabstop = 4, softtabstop = 4, shiftwidth = 4 },
    lua = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    js = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    ts = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    json = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    tsx = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    jsx = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    yaml = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    yml = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    html = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
    css = { expandtab = true, tabstop = 2, softtabstop = 2, shiftwidth = 2 },
  }

  local config = settings[ext] or { expandtab = true, tabstop = 4, softtabstop = 4, shiftwidth = 4 }
  vim.opt.expandtab = config.expandtab
  vim.opt.tabstop = config.tabstop
  vim.opt.softtabstop = config.softtabstop
  vim.opt.shiftwidth = config.shiftwidth
end

vim.api.nvim_create_autocmd("BufReadPost", {
  pattern = "*",
  callback = function()
    set_tabstop_based_on_extension()
  end,
})
