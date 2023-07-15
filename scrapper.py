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

    title = soup2.find('title').text.strip()

    store = soup2.find("p", {"class":"wt-text-body-03 wt-line-height-tight wt-mb-lg-1"}).text.strip()

    t = soup2.find("a", {"class":"wt-text-link-no-underline", "href" : "#reviews"}).text.strip()
    n = t.index('(')
    m = t.index(')')
    review_nums = int(t[n+1:m-8])
    title = title[:-14]
    
    return title, store, review_nums, reviews