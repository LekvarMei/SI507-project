import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd

drug_name_list = []
dosage_form_list = []
ingredient_list = []
labeler_list = []
NDC_code_list = []


BASE_URL = 'https://www.drugs.com/'
COURSES_PATH = 'otc-a1.html'
CACHE_FILE_NAME = 'cachedrug_Scrape.json'
headers = {'User-Agent': 'UMSI 507 Course Project - Python Web Scraping','From': 'youremail@domain.com','Course-Info': 'https://www.si.umich.edu/programs/courses/507'}

def load_cache():
    try:
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(cache):
    cache_file = open(CACHE_FILE_NAME, 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()


def make_url_request_using_cache(url, cache):
    if (url in cache.keys()): # the url is our unique key
        print("Using cache")
        return cache[url]
    else:
        print("Fetching")
        time.sleep(1)
        response = requests.get(url, headers=headers)
        cache[url] = response.text
        save_cache(cache)
        return cache[url]


courses_page_url = BASE_URL + COURSES_PATH
response = requests.get(courses_page_url)
soup = BeautifulSoup(response.text, 'html.parser')

drugs_listing_parent = soup.find('ul', class_='ddc-list-column-2')
drugs_listing_lis = drugs_listing_parent.find_all('li')
for drug_listing_lis in drugs_listing_lis:

    drug_link_tag = drug_listing_lis.find('a')
    drug_details_path = drug_link_tag['href']
    drug_details_url = BASE_URL + drug_details_path 

    response = requests.get(drug_details_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if (soup.find('div', class_='ddc-pid-list') == None):
        drug_name = soup.find('div', class_='contentBox').find('h1')
        drug_name_list.append(drug_name.text.strip())

        dosage_form = soup.find('p', class_='drug-subtitle').find('b').next_sibling
        dosage_form_list.append(dosage_form.text.strip())

        ingredient = soup.find('p', class_='drug-subtitle').find('b').next_sibling.next_sibling.next_sibling.next_sibling
        ingredient_list.append(ingredient.text.strip())
dict = {'drug_name': drug_name_list, 'dosage_form': dosage_form_list, 'ingredient': ingredient_list}
df = pd.DataFrame(dict)  
df.to_csv('drug.csv')