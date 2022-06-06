def getGoldRates():
    from bs4 import BeautifulSoup
    from requests import get
    from bs2json import bs2json
    import json

    html = get(
        'https://www.urdupoint.com/business/gold-rates-in-pakistan.html').text

    soup = BeautifulSoup(html, 'lxml')
    converter = bs2json()

    data = soup.tbody.tr
    jsonData = converter.convert(data)

    return jsonData
