import os
import subprocess
import time
import ipaddress
import map

class Command:
    def __init__(self, cmd, flags=[],target="", output=True):
      self.cmd = cmd
      self.flags = flags  
      self.target = target
      self.output = output

    def print_output(self, result):
        if result.returncode == 0:
            output = result.stdout.strip()
            print(self.cmd + " output:", output)
        else:
            print("Command failed with error:", result.stderr)

    def run_command(self):
        if not self.target:
            result = subprocess.run(self.cmd, shell=True, capture_output=True, text=True)
        else:
            full_cmd = self.cmd + " " + self.target
            result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
        if self.output:
            self.print_output(result)
        
    
def is_ip_address(word):
    try:
        ip = ipaddress.ip_address(word)
        return True
    except ValueError:
        return False

def get_ip_loc(filepath):
    ip_addresses = []
    with open(filepath) as f:
        for line in f.readlines():
            words = line.split()
            if len(words) > 0:
                last_word = words[-1]
                if is_ip_address(last_word):
                    ip_addresses.append(last_word)

    for ip in ip_addresses:
        location_ip = Command("curl", [],"ipinfo.io/" + ip + " | findstr loc >> output/locations.txt", False)
        location_ip.run_command()
#url = input("Please input url: ")
#ping = Command("ping",[],url)
#ping.run_command()

# user = Command("whoami")
# user.run_command()
ip_addr = Command("ipconfig | findstr IPv4")


#ip = input("Please input ip: ")

nslookup = "nslookup"
url = "google.com"
filepath = "output/output.txt"

###
# RUN TRACEROUTE COMMAND TO VIEW PATH TO SITE
###
# trace = Command("tracert -d ",[], url + " > output/output.txt", False)
# trace.run_command()

# WAIT FOR CMD TO COMPLETE
# time.sleep(3)

### RETRIEVE THE COORDINATES
# get_ip_loc(filepath)
time.sleep(1)

x, y = [], []
filepath = "output/locations.txt"
with open(filepath) as f:
    for line in f.readlines():
        words = line.split()
        if len(words) > 0:
            locs = words[-1]
            split_locs = locs.split(",")
            lat = split_locs[0].replace('"','')
            long = split_locs[1].replace('"','')
            x.append(float(lat))
            y.append(float(long))

map.map_locations(x,y)


        
# get_file_contents = open('hi.txt','r')
# print(get_file_contents.read())
#get_file_contents.run_command()
mac_addr = "getmac"
tasks = "tasklist | findstr chrome"
arp = "arp -a"
host = "hostname"
