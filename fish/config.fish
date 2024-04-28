if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting ""


alias cat='bat'
alias ls='lsd'
alias shutdown='shutdown now'



starship init fish | source

# pnpm
set -gx PNPM_HOME "/home/jsus/.local/share/pnpm"
if not string match -q -- $PNPM_HOME $PATH
  set -gx PATH "$PNPM_HOME" $PATH
end
# pnpm end
