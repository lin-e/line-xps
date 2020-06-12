export ZSH="/home/line/.oh-my-zsh"

ZSH_THEME="agnoster-line"
DISABLE_AUTO_UPDATE="true"
TERM="xterm-256color"

plugins=(
  git
  web-search
  command-not-found
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh
source /etc/zsh_command_not_found

eval $(thefuck --alias)
if [ -f ~/etc/.aliases ]; then
    . ~/etc/.aliases
fi

if [[ -r /usr/local/lib/python2.7/site-packages/powerline/bindings/zsh/powerline.zsh ]]; then
  source /usr/local/lib/python2.7/site-packages/powerline/bindings/zsh/powerline.zsh
fi
