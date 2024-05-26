### Map A Route

This application takes a URL and shows the hops on a map using python

![woohoo](https://github.com/sofjones/learning/assets/43796114/293b411b-a46f-4f2f-9207-3b2b56335b74)

#### trace route
First we have a user input the URL
We trace the route to the URL entered 
We output all the IPs to `output/output.txt`

##### mapping coordinates
From there to get the location of the hops the command `curl ipinfo.io/$ip` is run
this gets the coordinates of each ip address
the coordinates are saved to `output/locations.txt`
each location is then mapped using `folium`

#### Windows commands to list files (non powershell)

- `ls` is `dir`
- `cd`
- `pwd` is `cd`
- `clear` is `cls`
- `echo`
- `nc`
- `tnc`
- `top` `get-process`
#### Network commands

- `arp`
- `tracert`
- `ping`
- `whois`
#### `netstat`
 - `netstat -r`: shows routing table
 - `netstat -a`: shows all connections

#### Powershell commands

`ls`

#### Get an IP address windows

`ipconfig | Select-String IPv4 `

#### Permissions

- `chmod`

#### Web commands

`curl`

#### `Get-Process`
- `get-process`

##### flags
- `-name`
- `-id`


#### `Get-EventLog`

- `-list`: list all logs
- `-logname`: specify event log
- `-newest`: get the newest logs, requires a specific log
- `-message *word*` gets a specific word

###### log types
- `-entry-type error `
- example `get-eventlog -logname application -entry-type error -newest 10 | format-list`


#### making a map of tracert
if we saved all the ip hops from tracert
we could get the location of each of the ips from `curl ipinfo.io/<ip>`

* when we have the loc `x, y` then we could potentially map the route 
* ipv4 or ipv6 works fine
