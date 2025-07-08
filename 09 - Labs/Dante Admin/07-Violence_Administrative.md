# Violence

##### Create the vulnerable Service
```
nano /usr/local/bin/killer.sh
```
```
#!/bin/bash
ps -eo pid,ppid,cmd | grep '[s]shd: ' | grep -v 'priv' | awk '{print $1}' | xargs -r kill -9
```
```
*/5 * * * * /usr/local/bin/killer.sh
```
```
root passwd
never_gonna_give_you_up
```