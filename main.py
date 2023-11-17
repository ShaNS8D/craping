"""
div class="tm-articles-list
article
<time datetime="2023-10-26T16:04:51.000Z" title="2023-10-26, 19:04">58 минут назад</time>
h2 class="tm-title tm-title_h2"
a href
span
post-content-body
"""
# import bs4
from bs4 import BeautifulSoup
import fake_headers
import requests

headers_gen = fake_headers.Headers(os="win", browser="chrome")

response = requests.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=headers_gen.generate())
main_html_data = response.text


main_soup = BeautifulSoup(main_html_data, "lxml")


articles_list_tag = main_soup.find("div", id="a11y-main-content")


articles_tags = articles_list_tag.find_all("div", class_="vacancy-serp-item-body__main-info")

articles_data = []

for article_tag in articles_tags:
    # time_tag = article_tag.find("time")
    # pub_time = time_tag["datetime"]

    h3_tag = article_tag.find("h3", class_="bloko-header-section-3")
    span_tag = h3_tag.find("span")

    header = span_tag.text.strip()

    # a_tag = span_tag.find("a")
    # link_relative = a_tag["href"]

    # link_absolute = urljoin("https://habr.com/", link_relative)

    # response = requests.get(link_absolute, headers=headers_gen.generate())
    # article_html_data = response.text
    # article_soup = bs4.BeautifulSoup(article_html_data, "lxml")

    # article_body_tag = article_soup.find("div", id="post-content-body").text

    articles_data.append(
        {
            "header": header,
            # "link": link_absolute,
            # "pub_time": pub_time,
            # "text": article_body_tag[:100],
        }
    )


print(len(articles_data))
