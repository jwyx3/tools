#!/usr/bin/env python
"""
List specfic number of avaiable IPs within one IP range

E.g. python list-avaiable-ips.py start=10.155.90.130 end=10.155.90.254 num=5

* start - start IP of this range, 10.155.90.130 by default
* end - end IP of this range, 10.155.90.254 by default
* num - number of available IPs to search, 5 by default

All parameters are optional.

Compatibility

* Python 2.4.3

v0.1 - 4/8/2014

"""

try:
    from ipaddress import ip_address
except ImportError:
    from ipaddr import IPAddress as ip_address

import sys, os, subprocess

def findIPs(start, end):
    """Find all IPs with this range from start to end"""
    start = ip_address(start)
    end = ip_address(end)
    result = []
    while start <= end:
        result.append(str(start))
        start += 1
    return result

def pingIP(address):
    """ bash equivalent: ping -c 1 address """
    retcode = subprocess.call(['ping', address, '-c 1'], stdout=open(os.devnull));
    return retcode == 0

def parseArgv(start, end, num):
    """Parse key=value pairs parameters from command line"""
    result = []
    args = dict([arg.split('=') for arg in sys.argv[1:]])
    result.append(args.get('start', start))
    result.append(args.get('end', end))
    result.append(int(args.get('num', num)))
    return result

if __name__ == '__main__':

    if len(sys.argv) <= 2:
        print __doc__

    print 'Start to search available IPs ...'

    start, end, num = parseArgv('10.155.90.130', '10.155.90.254', 5)

    for address in findIPs(start, end):
        if num <= 0:
            break
        if not pingIP(address):
            print address, 'OK', num
            num -= 1
