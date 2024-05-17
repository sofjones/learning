import os
import subprocess
print("you are: ")
os.system("whoami")

command = "dir /b"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
if result.returncode == 0:
    output = result.stdout.strip()
    print("Command output:", output[0:20])
else:
    print("Command failed with error:", result.stderr)
