# Abusing Weak File Permissions

**gtfobins.github.io**

### Finding Files with SUID Bit Set
```
find / -perm -4000 2>/dev/null
```
```
find / -perm -u=s -type f 2>/dev/null
```

