import sys
print(sys.version)
print(sys.version_info)
print(sys.hexversion)
print('================')
from platform import python_version
print(python_version())

import sys
sys.version.split(' ')[0]


from sys import version_info, api_version, version, hexversion
print('==================')
print(f"sys.version: {version}")
print(f"sys.api_version: {api_version}")
print(f"sys.version_info: {version_info}")
print(f"sys.hexversion: {hexversion}")

print('=============')
import os
ver = os.popen('python -V').read().strip()
print(ver)
