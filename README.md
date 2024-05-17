### Shell Explorer

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

