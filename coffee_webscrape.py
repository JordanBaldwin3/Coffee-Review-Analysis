import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

links = []
records = []
start = 0
df = pd.DataFrame()

# For each review on the page, find the link to the review page and store in links list
for i in range(start,313):
    print("Page"+str(i+1)+"..."+" time = "+ str(datetime.datetime.now()))
    url = 'http://www.coffeereview.com/review/page/'+str(i+1)+'/'
    headers = {'User-Agent':'Chrome'}
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'html.parser')
    review_scores = soup.find_all('div', attrs={'class':'review-template-rating'})
    links = soup.find_all('a', attrs={'title':'Read Complete Review'})
    records = []
    # For each link in the list, go to the review page, extract info and store in records list, then add to df
    for link in links:
        try:  
            link = (link.get('href', None))
            review_text = requests.get(link, headers=headers).text
            review_soup = BeautifulSoup(review_text, 'html.parser')
            # print(review_soup)
            rating = review_soup.find('span', attrs={'class':'review-template-rating'}).text
            # print(rating)
            roaster = review_soup.find('p', attrs={'class':'review-roaster'}).text
            print(roaster)
            coffee_name = review_soup.find('h1', attrs={'class':'review-title'}).text
            # print(coffee_name)
            roaster_location = review_soup.find_all('table', attrs={'class':'review-template-table'})[0].find_all('td')[1].text
            # print(roaster_location)
            coffee_origin = review_soup.find_all('table', attrs={'class':'review-template-table'})[0].find_all('td')[3].text
            # print(coffee_origin)
            roast_level = review_soup.find_all('table', attrs={'class':'review-template-table'})[0].find_all('td')[5].text
            # print(roast_level)
            agtron = review_soup.find_all('table', attrs={'class':'review-template-table'})[0].find_all('td')[7].text
            # print(agtron)
            est_price = review_soup.find_all('table', attrs={'class':'review-template-table'})[0].find_all('td')[9].text
            # print(est_price)
            review_date = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[1].text
            # print(review_date)
            aroma = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[3].text
            # print(aroma)
            acidity = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[5].text
            # print(acidity)
            body = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[7].text
            # print(body)
            flavour = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[9].text
            # print(flavour)
            aftertaste = review_soup.find_all('table', attrs={'class':'review-template-table'})[1].find_all('td')[11].text
            # print(aftertaste)
            blind_assessment = review_soup.find_all('p')[22].text
            # print(blind_assessment)
            notes = review_soup.find_all('p')[23].text
            # print(notes)
            bottom_line = review_soup.find_all('p')[24].text
            # print(bottom_line)
            records = [(rating,roaster,coffee_name,roaster_location,coffee_origin,roast_level,est_price,review_date,
            agtron,acidity,body,flavour,aftertaste,blind_assessment,notes,bottom_line)]
        except:
            print("ERROR on Page"+str(i+1)+"..."+" time = "+ str(datetime.datetime.now()))
            pass

        col_names = ['rating','roaster','coffee_name','roaster_location','coffee_origin','roast_level','est_price','review_date',
        'agtron','acidity','body','flavour','aftertaste','blind_assessment','notes','bottom_line']

        df_tmp = pd.DataFrame(records, columns=col_names)
        df = df.append(df_tmp, ignore_index=True)

df.to_csv('coffeedata.csv', index=False, encoding='utf-8')

# links=[]
# records=[]
# starting_point = 0
# df = 1 # clear
# df = pd.DataFrame()

# for i in range(starting_point,2):
#     print("Page"+str(i+1)+"..."+" time = "+ str(datetime.datetime.now()))
#     url = 'http://www.coffeereview.com/review/page/'+str(i+1)+'/'
#     headers = {'User-Agent':'Chrome/74.0'}
#     r = requests.get(url, headers=headers)
#     soup = BeautifulSoup(r.text, 'html.parser') 
#     links = soup.find_all('a', attrs={'title':'Read Complete Review'})
#     records=[]
#     for link in links:
#         try:
#             link = link.get('href', None)
#             review = requests.get(link, headers=headers)
#             reviewsoup = BeautifulSoup(review.text, 'html.parser') 
#             rating = reviewsoup.find('div', attrs={"class":"review-rating"}).text
#             company = reviewsoup.find('div', attrs={"class":"review-col1"}).find('h3').text 
#             coffee_name = reviewsoup.find('div', attrs={"class":"review-col1"}).find('h2').text
#             location = reviewsoup.find_all('strong')[0].text
#             origin = reviewsoup.find_all('strong')[1].text
#             roast = reviewsoup.find_all('strong')[2].text
#             price = reviewsoup.find_all('strong')[3].text
#             review_date = reviewsoup.find_all('strong')[4].text
#             agtron = reviewsoup.find_all('strong')[5].text
#             aroma = reviewsoup.find_all('strong')[6].text
#             acidity = reviewsoup.find_all('strong')[7].text
#             body = reviewsoup.find_all('strong')[8].text
#             flavor = reviewsoup.find_all('strong')[9].text
#             aftertaste = reviewsoup.find_all('strong')[10].text
#             review = reviewsoup.find_all('p')
#             blind_assesment = review[14].text
#             notes = review[16].text
#             bottom_line = review[17].text
            # records = [(rating,company,coffee_name,location,origin,roast,price,review_date,
            #                                         agtron,acidity,body,flavor,aftertaste,blind_assesment,notes,bottom_line)]
#         except:
#             print("ERROR on Page"+str(i+1)+"..."+" time = "+ str(datetime.datetime.now()))
#             pass
#         dftemp = pd.DataFrame(records, columns=['rating','company','coffee_name','location','origin','roast','price','review_date',
#                                                 'agtron','acidity','body','flavor','aftertaste','blind_assesment','notes','bottom_line'
#                                                ]) 

#         df = df.append(dftemp, ignore_index=True)
#         df.to_csv('coffeedata.csv', index=False, encoding='utf-8')
       