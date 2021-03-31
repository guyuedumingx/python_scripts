import requests

class request:

    def __init__(self):
        self.url = "http://8.136.185.193/api/Search"
        self.method = "POST"
        self.data = {
            "keyword" : "周杰伦"
        }

    def get_res(self):
        res = requests.post(self.url, data=self.data)
        res.encoding = res.apparent_encoding
        return res.text
    
req = request()
print(req.get_res())