import subprocess
def run_command(command):
    return str(subprocess.check_output(command, shell=True, universal_newlines=True))

perc = run_command("upower -i $(upower -e | grep 'BAT') | grep 'percentage'").split(' ')
percentage = int(perc[len(perc) - 1].strip().split('%')[0])

parts = run_command("upower -i $(upower -e | grep 'BAT') | grep 'state'").split(' ')
state = parts[len(parts) - 1].strip()

discharge = run_command("~/etc/polybar/scripts/wattage.sh").strip()

symbol = "";
if state == "discharging":
    if percentage >= 80:
        symbol = u'\uf240'
    elif percentage >= 60:
        symbol = u'\uf241'
    elif percentage >= 40:
        symbol = u'\uf242'
    elif percentage >= 20:
        symbol = u'\uf243'
    else:
        symbol = u'\uf244'
    print("(" + discharge + ") " + str(percentage) + "%  " + symbol)
else:
    symbol = u'\uf0e7'
    print(str(percentage) + "%  " + symbol)
