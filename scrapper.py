from bs4 import BeautifulSoup
import requests


def scrap(URL):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Language": "en-US, en;q=0.5",
    }
    webpage = requests.get(URL, headers=HEADERS)
    soup1 = BeautifulSoup(webpage.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    reviews = []
    for n in range(4):
        review = soup2.find(id="review-preview-toggle-" + str(n))
        reviews.append(review.text.strip())
    return reviews
