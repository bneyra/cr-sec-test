import os
host = input("host to ping: ")
os.system("ping -c 1 " + host)
