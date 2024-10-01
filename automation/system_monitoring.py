import psutil
from datetime import datetime

def check_disk_space():
    """Checks the disk space usage."""
    disk_usage = psutil.disk_usage('C:/')
    # print(f"Total: {disk_usage.total / (1024 ** 3):.2f} GB")
    # print(f"Used: {disk_usage.used / (1024 ** 3):.2f} GB")
    # print(f"Free: {disk_usage.free / (1024 ** 3):.2f} GB")
    # print(f"Percentage: {disk_usage.percent}%")
    return {
        "Disk Size" : f"{disk_usage.total / (1024 ** 3):.2f} GB",
        "Disk Used" : f"{disk_usage.used / (1024 ** 3):.2f}GB",
        "Disk Free" : f"{disk_usage.free / (1024 ** 3):.2f} GB",
        "Disk Percentage" : f'{disk_usage.percent} %'
    }

def check_system_uptime():
    uptime_in_seconds = psutil.boot_time()
    uptime = datetime.now() - datetime.fromtimestamp(uptime_in_seconds)
    return uptime

def check_system_health():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Memory usage
    memory_info = psutil.virtual_memory()
    
    # Disk usage
    disk_usage = psutil.disk_usage('D:/')
    
    return {
        'cpu_usage': f'{cpu_usage}%',
        'memory_usage': f'{memory_info.percent}%',
        'disk_usage': f'{disk_usage.percent}%'
    }

if __name__ == "__main__":
    check_disk_space()
    check_system_health()