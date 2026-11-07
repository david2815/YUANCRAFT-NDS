import os, re

with open(os.path.join(os.environ['TEMP'], 'devkitProUpdater.exe'), 'rb') as f:
    data = f.read()

urls = re.findall(b'https?://[a-zA-Z0-9./_-]+', data)
for u in set(urls):
    print(u.decode('ascii'))
