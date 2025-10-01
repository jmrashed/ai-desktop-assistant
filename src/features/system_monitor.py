import psutil

class SystemMonitor:
    def get_system_info(self):
        """Get system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return f"System Info:\nCPU: {cpu_percent}%\nMemory: {memory.percent}%\nDisk: {disk.percent}%"
        except Exception as e:
            return f"Error getting system info: {str(e)}"