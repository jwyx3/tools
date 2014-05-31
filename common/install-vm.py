#!/usr/bin/env python
"""
Install ova in esx host

The config file template (vm.conf):

script <the location of ovftool binary, e.g. /usr/bin/ovftool>
name <name of vm machine>
datastore <name of datastore, e.g. nsmesx41-disk2>
image <the location of ova image in local machine>
user <user in esx host>
password <password of user in esx host>
host <address of esx host>

Usage: cat vm.conf |python install-vm.py

v0.1 - 5/31/2014

"""

import subprocess, fileinput, re

def installVm(name, ds, img, user, password, host, **kwargs):
  if kwargs is not None:
    script = kwargs['script'] or '/usr/bin/ovftool'

  retVal = subprocess.call([script,
    '--acceptAllEulas', '--skipManifestCheck',
    '--name=' + name, '--datastore=' + ds, img,
    'vi://' + user + ':' + password + '@' + host])

  return retVal

if __name__ == '__main__':

  config = dict()
  for line in fileinput.input():
    # Skip comments and empty line
    if re.match('^#|^\s*$', line):
      continue
    # The delimiter can be either = or space
    key, val = re.split('[ =]+', line.rstrip())
    config[key] = val

  keys = ['name', 'datastore', 'image', 'user', 'password', 'host', 'script']
  name, ds, img, user, password, host, ovftool = [ config[k] for k in keys ]
  installVm(name, ds, img, user, password, host, script=ovftool)
