#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias tree='tree -C'
alias ls='lsd'
alias cat='bat'
alias vim='nvim'
alias shutdown='shutdown now'
# alias xsel='xsel -ib <'
alias chmod='chmod -v'
alias rmd='rm -rf'
alias hdmi='xrandr --output eDP-1 --mode 1920x1080 --output HDMI-1 --mode 1920x1080 --same-as eDP-1;'

neofetch

# source ~/.scripts/bash-prompt.sh
source ~/.scripts/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1


function colors() {
  black="\e[30m"
  red="\e[31m"
  green="\e[32m"
  yelow="\e[33m"
  blue="\e[34m"
  magenta="\e[35m"
  cyan="\e[36m"
  lgray="\e[37m"
  gray="\e[90m"
  lred="\e[91m"
  lgreen="\e[92m"
  lyelow="\e[93m"
  lblue="\e[94m"
  lmagenta="\e[95m"
  lcyan="\e[96m"
  white="\e[97m"
  end="\e[0m"
}

function bg() {
  black="\e[40m"
  red="\e[41m"
  green="\e[42m"
  yelow="\e[43m"
  blue="\e[44m"
  magenta="\e[45m"
  cyan="\e[46m"
  lgray="\e[47m"
  gray="\e[100m"
  lred="\e[101m"
  lgreen="\e[102m"
  lyelow="\e[103m"
  lblue="\e[104m"
  lmagenta="\e[105m"
  lcyan="\e[106m"
  white="\e[107m"
  end="\e[0m"
}


function set_virtualenv () {
  if test -z "$VIRTUAL_ENV" ; then
      PYTHON_VIRTUALENV=""
  else
      PYTHON_VIRTUALENV=" |  `basename \"$VIRTUAL_ENV\"`"
  fi
}

function set_bash_prompt () {
  set_virtualenv

  PS1='┌─[\[\e[38;5;221m\]\u\[\e[0m\]   \[\e[38;5;39m\]\h \[\e[0m\]| \[\e[38;5;30m\]\W\[\e[0m\]${PYTHON_VIRTUALENV}\[\e[0m\]] \[\033[33m\]$(__git_ps1 "  %s") \n└──\[\e[38;5;159;1m\] '

}

PROMPT_COMMAND=set_bash_prompt


###########
# PS1='\[\e[0;38;5;221m\]\u\[\e[0;38;5;159m\]@\[\e[0;38;5;105m\]\H\[\e[0m\]:\[\e[0;38;5;30m\]\W \[\033[33m\]$(__git_ps1 " %s ")\[\e[0;1;38;5;159m\] \[\e[0m\]'

# PS1='┌─[\[\e[38;5;221m\]\u\[\e[0m\]  \[\e[38;5;39m\]\h \[\e[0m\]| \[\e[38;5;30m\]\W\[\e[0m\]] \[\033[33m\]$(__git_ps1 "  %s") \n└──\[\e[38;5;159;1m\] \[\e[0m\]'

#PS1='┌─[\[\e[38;5;221m\]\u\[\e[0m\]  \[\e[38;5;39m\]\h \[\e[0m\]| \[\e[38;5;30m\]\W\[\e[0m\]] \[\033[33m\]$(__git_ps1 "  %s") \n└──\[\e[38;5;159;1m\] '
# PS1='┌─[\[\e[38;5;221m\]\u\[\e[0m\]   \[\e[38;5;39m\]\h \[\e[0m\]| \[\e[38;5;30m\]\W\[\e[0m\]] \[\033[33m\]$(__git_ps1 "  %s") \n└──\[\e[38;5;159;1m\] '

###########



if [ -f /usr/share/bash-completion/bash_completion ]; then
	. /usr/share/bash-completion/bash_completion
fi
