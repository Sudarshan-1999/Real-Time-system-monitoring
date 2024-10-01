import psutil
import json
from datetime import datetime
def check_system_uptime():
    uptime_in_seconds = psutil.boot_time()
    uptime = datetime.now() - datetime.fromtimestamp(uptime_in_seconds)
    json_dump_time = json.dumps({
        "uptime_str": str(uptime),
        "uptime_hours": uptime.total_seconds() / (60 * 60)
    })

    return json_dump_time

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
