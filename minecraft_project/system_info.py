"""
System Information Gathering Module
Collects detailed information about the target system for reconnaissance
"""

import platform
import socket
import os
import psutil
import subprocess
from datetime import datetime
import json


class SystemInfo:
    """Gathers comprehensive system information from the target machine"""
    
    def __init__(self):
        self.info = {}
        
    def gather_all(self):
        """Collect all available system information"""
        self.info['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.info['basic'] = self.get_basic_info()
        self.info['network'] = self.get_network_info()
        self.info['hardware'] = self.get_hardware_info()
        self.info['software'] = self.get_software_info()
        self.info['user'] = self.get_user_info()
        self.info['security'] = self.get_security_info()
        return self.info
    
    def get_basic_info(self):
        """Get basic system information"""
        try:
            basic = {
                'hostname': socket.gethostname(),
                'platform': platform.system(),
                'platform_release': platform.release(),
                'platform_version': platform.version(),
                'architecture': platform.machine(),
                'processor': platform.processor(),
                'python_version': platform.python_version(),
            }
            return basic
        except Exception as e:
            return {'error': str(e)}
    
    def get_network_info(self):
        """Get network configuration and IP addresses"""
        try:
            network = {
                'hostname': socket.gethostname(),
                'fqdn': socket.getfqdn(),
            }
            
            # Get local IP address
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                network['local_ip'] = s.getsockname()[0]
                s.close()
            except:
                network['local_ip'] = 'Unable to determine'
            
            # Get all network interfaces
            try:
                interfaces = psutil.net_if_addrs()
                network['interfaces'] = {}
                for interface_name, interface_addresses in interfaces.items():
                    network['interfaces'][interface_name] = []
                    for address in interface_addresses:
                        if str(address.family) == 'AddressFamily.AF_INET':
                            network['interfaces'][interface_name].append({
                                'ip': address.address,
                                'netmask': address.netmask,
                                'broadcast': address.broadcast
                            })
            except:
                network['interfaces'] = 'Unable to determine'
            
            # Get MAC addresses
            try:
                network['mac_addresses'] = {}
                for interface_name, interface_addresses in psutil.net_if_addrs().items():
                    for address in interface_addresses:
                        if str(address.family) == 'AddressFamily.AF_LINK':
                            network['mac_addresses'][interface_name] = address.address
            except:
                network['mac_addresses'] = 'Unable to determine'
            
            return network
        except Exception as e:
            return {'error': str(e)}
    
    def get_hardware_info(self):
        """Get hardware specifications"""
        try:
            hardware = {}
            
            # CPU Information
            hardware['cpu'] = {
                'physical_cores': psutil.cpu_count(logical=False),
                'total_cores': psutil.cpu_count(logical=True),
                'max_frequency': f"{psutil.cpu_freq().max:.2f} MHz" if psutil.cpu_freq() else "N/A",
                'current_frequency': f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else "N/A",
                'cpu_usage': f"{psutil.cpu_percent(interval=1)}%"
            }
            
            # Memory Information
            memory = psutil.virtual_memory()
            hardware['memory'] = {
                'total': self.get_size(memory.total),
                'available': self.get_size(memory.available),
                'used': self.get_size(memory.used),
                'percentage': f"{memory.percent}%"
            }
            
            # Disk Information
            hardware['disks'] = []
            partitions = psutil.disk_partitions()
            for partition in partitions:
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                    hardware['disks'].append({
                        'device': partition.device,
                        'mountpoint': partition.mountpoint,
                        'filesystem': partition.fstype,
                        'total': self.get_size(partition_usage.total),
                        'used': self.get_size(partition_usage.used),
                        'free': self.get_size(partition_usage.free),
                        'percentage': f"{partition_usage.percent}%"
                    })
                except PermissionError:
                    continue
            
            # GPU Information (Windows only)
            if platform.system() == "Windows":
                try:
                    import wmi
                    computer = wmi.WMI()
                    gpu_info = []
                    for gpu in computer.Win32_VideoController():
                        gpu_info.append({
                            'name': gpu.Name,
                            'driver_version': gpu.DriverVersion,
                            'video_processor': gpu.VideoProcessor
                        })
                    hardware['gpu'] = gpu_info
                except:
                    hardware['gpu'] = 'Unable to determine'
            
            return hardware
        except Exception as e:
            return {'error': str(e)}
    
    def get_software_info(self):
        """Get installed software and OS details"""
        try:
            software = {
                'os': platform.system(),
                'os_version': platform.version(),
                'os_release': platform.release(),
            }
            
            # Boot time
            boot_time = datetime.fromtimestamp(psutil.boot_time())
            software['boot_time'] = boot_time.strftime("%Y-%m-%d %H:%M:%S")
            software['uptime'] = str(datetime.now() - boot_time).split('.')[0]
            
            # Running processes count
            software['running_processes'] = len(psutil.pids())
            
            # Windows-specific information
            if platform.system() == "Windows":
                try:
                    # Get Windows version details
                    import winreg
                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                        r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
                    software['windows_edition'] = winreg.QueryValueEx(key, "ProductName")[0]
                    software['windows_build'] = winreg.QueryValueEx(key, "CurrentBuild")[0]
                    winreg.CloseKey(key)
                except:
                    pass
                
                # Check for antivirus (Windows)
                software['antivirus'] = self.check_antivirus_windows()
            
            # Linux-specific information
            elif platform.system() == "Linux":
                try:
                    # Get distribution info
                    with open('/etc/os-release', 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                            if line.startswith('PRETTY_NAME'):
                                software['linux_distribution'] = line.split('=')[1].strip().strip('"')
                except:
                    pass
            
            return software
        except Exception as e:
            return {'error': str(e)}
    
    def get_user_info(self):
        """Get current user and session information"""
        try:
            user = {
                'username': os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USERNAME') or os.environ.get('USER'),
                'home_directory': os.path.expanduser('~'),
                'current_directory': os.getcwd(),
            }
            
            # Get environment variables (selected)
            user['environment'] = {
                'PATH': os.environ.get('PATH', 'N/A'),
                'TEMP': os.environ.get('TEMP', 'N/A'),
                'USERPROFILE': os.environ.get('USERPROFILE', 'N/A'),
                'COMPUTERNAME': os.environ.get('COMPUTERNAME', 'N/A'),
            }
            
            # Check if user has admin privileges
            user['is_admin'] = self.check_admin_privileges()
            
            return user
        except Exception as e:
            return {'error': str(e)}
    
    def get_security_info(self):
        """Get security-related information"""
        try:
            security = {}
            
            # Check if running in virtual machine
            security['is_vm'] = self.check_virtual_machine()
            
            # Check firewall status (Windows)
            if platform.system() == "Windows":
                security['firewall'] = self.check_firewall_windows()
            
            # Check for debugger
            security['debugger_present'] = self.check_debugger()
            
            return security
        except Exception as e:
            return {'error': str(e)}
    
    # Helper methods
    
    @staticmethod
    def get_size(bytes_size):
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    @staticmethod
    def check_admin_privileges():
        """Check if running with administrator/root privileges"""
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
    
    @staticmethod
    def check_virtual_machine():
        """Detect if running in a virtual machine"""
        try:
            # Check common VM indicators
            vm_indicators = [
                'vmware', 'virtualbox', 'qemu', 'xen', 'hyper-v', 'parallels'
            ]
            
            system_info = platform.platform().lower()
            processor_info = platform.processor().lower()
            
            for indicator in vm_indicators:
                if indicator in system_info or indicator in processor_info:
                    return True
            
            # Check for VM-specific files (Windows)
            if platform.system() == "Windows":
                vm_files = [
                    r'C:\windows\System32\Drivers\Vmmouse.sys',
                    r'C:\windows\System32\Drivers\vmhgfs.sys',
                    r'C:\windows\System32\Drivers\VBoxMouse.sys',
                    r'C:\windows\System32\Drivers\VBoxGuest.sys',
                ]
                for vm_file in vm_files:
                    if os.path.exists(vm_file):
                        return True
            
            return False
        except:
            return False
    
    @staticmethod
    def check_debugger():
        """Check if a debugger is attached"""
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.kernel32.IsDebuggerPresent() != 0
            else:
                # Linux: Check for TracerPid in /proc/self/status
                with open('/proc/self/status', 'r') as f:
                    for line in f:
                        if line.startswith('TracerPid:'):
                            return int(line.split(':')[1].strip()) != 0
            return False
        except:
            return False
    
    @staticmethod
    def check_antivirus_windows():
        """Check for installed antivirus (Windows only)"""
        try:
            if platform.system() != "Windows":
                return "N/A"
            
            import wmi
            computer = wmi.WMI()
            av_products = []
            
            # Query Windows Security Center
            for av in computer.query("SELECT * FROM AntiVirusProduct", namespace=r"root\SecurityCenter2"):
                av_products.append(av.displayName)
            
            return av_products if av_products else "None detected"
        except:
            return "Unable to determine"
    
    @staticmethod
    def check_firewall_windows():
        """Check Windows Firewall status"""
        try:
            if platform.system() != "Windows":
                return "N/A"
            
            result = subprocess.run(
                ['netsh', 'advfirewall', 'show', 'allprofiles', 'state'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if 'ON' in result.stdout:
                return "Enabled"
            elif 'OFF' in result.stdout:
                return "Disabled"
            else:
                return "Unknown"
        except:
            return "Unable to determine"
    
    def to_json(self):
        """Convert system info to JSON string"""
        return json.dumps(self.info, indent=4)
    
    def to_formatted_text(self):
        """Convert system info to formatted text"""
        output = []
        output.append("=" * 80)
        output.append("SYSTEM INFORMATION REPORT")
        output.append("=" * 80)
        output.append(f"Generated: {self.info.get('timestamp', 'N/A')}")
        output.append("")
        
        # Basic Information
        if 'basic' in self.info:
            output.append("-" * 80)
            output.append("BASIC INFORMATION")
            output.append("-" * 80)
            for key, value in self.info['basic'].items():
                output.append(f"{key.replace('_', ' ').title()}: {value}")
            output.append("")
        
        # Network Information
        if 'network' in self.info:
            output.append("-" * 80)
            output.append("NETWORK INFORMATION")
            output.append("-" * 80)
            network = self.info['network']
            output.append(f"Hostname: {network.get('hostname', 'N/A')}")
            output.append(f"FQDN: {network.get('fqdn', 'N/A')}")
            output.append(f"Local IP: {network.get('local_ip', 'N/A')}")
            output.append("")
        
        # Hardware Information
        if 'hardware' in self.info:
            output.append("-" * 80)
            output.append("HARDWARE INFORMATION")
            output.append("-" * 80)
            hardware = self.info['hardware']
            
            if 'cpu' in hardware:
                output.append("CPU:")
                for key, value in hardware['cpu'].items():
                    output.append(f"  {key.replace('_', ' ').title()}: {value}")
            
            if 'memory' in hardware:
                output.append("\nMemory:")
                for key, value in hardware['memory'].items():
                    output.append(f"  {key.title()}: {value}")
            output.append("")
        
        # User Information
        if 'user' in self.info:
            output.append("-" * 80)
            output.append("USER INFORMATION")
            output.append("-" * 80)
            user = self.info['user']
            output.append(f"Username: {user.get('username', 'N/A')}")
            output.append(f"Home Directory: {user.get('home_directory', 'N/A')}")
            output.append(f"Admin Privileges: {user.get('is_admin', 'N/A')}")
            output.append("")
        
        # Security Information
        if 'security' in self.info:
            output.append("-" * 80)
            output.append("SECURITY INFORMATION")
            output.append("-" * 80)
            for key, value in self.info['security'].items():
                output.append(f"{key.replace('_', ' ').title()}: {value}")
            output.append("")
        
        output.append("=" * 80)
        return "\n".join(output)
    
    def save_to_file(self, filename="system_info.txt", format="text"):
        """Save system information to file"""
        try:
            if format == "json":
                with open(filename, 'w') as f:
                    f.write(self.to_json())
            else:
                with open(filename, 'w') as f:
                    f.write(self.to_formatted_text())
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False


def main():
    """Main function to demonstrate system info gathering"""
    print("Gathering system information...")
    print()
    
    # Create system info object
    sys_info = SystemInfo()
    
    # Gather all information
    sys_info.gather_all()
    
    # Display formatted output
    print(sys_info.to_formatted_text())
    
    # Save to files
    sys_info.save_to_file("system_info.txt", format="text")
    sys_info.save_to_file("system_info.json", format="json")
    
    print("\nSystem information saved to:")
    print("  - system_info.txt (formatted text)")
    print("  - system_info.json (JSON format)")


if __name__ == "__main__":
    main()
