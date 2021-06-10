from bs4 import BeautifulSoup
import requests

html_text= requests.get('https://www.sothebys.com/en/buy/auction/2021/the-swiss-fine-art-sale').text
soup = BeautifulSoup(html_text,'html.parser')
arts = soup.find_all('div', class_='css-1up9enl')

for art in arts:

    lot_art = art.find('p', class_='css-8908nx').text.replace('','')
    det_art = art.find('p', class_='css-17ei96f').text.replace('','')
    est_art = art.find('span', class_='css-17b8gen').text.replace('','')
    cur_bid = art.find('span', class_='css-1ls9t5d').text.replace('', '')
    time_left = art.find('div', class_='css-1nmxx7h').text.replace('', '')


print(f"lot_number: {lot_art.strip()}")
print(f"art_details: {det_art.strip()}")
print(f"estimate: {est_art.strip()}")
print(f"current_bid: {cur_bid.strip()}")
print(f"time_left: {time_left.strip()}")

'''print(f" 
     lot_number:{lot_art}
    art_details: {det_art}
    estimate: {est_art}
    current_bid: {cur_bid}
    time_left: {time_left}"

      )
'''
print(' ')