# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="/home/line/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
ZLE_RPROMPT_INDENT=0
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

if [ -f ~/etc/zsh/.aliases ]; then
    . ~/etc/zsh/.aliases
fi

if [[ -r /usr/local/lib/python2.7/site-packages/powerline/bindings/zsh/powerline.zsh ]]; then
  source /usr/local/lib/python2.7/site-packages/powerline/bindings/zsh/powerline.zsh
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
