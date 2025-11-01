import ipaddress
from gate.tasks import save

def ip_range_int(from_ip, to_ip, country_code):
    start = int(ipaddress.IPv4Address(from_ip))
    end = int(ipaddress.IPv4Address(to_ip))
    save.delay(start,end,country_code)
