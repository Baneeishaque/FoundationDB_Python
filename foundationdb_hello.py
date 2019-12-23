import fdb
fdb.api_version(520)
db = fdb.open()
db['hello'.encode()] = 'world'.encode()
print ('hello', db['hello'.encode()].decode())
