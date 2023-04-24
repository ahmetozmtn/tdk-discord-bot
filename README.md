<h1 align="center">TDK Discord Bot</h1>

Bu proje Python ile geliştirilmiştir. TDK API'ini kullanan Discord Kelime Botu

<br>

Proje de kullanılan kütüphaneler;
- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [requests](https://github.com/psf/requests)

<br>

## Proje'yi İndirme

```shell
git clone REPO_URL
cd tdk-discord-bot
```

## Kurulum

- ### Ortam değişklenlerinin ayarlamması

```shell
cp .env.example .env
# .env.example dosyasını .env olarak değiştirin.
# ardından BOT_TOKEN değişkenine oluşturmuş olduğunuz discord botunun token'ını yapıştırın
```

## Çalıştırma


```shell
pip3 install -r requirements.txt
# Gerekli kütüphanelerini kurulumu
python main.py
# main.py dosyasını çalıştırır.
```