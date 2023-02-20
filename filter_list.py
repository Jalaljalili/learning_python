import ipaddress

networks = ['192.168.1.0/25', '172.16.1.0/24', '0.0.0.0/0', '4.1.56.2/32']

def convert(network):
    return ipaddress.ip_network(network).with_netmask

def public(network):
    if ipaddress.ip_network(network).is_global:
        return  True

new = list(map(convert, filter(public, networks)))

#new =[]
#for network in networks:
#      if ipaddress.ip_network(network).is_global:
#            new.append(convert(network))

print (new)