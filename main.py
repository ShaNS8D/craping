""" <div class="bloko-gap bloko-gap_top">
<span class="pager-item-not-in-short-range" data-qa="pager-page-wrapper-40-39">
<a class="bloko-button" rel="nofollow" data-qa="pager-page" href="/search/vacancy?text=python&amp;area=1&amp;area=2&amp;page=39&amp;hhtmFrom=vacancy_search_list">
<span>40</span>
</a><span class="bloko-form-spacer"></span></span>
"""

from bs4 import BeautifulSoup
import fake_headers
import requests


headers_gen = fake_headers.Headers(os="win", browser="chrome")

response = requests.get(
    "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=headers_gen.generate())
main_html_data = response.text
main_soup = BeautifulSoup(main_html_data, "lxml")

obl = main_soup.find_all("a", class_="bloko-button")
num_page = int(obl[-2].text)
tags_all = []
for i in range(0, num_page):
    articles_list_tag = main_soup.find("div", id="a11y-main-content")
    articles_tags = articles_list_tag.find_all(
        "div", class_="vacancy-serp-item-body__main-info")
    tags_all = tags_all + articles_tags

articles_data = []

for article_tag in tags_all:

    h3_tag = article_tag.find("h3", class_="bloko-header-section-3")

    span_tag = h3_tag.find("span")
    a_tag = span_tag.find("a")
    link_absolute = a_tag["href"]
    response = requests.get(link_absolute, headers=headers_gen.generate())
    article_html_data = response.text
    article_soup = BeautifulSoup(article_html_data, "lxml")
    article_body_tag = article_soup.find("div", class_="g-user-content")
    if article_body_tag != None:
        body_tag = article_body_tag.text
    else:
        body_tag = "None"


    if (("Django" in body_tag) and ("Flask" in body_tag)):
        com_tag = article_tag.find(
            "a", class_="bloko-link bloko-link_kind-tertiary")
        company_name = com_tag.text.strip()

        sal_tag = article_tag.find("span", class_="bloko-header-section-2")
        if sal_tag != None:
            salary = sal_tag.text
        else:
            salary = "None"

        city_tag = article_tag.find("div", class_="bloko-text")
        city = city_tag.text.strip()
        articles_data.append(
            {
                "link": link_absolute,
                "salary": salary,
                "company_name": company_name,
                "city": city
            }
        )


print((articles_data))
