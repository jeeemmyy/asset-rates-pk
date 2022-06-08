def getUsdRates():
    from bs4 import BeautifulSoup
    from requests import get
    from bs2json import bs2json

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    html = get(
        'https://www.linkexchange.com.pk', headers=headers).text

    soup = BeautifulSoup(html, 'lxml')

    converter = bs2json()

    data = soup.find("tr", {"id": "usd"})
    print(data)

    jsonData = converter.convert(data)

    return jsonData
