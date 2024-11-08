class Codec:
    baseUrl = "https://tinyurl.com/"
    upperCaseMin = 65
    upperCaseMax = 90
    codeLength = 10

    def __init__(self):
        self.store = {}
    
    def __randomCode(self):
        code = ""

        for i in range(self.codeLength):
            code += chr(random.randint(self.upperCaseMin, self.upperCaseMax) + random.randint(0, 1) * 32)
        
        return code


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        code = self.__randomCode()

        while code in self.store:
            code = self.__randomCode()


        self.store[code] = longUrl

        return self.baseUrl + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.store[shortUrl[-self.codeLength:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))