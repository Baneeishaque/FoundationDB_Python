import fdb
fdb.api_version(510)
db = fdb.open()
db['hello'.encode()] = 'world'.encode()
print ('hello', db['hello'.encode()].decode())
