import re
import subprocess

def run_command(command):
    return str(subprocess.check_output(command, shell=True, universal_newlines=True))

def displays():
    connected_r = r"(.*?) connected"
    res_r = r"(\d+x\d+)"
    hz_r = "(\d+\.\d+)"

    out = run_command("xrandr").split("\n")
    results = []

    check = False
    current_display = ""

    for line in out:
        if not check:
            res = re.search(connected_r, line)
            if res:
                current_display = res.group(1)
                check = True
        else:
            res = re.search(res_r, line).group(1)

            results.append({
                "name": current_display,
                "resolution": res,
                "refresh_rates": re.findall(hz_r, line)
            })
            check = False

    return results

def generate_xrandr(monitor, mapping):
    cmd = f'xrandr --output {mapping[monitor["name"]]}'
    if monitor["enabled"]:
        cmd += f' --auto --mode {monitor["resolution"]} --rate {monitor["refresh_rate"]}'
        if monitor["primary"]:
            cmd += ' --primary'
        for (d, m) in monitor["positioning"]:
            cmd += f' --{d} {mapping[m]}'
    else:
        cmd += ' --off'

    return cmd

def generate_bspc(monitor, mapping):
    return f'bspc monitor {mapping[monitor["name"]]} -d {" ".join(monitor["workspaces"])}'

def match(rule, xrandr):
    return rule["resolution"] == xrandr["resolution"] and rule["refresh_rate"] in xrandr["refresh_rates"]

def try_match(monitors, available):
    used = []
    mapping = {}
    for monitor in monitors:
        matched = False
        for xrandr in available:
            if xrandr["name"] in used:
                continue
            if match(monitor, xrandr):
                mapping[monitor["name"]] = xrandr["name"]
                matched = True
                used.append(xrandr["name"])
        if not matched:
            return (False, {})
    return (True, mapping)

# try each of these rules in order, first match is applied
rules = [
    {
        "name": "Dual HDMI Dock",
        "monitors": [
            {
                "name": "34gk950f",
                "resolution": "3440x1440",
                "refresh_rate": "59.97",
                "primary": True,
                "enabled": True,
                "workspaces": list(map(str, range(7, 13))),
                "positioning": []
            },
            {
                "name": "27gn88a",
                "resolution": "2560x1440",
                "refresh_rate": "99.95",
                "primary": False,
                "enabled": True,
                "workspaces": list(map(str, range(1, 7))),
                "positioning": [
                    ("left-of", "34gk950f")
                ]
            },
            {
                "name": "internal",
                "resolution": "1920x1200",
                "refresh_rate": "59.95",
                "primary": False,
                "enabled": False,
                "workspaces": [],
                "positioning": []
            },
        ]
    },
    {
        "name": "Ultrawide Only",
        "monitors": [
            {
                "name": "34gk950f",
                "resolution": "3440x1440",
                "refresh_rate": "59.97",
                "primary": True,
                "enabled": True,
                "workspaces": list(map(str, range(1, 13))),
                "positioning": []
            },
            {
                "name": "internal",
                "resolution": "1920x1200",
                "refresh_rate": "59.95",
                "primary": False,
                "enabled": False,
                "workspaces": [],
                "positioning": []
            },
        ]
    },
    {
        "name": "Default",
        "monitors": [
            {
                "name": "internal",
                "resolution": "1920x1200",
                "refresh_rate": "59.95",
                "primary": True,
                "enabled": True,
                "workspaces": list(map(str, range(1, 13))),
                "positioning": []
            },
        ]
    }
]

available = displays()

for rule in rules:
    print(f'Attempting "{rule["name"]}"')
    (success, mapping) = try_match(rule["monitors"], available)
    if success:
        print(f'Match success!')
        for (k, v) in mapping.items():
            print(f'  {k} -> {v}')
        for monitor in rule["monitors"]:
            cmd = generate_xrandr(monitor, mapping)
            print(f'Running "{cmd}"')
            run_command(cmd)
        for monitor in rule["monitors"]:
            if not monitor["enabled"]:
                continue
            cmd = generate_bspc(monitor, mapping)
            print(f'Running "{cmd}"')
            run_command(cmd)
        break
    else:
        print(f'Match failed!')