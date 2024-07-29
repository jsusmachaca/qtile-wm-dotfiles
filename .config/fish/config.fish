if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""


alias cat='bat'
alias ls='lsd'
alias tree='lsd --tree'
alias shutdown='shutdown now'
alias pnpx='pnpm dlx'
alias icat='kitten icat'

fastfetch

starship init fish | source

# pnpm
set -gx PNPM_HOME "/home/jsus/.local/share/pnpm"
if not string match -q -- $PNPM_HOME $PATH
  set -gx PATH "$PNPM_HOME" $PATH
end
# pnpm end
