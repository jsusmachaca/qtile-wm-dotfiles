local cmp = require("cmp")

require("mason").setup()
require('mason-lspconfig').setup({
  ensure_installed = {
    "rust_analyzer",
    "zls",
    "gopls",
    "ts_ls",
    "pyright",
    "lua_ls",
    "docker_compose_language_service",
    "dockerls",
    "html",
    "cssls",
    "tailwindcss",
    "bashls",
    "yamlls",
    "sqls",
  }
})

local function on_attach(_, bufnr)
  vim.api.nvim_create_user_command("ToggleInlineDiagnostics", function()
    local config = vim.diagnostic.config()
    vim.diagnostic.config {
      virtual_text = not config.virtual_text,
    }
  end, {})

  vim.keymap.set("n", "<leader>lr", vim.lsp.buf.rename, { buffer = bufnr })
  vim.keymap.set("n", "<leader>lf", vim.lsp.buf.format, { buffer = bufnr })
  vim.keymap.set('n', '<leader>ld', vim.diagnostic.open_float, { buffer = bufnr })
  vim.keymap.set('n', '<leader>lt', vim.cmd.ToggleInlineDiagnostics, { buffer = bufnr })
  vim.keymap.set("n", "gd", vim.lsp.buf.definition, { buffer = bufnr })
  vim.keymap.set("n", "gr", vim.lsp.buf.references, { buffer = bufnr })

  local signs = {
    Error = "",
    Warn = "",
    Hint = "󰌶",
  }

  vim.diagnostic.config({
    virtual_text = true,
    signs = {
      text = {
        [vim.diagnostic.severity.ERROR] = signs.Error,
        [vim.diagnostic.severity.WARN] = signs.Warn,
        [vim.diagnostic.severity.HINT] = signs.Hint,
      }
    }
  })
end

vim.lsp.config("lua_ls", {
  on_attach = on_attach,
  settings = {
    Lua = {
      diagnostics = { globals = { "vim" } },
    }
  }
})

vim.lsp.config("gopls", {
  on_attach = on_attach,
  settings = {
    gopls = {
      semanticTokens = true,
      staticcheck = true,
      gofumpt = true,
    }
  },
})

vim.api.nvim_create_autocmd("LspAttach", {
  callback = function(args)
    local client = vim.lsp.get_client_by_id(args.data.client_id)
    if client then
      on_attach(client, args.buf)
    end
  end,
})

local select_behavior = { behavior = cmp.SelectBehavior.Select }

cmp.setup({
  mapping = {
    ["<CR>"] = cmp.mapping.confirm({ select = false }),
    ["<TAB>"] = cmp.mapping.select_next_item(select_behavior),
    ["<S-TAB>"] = cmp.mapping.select_prev_item(select_behavior),
  }
})
