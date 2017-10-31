from netaddr import IPNetwork

#http://blog.trendmicro.com/trendlabs-security-intelligence/a-closer-look-at-north-koreas-internet/
ipranges='''5.62.56.160/30
5.62.61.64/30
45.42.151.0/24
46.36.203.81/32
46.36.203.82/30
57.73.224.0/19
88.151.117.0/24
172.97.82.128/25
175.45.176.0/22
185.56.163.144/28
210.52.109.0/24'''

for cidr in ipranges.splitlines():
	for ip in IPNetwork(cidr):
		print '%s' % ip
