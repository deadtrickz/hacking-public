# Function to get the subnet mask as a string based on the prefix length
function Get-SubnetMask {
    param([int]$prefixLength)
    $mask = ""
    $remainingBits = $prefixLength
    for ($i = 0; $i -lt 4; $i++) {
        if ($remainingBits -ge 8) {
            $mask += "255"
            $remainingBits -= 8
        } elseif ($remainingBits -gt 0) {
            $octetValue = 256 - [math]::Pow(2, 8 - $remainingBits)
            $mask += "$octetValue"
            $remainingBits = 0
        } else {
            $mask += "0"
        }
        if ($i -lt 3) {
            $mask += "."
        }
    }
    return $mask
}

# Function to convert a 32-bit integer to an IP address
function Convert-IntToIPAddress {
    param([uint32]$int)
    $bytes = [System.BitConverter]::GetBytes([uint32]$int)
    [Array]::Reverse($bytes)
    return [System.Net.IPAddress]::new($bytes)
}

# Prompt the user for input
$input = Read-Host "Enter IP address with CIDR notation (e.g., 192.168.0.1/30)"
$ip, $cidr = $input -split '/'

# Trim any leading or trailing whitespace
$ip = $ip.Trim()
$cidr = $cidr.Trim()

# Validate the CIDR notation
$prefixLength = [int]$cidr
if ($prefixLength -lt 0 -or $prefixLength -gt 32) {
    Write-Host "Invalid CIDR prefix length. It should be between 0 and 32."
    exit
}

# Parse the IP address
try {
    $ipAddress = [System.Net.IPAddress]::Parse($ip)
} catch {
    Write-Host "Invalid IP address format."
    exit
}

# Get subnet mask as string and parse it
$subnetMaskString = Get-SubnetMask $prefixLength
$subnetMaskAddress = [System.Net.IPAddress]::Parse($subnetMaskString)
$subnetMaskBytes = $subnetMaskAddress.GetAddressBytes()
[Array]::Reverse($subnetMaskBytes)
$subnetMaskInt = [System.BitConverter]::ToUInt32($subnetMaskBytes, 0)

# Convert IP address to 32-bit integer
$ipBytes = $ipAddress.GetAddressBytes()
[Array]::Reverse($ipBytes)
$ipInt = [System.BitConverter]::ToUInt32($ipBytes, 0)

# Calculate the network ID and broadcast address
$networkInt = $ipInt -band $subnetMaskInt
$broadcastInt = $networkInt -bor (-bnot $subnetMaskInt)

# Convert calculated integers back to IP addresses
$networkAddress = Convert-IntToIPAddress $networkInt
$broadcastAddress = Convert-IntToIPAddress $broadcastInt

# Calculate the first and last usable IP addresses
$hostBits = 32 - $prefixLength
if ($hostBits -eq 0) {
    $firstUsableIP = $networkAddress
    $lastUsableIP = $networkAddress
} elseif ($hostBits -eq 1) {
    $firstUsableIP = $networkAddress
    $lastUsableIP = $broadcastAddress
} else {
    $firstUsableInt = $networkInt + 1
    $lastUsableInt = $broadcastInt - 1
    $firstUsableIP = Convert-IntToIPAddress $firstUsableInt
    $lastUsableIP = Convert-IntToIPAddress $lastUsableInt
}

# Calculate the number of hosts
if ($hostBits -eq 0) {
    $numberOfHosts = 1
} elseif ($hostBits -eq 1) {
    $numberOfHosts = 2
} else {
    $numberOfHosts = [math]::Pow(2, $hostBits) - 2
}

# Determine the default network prefix length based on the IP class
$firstOctet = [int]$ipAddress.GetAddressBytes()[0]
if ($firstOctet -ge 1 -and $firstOctet -le 126) {
    $defaultNetworkPrefixLength = 8    # Class A
} elseif ($firstOctet -ge 128 -and $firstOctet -le 191) {
    $defaultNetworkPrefixLength = 16   # Class B
} elseif ($firstOctet -ge 192 -and $firstOctet -le 223) {
    $defaultNetworkPrefixLength = 24   # Class C
} else {
    $defaultNetworkPrefixLength = $prefixLength  # Classes D and E
}

# Adjust the default network prefix length if the prefix length is less
if ($prefixLength -lt $defaultNetworkPrefixLength) {
    $defaultNetworkPrefixLength = $prefixLength
}

# Calculate the number of subnet bits
$n = $prefixLength - $defaultNetworkPrefixLength

# Calculate the number of subnets
$numberOfSubnets = [math]::Pow(2, $n)

# Display a warning if the IP address is in the loopback range
if ($firstOctet -eq 127) {
    Write-Host "Warning: IP addresses in the 127.0.0.0/8 range are reserved for loopback and are not routable."
}

# Display the results
Write-Host "Network ID: $($networkAddress)/$prefixLength"
Write-Host "First Usable IP: $($firstUsableIP)"
Write-Host "Last Usable IP: $($lastUsableIP)"
Write-Host "Broadcast Address: $($broadcastAddress)"
Write-Host "Number of Hosts: $numberOfHosts"
Write-Host "Number of Subnets: $numberOfSubnets"
Write-Host "Subnet Mask: $($subnetMaskAddress)"
