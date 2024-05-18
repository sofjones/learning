import os
import subprocess

class Command:
    def __init__(self, cmd, flags=[],target=""):
      self.cmd = cmd
      self.flags = flags  
      self.target = target

    def run_command(self):
        if not self.target:
            print(self.cmd)
            result = subprocess.run(self.cmd, shell=True, capture_output=True, text=True)
        else:
            full_cmd = self.cmd + " " + self.target
            result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
            print("Command output:", output)
        else:
            print("Command failed with error:", result.stderr)
print("you are: ")
os.system("whoami")



url = input("please input url")
opts = "would you like to ping google?"
ping = Command("ping",[],url)
ping.run_command()


ip_addr = "ipconfig | findstr IPv4"
nslookup = "nslookup"
trace = "tracert -d " + url
mac_addr = "getmac"
tasks = "tasklist | findstr chrome"
arp = "arp -a"
host = "hostname"
