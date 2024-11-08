class Codec:
    baseUrl = "https://tinyurl.com/"
    upperCaseMin = 65
    upperCaseMax = 90
    codeLength = 10

    def __init__(self):
        self.store = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        code = ""

        for i in range(self.codeLength):
            code += chr(random.randint(self.upperCaseMin, self.upperCaseMax) + random.randint(0, 1) * 32)

        while code in self.store:
            code = ""

            for i in range(self.codeLength):
                code += chr(random.randint(self.upperCaseMin, self.upperCaseMax) + random.randint(0, 1) * 32)

        
        shortUrl = self.baseUrl + code
        self.store[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.store[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))