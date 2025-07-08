# Salvation (Metasploitable2)

##### Networking
```
sudo nano /etc/network/interfaces
```
```
auto eth1
iface eth1 inet static
address 72.69.76.2
netmask 255.255.255.0
gateway 72.69.76.1
```
![[Pasted image 20250604084525.png]]
```
sudo /etc/init.d/networking restart
```

##### Lan Segments
```
Network Adapter: LAN (DISABLED)
Network Adapter 2: 09-TREACHERY
```
![[Pasted image 20250604084838.png]]