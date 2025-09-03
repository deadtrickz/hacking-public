# Fixed reg_set code for havoc
```
#include <windows.h>
#include "beacon.h"
#include "bofdefs.h"
#include "base.c"

DWORD set_regkey(const char * hostname, HKEY hive, const char * path, const char * key, DWORD type, const BYTE * data, DWORD datalen)
{
    DWORD dwresult = ERROR_SUCCESS;
    HKEY rootkey = NULL;
    HKEY RemoteKey = NULL;
    HKEY targetkey = NULL;

    // Open local or remote hive
    if (hostname == NULL)
    {
        dwresult = ADVAPI32$RegOpenKeyExA(
            hive,
            NULL,
            0,
            KEY_WRITE | KEY_SET_VALUE | KEY_WOW64_64KEY,
            &rootkey
        );
        if (ERROR_SUCCESS != dwresult)
        {
            internal_printf("RegOpenKeyExA failed (%lX)\n", dwresult);
            goto set_regkey_end;
        }
    }
    else
    {
        dwresult = ADVAPI32$RegConnectRegistryA(hostname, hive, &RemoteKey);
        if (ERROR_SUCCESS != dwresult)
        {
            internal_printf("RegConnectRegistryA failed (%lX)\n", dwresult);
            goto set_regkey_end;
        }

        dwresult = ADVAPI32$RegOpenKeyExA(
            RemoteKey,
            NULL,
            0,
            KEY_WRITE | KEY_SET_VALUE | KEY_WOW64_64KEY,
            &rootkey
        );
        if (ERROR_SUCCESS != dwresult)
        {
            internal_printf("RegOpenKeyExA2 failed (%lX)\n", dwresult);
            goto set_regkey_end;
        }
    }

    // Create or open the target key
    dwresult = ADVAPI32$RegCreateKeyExA(
        rootkey,
        path,
        0,
        NULL,
        0,
        KEY_WRITE | KEY_SET_VALUE | KEY_WOW64_64KEY,
        NULL,
        &targetkey,
        NULL
    );
    if (ERROR_SUCCESS != dwresult)
    {
        internal_printf("RegCreateKeyExA failed (%lX)\n", dwresult);
        goto set_regkey_end;
    }

    // Set the value
    dwresult = ADVAPI32$RegSetValueExA(targetkey, key, 0, type, data, datalen);
    if (ERROR_SUCCESS != dwresult)
    {
        internal_printf("RegSetValueExA failed (%lX)\n", dwresult);
        goto set_regkey_end;
    }

    internal_printf("Successfully set registry key\n");

set_regkey_end:
    if (RemoteKey)
    {
        ADVAPI32$RegCloseKey(RemoteKey);
        rootkey = NULL;
    }

    if (rootkey)
    {
        ADVAPI32$RegCloseKey(rootkey);
        rootkey = NULL;
    }

    if (targetkey)
    {
        ADVAPI32$RegCloseKey(targetkey);
        targetkey = NULL;
    }

    return dwresult;
}

#ifdef BOF
VOID go(
    IN PCHAR Buffer,
    IN ULONG Length
)
{
    DWORD dwErrorCode = ERROR_SUCCESS;
    datap parser = {0};
    const char * hostname = NULL;
    HKEY hive = (HKEY)0x80000000;
    const char * path = NULL;
    const char * key = NULL;
    DWORD type = 0;
    const void * data = NULL;
    DWORD datalen = 0;
    int t = 0;

    BeaconDataParse(&parser, Buffer, Length);
    hostname = BeaconDataExtract(&parser, NULL);
    t = BeaconDataInt(&parser);
#pragma GCC diagnostic ignored "-Wint-to-pointer-cast"
#pragma GCC diagnostic ignored "-Wpointer-to-int-cast"
    hive = (HKEY)((DWORD)hive + (DWORD)t);
#pragma GCC diagnostic pop
    path = BeaconDataExtract(&parser, NULL);
    key = BeaconDataExtract(&parser, NULL);
    type = BeaconDataInt(&parser);

    // Correct hostname param
    if (*hostname == 0)
        hostname = NULL;

    // Use BeaconDataInt directly for DWORD/QWORD
    static DWORD dval;
    static ULONGLONG qval;
    if (type == REG_DWORD)
    {
        dval = (DWORD)BeaconDataInt(&parser);
        data = &dval;
        datalen = sizeof(DWORD);
    }
    else if (type == REG_QWORD)
    {
        qval = (ULONGLONG)BeaconDataInt(&parser);
        data = &qval;
        datalen = sizeof(ULONGLONG);
    }
    else
    {
        data = BeaconDataExtract(&parser, (int *)&datalen);
    }

    if (!bofstart())
        return;

    internal_printf("Setting registry key %s\\%p\\%s\\%s with type %d\n",
                    ((hostname == NULL) ? "\\\\." : hostname),
                    hive, path, key, type);

    dwErrorCode = set_regkey(hostname, hive, path, key, type, data, datalen);
    if (ERROR_SUCCESS != dwErrorCode)
    {
        BeaconPrintf(CALLBACK_ERROR, "set_regkey failed: %lX\n", dwErrorCode);
        goto go_end;
    }

    internal_printf("SUCCESS.\n");

go_end:
    printoutput(TRUE);
    bofstop();
};
#else
#define TEST_HOSTNAME ""
#define TEST_REG_HIVE HKEY_CURRENT_USER
#define TEST_REG_PATH "Uninstall"
#define TEST_REG_VALUE "BOF_TEST"
#define TEST_REG_TYPE REG_DWORD
int main(int argc, char **argv)
{
    DWORD dwErrorCode = ERROR_SUCCESS;
    LPCSTR lpszHostName = TEST_HOSTNAME;
    HKEY hkRootKey = TEST_REG_HIVE;
    LPCSTR lpszRegPathName = TEST_REG_PATH;
    LPCSTR lpszRegValueName = TEST_REG_VALUE;
    DWORD dwType = TEST_REG_TYPE;
    DWORD dwRegData = 1;
    DWORD dwRegDataLength = sizeof(DWORD);

    if (*lpszHostName == 0)
        lpszHostName = NULL;

    internal_printf("Setting registry key %s\\%p\\%s\\%s with type %lu\n",
                    ((lpszHostName == NULL) ? "\\\\." : lpszHostName),
                    hkRootKey, lpszRegPathName, lpszRegValueName, dwType);

    dwErrorCode = set_regkey(
        lpszHostName,
        hkRootKey,
        lpszRegPathName,
        lpszRegValueName,
        dwType,
        (LPBYTE)(&dwRegData),
        dwRegDataLength
    );
    if (ERROR_SUCCESS != dwErrorCode)
    {
        BeaconPrintf(CALLBACK_ERROR, "set_regkey failed: %lX\n", dwErrorCode);
        goto main_end;
    }

    internal_printf("SUCCESS.\n");

main_end:
    return dwErrorCode;
}
#endif
```
