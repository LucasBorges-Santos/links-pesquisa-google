from bs4 import BeautifulSoup
import requests, urllib.parse
import lxml

def print_extracted_data_from_url(url):

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')


    for container in soup.findAll('div', class_='tF2Cxc'):
        head_link = container.a['href']
        print(head_link)

    return soup.select_one('a#pnnext')



next_page_node = print_extracted_data_from_url('https://www.google.com/search?hl=en-US&q=python')
