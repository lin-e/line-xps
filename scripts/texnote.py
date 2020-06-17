import os
import sys
from datetime import datetime

def suffix(d):
  if 11 <= d <= 13:
    return "th"
  return {1:'st',2:'nd',3:'rd'}.get(d % 10, 'th')

def custom_strftime(format, t):
  return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

directory = sys.argv[1]

cwd = os.path.dirname(os.path.realpath(__file__))
template = open(cwd + "/../ic/template.tex", "r").read()

ts = datetime.today().strftime('%Y%m%d')
module = os.path.basename(directory)
newdir = directory + "/" + ts + "_" + module

if not os.path.exists(newdir):
  os.mkdir(newdir)
  title = module.upper() + " - " + custom_strftime("%B {S} %Y", datetime.now())

  f = open(newdir + "/main.tex", "w")
  f.write(template.replace("$TITLE$", title))
  f.close()

print(newdir)
