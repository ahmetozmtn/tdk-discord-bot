import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"


def tdkresponse(kelime):
    url = f"https://sozluk.gov.tr/gts?ara={kelime}"
    headers = requests.utils.default_headers()
    headers.update({"User-Agent": USER_AGENT})
    response = requests.get(url, headers=headers)
    result = response.json()
    for item in result:
        if "error" in result:
            return "Hatalı Kelime!"
        return item["anlamlarListe"][0]["anlam"]
