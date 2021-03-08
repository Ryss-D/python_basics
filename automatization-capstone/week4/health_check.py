import psutil
import socket
import emails

error_mensagges = {'cpu_error' : 'Error - CPU usage is over 80%',
    'space_error' : 'Error - Available disk space is less than 20%',
    'memory_error' : 'Error - Available memory is less than 500MB',
    'hostname_error' : 'Error - localhost cannot be resolved to 127.0.0.1',
    }

cpu_usage = psutil.cpu_percent(interval = 1)
if cpu_usage > 0.80:
    message = emails.generate_issue_email("username", error_mensagges["cpu_error"])
    emails.send_email("username", "password", message)
space_used = psutil.disk_usage('C:\\')[3] #Element 3
if space_used >= 0.80:
    message = emails.generate_issue_email("username", error_mensagges["space_error"])
    emails.send_email("username", "password", message)
memory_avaliable = psutil.virtual_memory()[1] #Element 1
THRESHOLD = 500 * 1024 * 1024
if memory_avaliable < THRESHOLD:
    message = emails.generate_issue_email("username", error_mensagges["memory_error"])
    emails.send_email("username", "password", message)
host_ip = socket.gethostbyname('localhost')
if host_ip != '127.0.0.1':
    message = emails.generate_issue_email("username", error_mensagges["hostname_error"])
    emails.send_email("username", "password", message)