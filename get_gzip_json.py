import json
import gzip
import requests
import zlib

url = "https://pm25.lass-net.org/data/last-all-epa.json.gz"

r = requests.get(url)
json_bytes = zlib.decompress(r.content,15+32)

json_str = json_bytes.decode('utf-8')           
data = json.loads(json_str)                     

print(data)