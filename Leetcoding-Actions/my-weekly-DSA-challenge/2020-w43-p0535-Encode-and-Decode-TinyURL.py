class Codec:
    def __init__(self):
        self.counter = 0
        self.base62 = string.ascii_lowercase + string.ascii_uppercase + '0123456789'
        self.data = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = ''.join(random.Random(self.counter).sample(self.base62, 3))
        self.data[key] = longUrl
        return 'http://tinyurl.com/' + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split('/')[-1]
        return self.data[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
