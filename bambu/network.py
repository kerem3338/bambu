#Bambu Engine - Network

import urllib.request as urllib2
import socket
class Network:
    def __init__(self):
        self.host = socket.gethostname()
        self.localhost = socket.gethostbyname(self.host)

        
    def internet_required(self, error="İnternet bağlantısı gerekli, lütfen internet bağlantınızı kontrol edin"):
        
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            print(error)
        else:
            return True
            


