# Install urllib3 package using PIP. 
# Send HTTP requests to any URL and print status for the same.

import urllib3

b = urllib3.PoolManager()
url = input('Enter your url: ')
r = b.request('GET', url)
f = r.status
    
print("status of url is:",f)
print('finished')