#!/bin/sh
killall -q polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 60; done
MONITOR=eDP-1 polybar top &
