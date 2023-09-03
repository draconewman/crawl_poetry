
import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from urllib.parse import unquote, urlparse

poet_links_path = r"D:\STUDY\Projects\FYP\crawl_poetry\poets_links.txt"
output_path = r"D:\STUDY\Projects\FYP\crawl_poetry\output"


def create_poet_folders(poet_links_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(poet_links_path, 'r', encoding='utf-8') as file:
        links = file.readlines()

    for link in links:
        # Remove any leading/trailing whitespaces and line breaks
        link = link.strip()

        # Extract the unique term from the link
        unique_term = link.split("/")[-2]

        # Create the subfolder path
        subfolder_path = os.path.join(output_path, unique_term)

        # Create the subfolder if it doesn't exist
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        print(unique_term, '\n')
        get_poem_links(link, subfolder_path)

def get_poem_term(link):
    parsed_url = urlparse(link)
    path_components = unquote(parsed_url.path).split('/')
    unique_term = path_components[-2]
    return unique_term

def get_poem_links(url, subfolder_path):
    driver = webdriver.Chrome()
    driver.get(url)
    content = driver.page_source
    driver.quit()     
    
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('h2', {'class': 'entry-title'})
    for link in links:
        href = link.find('a')['href']
        extract_poems(href, subfolder_path)


def extract_poems(url, output_directory):   
    driver = webdriver.Chrome()
    driver.get(url)
    content = driver.page_source
    driver.quit() 
    unique_term = get_poem_term(url)

    # Find the poem part using regular expressions
    poem_pattern = r'<div class="kksr-legend"(.*?)<div class="heateorSssClear"'
    poem_match = re.search(poem_pattern, content, re.DOTALL)

    # Find the Bengali terms using regular expressions
    terms_pattern = r'<strong>কবিতা:</strong>(.*?)<article id'
    terms_match = re.search(terms_pattern, content, re.DOTALL)

    if poem_match and terms_match:
        poem = poem_match.group(1).strip()
        bengali_terms = re.findall(r'([ঀ-৾:]+)', terms_match.group(1))

        # Save the poem in a separate .txt file with the same name
        output_file_path = os.path.join(output_directory, f"{unique_term}.txt")
        with open(output_file_path, 'w', encoding='utf-8') as poem_file:
            # Write Bengali terms to the beginning of the output file
            for term in bengali_terms:
                poem_file.write(term + " ")
            poem_file.write("\n")

            # Write the extracted poem
            poem_file.write(poem)

        print("Poem extracted and saved:", output_file_path, '\n')
        print(unique_term, '\n')       


create_poet_folders(poet_links_path, output_path)
    # settings = get_project_settings()
    # process = CrawlerProcess(settings)
    # process.crawl(MySpider1)
    # process.crawl(MySpider2)
    # process.start()

