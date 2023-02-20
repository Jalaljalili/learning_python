import ipaddress

networks = ['192.168.1.0/25', '172.16.1.0/24', '0.0.0.0/0', '4.1.56.2/32']

def convert(network):
    return ipaddress.ip_network(network).with_netmask

new = list(map(convert, networks))
#new =[]
#for network in networks:
#      new.append(convert(network))

print (new)