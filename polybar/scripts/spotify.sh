#!/bin/bash
title=$(playerctl metadata xesam:title 2>/dev/null)
artist=$(playerctl metadata xesam:artist 2>/dev/null)
if [ -z "$title" ] && [ -z "$artist" ];
then
  echo ""
else
  echo "$title - $artist"
fi
