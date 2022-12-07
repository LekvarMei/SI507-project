import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd

drug_name_list = []
dosage_form_list = []
ingredient_list = []
labeler_list = []
NDC_code_list = []

BASE_URL = 'https://www.drugs.com/'
COURSES_PATH = 'otc-a1.html'

## Make the soup for the Courses page
courses_page_url = BASE_URL + COURSES_PATH
response = requests.get(courses_page_url)
soup = BeautifulSoup(response.text, 'html.parser')

drugs_listing_parent = soup.find('ul', class_='ddc-list-column-2')
drugs_listing_lis = drugs_listing_parent.find_all('li')
for drug_listing_lis in drugs_listing_lis:

    drug_link_tag = drug_listing_lis.find('a')
    drug_details_path = drug_link_tag['href']
    drug_details_url = BASE_URL + drug_details_path 

    ## Make the soup for course details
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