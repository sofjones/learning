import os
import subprocess
print("you are: ")
os.system("whoami")

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        output = result.stdout.strip()
        print("Command output:", output)
    else:
        print("Command failed with error:", result.stderr)


run_command("dir")