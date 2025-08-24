# Havoc Basic Usage

## Server
```
havoc server --profile /usr/share/havoc/profiles/havoc.yaotl
```
![](../../zzAttachments/Pasted%20image%2020250820084842.png)

##### Example havoc.yaotl
```
Teamserver {
    Host = "127.0.0.1"
    Port = 40056

    Build {
        Compiler64 = "/usr/bin/x86_64-w64-mingw32-cross/bin/x86_64-w64-mingw32-gcc"
        Compiler86 = "/usr/bin/x86_64-w64-mingw32-cross/bin/x86_64-w64-mingw32-gcc"
        Nasm = "/usr/bin/nasm"
    }
}

Operators {
    user "BoB" {
        Password = "theBuild3r"
    }
}

# this is optional. if you dont use it you can remove it.
Service {
    Endpoint = "service-endpoint"
    Password = "service-password"
}

Demon {
    Sleep = 2
    Jitter = 15

    TrustXForwardedFor = false

    Injection {
        Spawn64 = "C:\\Windows\\System32\\notepad.exe"
        Spawn32 = "C:\\Windows\\SysWOW64\\notepad.exe"
    }
}
```

## Client
```
havoc client
```
![](../../zzAttachments/Pasted%20image%2020250820084750.png)
