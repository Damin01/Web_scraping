#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page.text, 'html.parser')

#Get data from first table on the website
table = soup.find_all('table')[1]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

# Get data in pandas
df = pd.DataFrame(columns = world_table_titles)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(df['Rank'].values,df['Revenue (USD billions)'].values)
ax1.set_xlabel('Rank')
ax1.set_ylabel('Revenue')
ax1.set_title('Rank vs. Revenue')
ax1.grid()

ax2.plot(df['Rank'].values,df['Employees'].values)
ax2.set_xlabel('Rank')
ax2.set_ylabel('Employees')
ax2.set_title('Rank vs. Employees')
ax2.grid()

plt.tight_layout()
plt.show()
