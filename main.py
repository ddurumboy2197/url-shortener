class URLShortener:
    def __init__(self):
        self.url_map = {}

    def generate_short_url(self, original_url):
        import uuid
        short_url = str(uuid.uuid4())[:6]
        self.url_map[short_url] = original_url
        return f"http://short.url/{short_url}"

    def get_original_url(self, short_url):
        return self.url_map.get(short_url.split("/")[-1])

    def update_url_map(self, short_url, original_url):
        self.url_map[short_url] = original_url

    def delete_url_map(self, short_url):
        if short_url in self.url_map:
            del self.url_map[short_url]

# Misol foydalanuvchi
url_shortener = URLShortener()

# Original URL yaratish
original_url = "https://www.example.com/original-url"
print(f"Original URL: {original_url}")

# Qisqartirilgan URL yaratish
short_url = url_shortener.generate_short_url(original_url)
print(f"Qisqartirilgan URL: {short_url}")

# Asl URL qidirish
print(f"Asl URL: {url_shortener.get_original_url(short_url.split('/')[-1])}")

# URL mapni yangilash
url_shortener.update_url_map(short_url.split('/')[-1], "https://www.example.com/yangilangan-url")
print(f"Yangilangan URL map: {url_shortener.url_map}")

# URL mapdan o'chirish
url_shortener.delete_url_map(short_url.split('/')[-1])
print(f"O'chirilgan URL map: {url_shortener.url_map}")
