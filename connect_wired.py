import requests
import pandas as pd
import sys
from  beautifulsoup4 import BeautifulSoup
from time import *
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from config import MY_COOKIE
from help_main import help_choise
from convert_file import convert

arguments = help_choise()
number_pages = arguments[0]
category_choise = arguments[1]
output_file = arguments[2]


for num in (number + 1 for number in range(number_pages)):
    url = f'https://www.wired.com/category/{category_choise}/page/{num}/'
    print(url)
    headers = {'authority': 'www.wired.com', 'user-agent': 'Slow wired subsciber parser, for my personal comfort (0.1)', 'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                'cookie': MY_COOKIE}
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
    s.mount('https://', HTTPAdapter(max_retries=retries))
    page = s.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    main_archive_list = soup.find("div", {"class": "archive-listing-component"})
    try:
        articles_info = main_archive_list.find_all("ul", {"class": "archive-list-component__items"})
    except AttributeError as err:
        print(err)
        print("Check category in argument or pages and")
        sys.exit()
    article_list = []
    articles_blocks_list = []
    time_list = []
    author_list = []
    title_list = []
    discribe_list = []
    link_list = []

    for items in articles_info:
        component_info = items.find_all("div", {"class": "archive-item-component__info"})
        for one_block in component_info:
            # print(one_block)
            time = one_block.find("time")
            author = one_block.find("div", {"class": "byline-component byline-component--micro"})
            # print(author.text)
            title = one_block.find("h2")
            # print(title.text)
            discribe = one_block.find("p")
            # print(discribe.text)
            link = one_block.find("a", {"class": "archive-item-component__link"})
            # print(link['href'])
            time_list.append(time.text)
            try:
                author_list.append(author.text)
            except AttributeError as err:
                author_list.append('None')
                print(err)
                sys.exit()
            title_list.append(title.text)
            discribe_list.append(discribe.text)
            link_list.append('https://www.wired.com' + link['href'])

    articles_blocks_list = [time_list, author_list, title_list, discribe_list, link_list]
    # print(articles_blocks_list)

    for index in range(len(time_list)):
        with open(output_file + '.md', 'a') as f:
            f.write(time_list[index] + ' | ')
            f.write(author_list[index])
            f.write('\n')
            f.write('**' + title_list[index] + '**')
            f.write('\n')
            f.write(discribe_list[index])
            f.write('\n')
            f.write(link_list[index])
            f.write('\n' + '\n')
    print(f"End page {num}")
    sleep(1)
converted_output_file = output_file + ".html"
convert_file.convert(output_file, converted_output_file)