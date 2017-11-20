import subprocess

child = subprocess.Popen(['pgrep','othello'], stdout=subprocess.PIPE, shell=True)
enemyPID = child.communicate()[0]

