{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9c642b09-8ab2-4f0e-bae3-138563b0b8db",
   "metadata": {},
   "source": [
    "# Data Collection Using Web Scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7cee7dca-b12b-4005-beb1-2876508e62b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: bs4 in c:\\users\\samue\\anaconda3\\lib\\site-packages (0.0.2)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\samue\\anaconda3\\lib\\site-packages (from bs4) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\samue\\anaconda3\\lib\\site-packages (from beautifulsoup4->bs4) (2.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install bs4 #Installing the Library for the scrapping"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc9fe0eb-474a-450d-8419-f18a15a503c2",
   "metadata": {},
   "source": [
    "### IMPORTING NECESSARY LIBRARIES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d5ad5c64-fede-43a4-9af8-dbb0310deabe",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup \n",
    "import requests\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d036113d-8252-431c-8d4f-bcc0b4b480ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "response=requests.get('https://www.howstat.com/Cricket/Statistics/IPL/MatchScores.asp')\n",
    "#scrapping the data from the site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "02f24a4e-3aaa-4245-83f9-f5baf75e1a70",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup=BeautifulSoup(response.text,'html') #reading the data using beautifulSoup Library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d03277e1-8214-4bbd-a902-fca0f50fd754",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup=soup.find_all('table')[3] #finding the html code of the table that we wanted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "883a02a5-190a-4543-9ebd-006f333b5758",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[]\n",
    "for i in soup.find_all('tr'):\n",
    "    head=[h.text.strip() for h in i.find_all('td')]   #creating a list using the contents of the table\n",
    "    a.append(head)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1fff951-0225-4f3e-b6b9-0c0a2e860223",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "287e589d-522a-40fa-8f53-17bd4db8c9ce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "5cfbc3fa-c185-46af-b0c9-01ab0eeadb06",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.DataFrame(a)    #creating a new dataframe using the list data that we have already created\n",
    "df.columns=df.iloc[0] #using iloc function we make the first row of the dataframe to columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "eba52f63-1916-40ca-861f-f6b1799fe386",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.iloc[1:] #deleting the first row because we have already made it as columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "4b96f009-efec-4ed8-bd44-fb21bae2a83b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.iloc[:-1] #deleting the last row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "7e23fc04-87af-49c8-b297-1e3f0f2f6120",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(r'C:\\Users\\samue\\OneDrive\\Desktop\\CRICKET DATASET SCRAPPED\\match_data.csv') #to save the dataframe as a csv file, we used the function of to_csv and added the path of saving at last also added the filename that we wanted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "b82f6e49-2fba-4773-bf53-9b38de53c56e",
   "metadata": {},
   "outputs": [],
   "source": [
    "ndf=df.tail(10) #took the last 10 data as per the instruction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "977cca27-2bf1-4ae1-9c84-73eda55cb6c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\samue\\AppData\\Local\\Temp\\ipykernel_3820\\647097666.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  ndf[['winner','run/wicket']]=ndf['Result'].str.split('won by',expand=True)\n",
      "C:\\Users\\samue\\AppData\\Local\\Temp\\ipykernel_3820\\647097666.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  ndf[['winner','run/wicket']]=ndf['Result'].str.split('won by',expand=True)\n"
     ]
    }
   ],
   "source": [
    "ndf[['winner','run/wicket']]=ndf['Result'].str.split('won by',expand=True) #split the reult column to winner and run/wicket for easy understanding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "8dfad5ca-7aeb-454c-b217-b162bb89d383",
   "metadata": {},
   "outputs": [],
   "source": [
    "ndf=ndf.rename(columns={'Scorecard':'Date'}) #renamed the scorecard to date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "6793498c-d8dd-4db0-af11-fdba0531df20",
   "metadata": {},
   "outputs": [],
   "source": [
    "ndf=ndf.drop(columns=['Result']) #removed the result column because of we have already splitted the column to winners and run/wicket"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "d290117a-2d02-4df2-a5fb-8acba9a654a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0\n",
       "Team          0\n",
       "Score         0\n",
       "Versus        0\n",
       "Venue         0\n",
       "Date          0\n",
       "winner        0\n",
       "run/wicket    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndf.isnull().sum() #checked the null values of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "79dcabc2-f084-4480-833e-82be75deb565",
   "metadata": {},
   "outputs": [],
   "source": [
    "ndf=ndf.rename(columns={'Team':'Team1','Versus':'Team2'})  #renamed the teamname columns to team1 and team2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "cf5f524c-72c3-4377-8a05-3a9f4833d2ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Team1</th>\n",
       "      <th>Team2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Royal Challengers Bengaluru</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Punjab Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Lucknow Super Giants</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Gujarat Titans</td>\n",
       "      <td>Rajasthan Royals</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Gujarat Titans</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Rajasthan Royals</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Rajasthan Royals</td>\n",
       "      <td>Punjab Kings</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Lucknow Super Giants</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "0                         Team1                 Team2\n",
       "11          Sunrisers Hyderabad        Delhi Capitals\n",
       "12  Royal Challengers Bengaluru        Mumbai Indians\n",
       "13          Sunrisers Hyderabad          Punjab Kings\n",
       "14          Sunrisers Hyderabad      Rajasthan Royals\n",
       "15               Mumbai Indians  Lucknow Super Giants\n",
       "16               Gujarat Titans      Rajasthan Royals\n",
       "17               Gujarat Titans   Chennai Super Kings\n",
       "18             Rajasthan Royals   Sunrisers Hyderabad\n",
       "19             Rajasthan Royals          Punjab Kings\n",
       "20         Lucknow Super Giants        Mumbai Indians"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndf[['Team1','Team2']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "9a5c9f04-cece-48d7-869a-08b4e2ca2ab7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11    21/04/2026\n",
       "12    12/04/2026\n",
       "13    06/05/2026\n",
       "14    25/04/2026\n",
       "15    04/05/2026\n",
       "16    09/05/2026\n",
       "17    21/05/2026\n",
       "18    25/04/2026\n",
       "19    28/04/2026\n",
       "20    04/05/2026\n",
       "Name: Date, dtype: object"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndf['Date'] #the date of matches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "37f7f28f-aa43-4188-854c-d55fa69c68a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11                   Rajiv Gandhi International Stadium\n",
       "12                                     Wankhede Stadium\n",
       "13                   Rajiv Gandhi International Stadium\n",
       "14                               Sawai Mansingh Stadium\n",
       "15                                     Wankhede Stadium\n",
       "16                               Sawai Mansingh Stadium\n",
       "17                                Narendra Modi Stadium\n",
       "18                               Sawai Mansingh Stadium\n",
       "19    Maharaja Yadavindra Singh International Cricke...\n",
       "20                                     Wankhede Stadium\n",
       "Name: Venue, dtype: object"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndf['Venue'] #The area of the matches happened"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "4f37d86a-9d87-4c3e-a601-7d2d7fe2ae13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11            Sunrisers Hyderabad \n",
       "12    Royal Challengers Bengaluru \n",
       "13            Sunrisers Hyderabad \n",
       "14            Sunrisers Hyderabad \n",
       "15                 Mumbai Indians \n",
       "16                 Gujarat Titans \n",
       "17                 Gujarat Titans \n",
       "18            Sunrisers Hyderabad \n",
       "19               Rajasthan Royals \n",
       "20                 Mumbai Indians \n",
       "Name: winner, dtype: object"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ndf['winner'] #the winner teams "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "id": "cae8c11a-b19b-4f2e-af8a-3607e3edda59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sunrisers Hyderabad  has won the match for  47 runs in Rajiv Gandhi International Stadium on 21/04/2026\n",
      "Royal Challengers Bengaluru  has won the match for  18 runs in Wankhede Stadium on 12/04/2026\n",
      "Sunrisers Hyderabad  has won the match for  33 runs in Rajiv Gandhi International Stadium on 06/05/2026\n",
      "Sunrisers Hyderabad  has won the match for  5 wickets in Sawai Mansingh Stadium on 25/04/2026\n",
      "Mumbai Indians  has won the match for  6 wickets in Wankhede Stadium on 04/05/2026\n",
      "Gujarat Titans  has won the match for  77 runs in Sawai Mansingh Stadium on 09/05/2026\n",
      "Gujarat Titans  has won the match for  89 runs in Narendra Modi Stadium on 21/05/2026\n",
      "Sunrisers Hyderabad  has won the match for  5 wickets in Sawai Mansingh Stadium on 25/04/2026\n",
      "Rajasthan Royals  has won the match for  6 wickets in Maharaja Yadavindra Singh International Cricket St on 28/04/2026\n",
      "Mumbai Indians  has won the match for  6 wickets in Wankhede Stadium on 04/05/2026\n"
     ]
    }
   ],
   "source": [
    "for i,j,k,l in zip(ndf['winner'],ndf['run/wicket'],ndf['Venue'],ndf['Date']): # using for loop and f string we created a report of the match for the understanding\n",
    "    print(f'{i} has won the match for {j} in {k} on {l}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "361d3cd0-1578-49b7-8264-7e58cc563d03",
   "metadata": {},
   "source": [
    "#### COLLECTED THE DATA THROUGH WEB SCRAPPING AND HENCE THE PROJECT HAS BEEN COMPLETED"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
