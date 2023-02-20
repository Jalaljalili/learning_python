import ipaddress

networks = ['192.168.1.0/25', '172.16.1.0/24', '0.0.0.0/0', '4.1.56.2/32']


new = list(map(lambda x: ipaddress.ip_network(x).with_netmask, filter(lambda x: True if ipaddress.ip_network(x).is_global else False , networks)))


print (new)