#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

alias wlanup='sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf' #U dont need that

hyfetch --ascii-file <(pokemon-colorscripts -n sylveon --no-title)
#hyfetch --ascii-file ~/ImagesAndVideos/neofetchAscii
. "$HOME/.cargo/env" #U dont need that

##-----------------------------------------------------
## synth-shell-prompt.sh
if [ -f /home/xenya/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source /home/xenya/.config/synth-shell/synth-shell-prompt.sh
fi
