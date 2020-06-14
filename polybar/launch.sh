#!/bin/sh
killall -q polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 60; done

monitors=$(xrandr -q | grep " connected" | cut -d ' ' -f1)
IFS='\n'

echo $monitors | while IFS= read -r line; do
  MONITOR=$line polybar top &
done
