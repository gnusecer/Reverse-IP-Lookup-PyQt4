import urllib.request
import re


class ReverseIP:
    """ This class collects the data using the API for reverse ip lookups"""

    def __init__(self):

        self.api = "http://viewdns.info/reverseip/?host="

        self.results = []

        self.user_agent= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)'}


    def getHosts(self,host):
        self.url = "http://viewdns.info/reverseip/?host={0}&t=1".format(host)
        req = urllib.request.Request(self.url, headers=self.user_agent)
        page_data = urllib.request.urlopen(req)
        data = page_data.read()
        hosts = re.findall(b'<tr><td>\S+</td><td', data)
        for host in hosts:
            host = host.replace(b'<tr><td>', b'').replace(b'</td><td', b'')
            if host.startswith(b'http://'):
                pass
            else:
                host = "http://{0}".format(host.decode())
            if "Domain" not in host:
                self.results.append(str(host))

        return self.results
    
if __name__ == "__main__":

    rIP = ReverseIP()
    res = rIP.getHosts("1337coder.co.uk")
    print(res)
  
    
