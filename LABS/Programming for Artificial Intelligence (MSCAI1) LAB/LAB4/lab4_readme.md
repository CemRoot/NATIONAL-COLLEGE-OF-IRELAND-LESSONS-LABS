Aşağıda, kodunuzun işlevlerini ve neden kullanıldıklarını açıklayan bir `README.md` dosyası bulunmaktadır:

```markdown
# Web Scraping Quotes

Bu proje, Python kullanarak bir web sitesinden alıntıları nasıl kazıyacağınızı gösterir. Betik, web sitesine bir GET isteği gönderir, HTML içeriğini ayrıştırır ve alıntıları yazarlarıyla birlikte çıkarır.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi
- `beautifulsoup4` kütüphanesi

Gerekli kütüphaneleri pip kullanarak yükleyebilirsiniz:

```bash
pip install requests beautifulsoup4
```

## Kullanım

Betik şu şekilde çalıştırılır:

```bash
python lab4_Scraping.py
```

## Kod Açıklaması

### Kütüphanelerin İçe Aktarılması

```python
import requests
from bs4 import BeautifulSoup
```

- `requests`: Bu kütüphane, web sitesine HTTP istekleri göndermek için kullanılır.
- `BeautifulSoup`: Bu kütüphane, web sayfasının HTML içeriğini ayrıştırmak için kullanılır.

### GET İsteği Gönderme

```python
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
```

- `url`: Kazınacak web sitesinin URL'si.
- `requests.get(url)`: Belirtilen URL'ye bir GET isteği gönderir ve yanıtı saklar.

### Yanıt Durumunu Kontrol Etme

```python
if response.status_code == 200:
    print("Successfully accessed the webpage.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

- `response.status_code`: İsteğin başarılı olup olmadığını kontrol etmek için yanıtın durum kodunu kontrol eder (durum kodu 200).

### HTML İçeriğini Ayrıştırma

```python
soup = BeautifulSoup(response.content, 'html.parser')
```

- `BeautifulSoup(response.content, 'html.parser')`: Yanıtın HTML içeriğini HTML ayrıştırıcı kullanarak ayrıştırır.

### Alıntıları Bulma

```python
quotes = soup.find_all('div', class_='quote')
```

- `soup.find_all('div', class_='quote')`: Sayfadaki alıntıları içeren `quote` sınıfına sahip tüm `div` öğelerini bulur.

### Alıntıları ve Yazarları Çıkarma ve Yazdırma

```python
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f'Quote: {text}')
    print(f'Author: {author}')
    print('-' * 50)  # Okunabilirlik için ayırıcı
```

- `quote.find('span', class_='text').get_text()`: Alıntının metnini çıkarır.
- `quote.find('small', class_='author').get_text()`: Alıntının yazarını çıkarır.
- `print(f'Quote: {text}')`: Alıntı metnini yazdırır.
- `print(f'Author: {author}')`: Alıntının yazarını yazdırır.
- `print('-' * 50)`: Okunabilirlik için bir ayırıcı çizgi yazdırır.

## Sonuç

Bu betik, Python kullanarak temel bir web kazıma görevini göstermektedir. Web sitesine bir GET isteği gönderir, HTML içeriğini ayrıştırır ve sayfadaki belirli bilgileri (alıntılar ve yazarlar) çıkarır.
```