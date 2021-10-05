from sqlite3.dbapi2 import connect
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import sqlite3


def saveing_data(youtube_count, twitter_count, insta_count):
    record = {
        'date_time': str(datetime.now()),
        'youtube': youtube_count,
        'twitter': twitter_count,
        'instagram': insta_count
    }

    # connect to sqlite
    connection = sqlite3.connect('shg_followers.db')
    curs = connection.cursor()
    curs.execute(''' CREATE TABLE IF NOT EXISTS shg_stats(
        date_time TEXT,
        youtube INTEGER,
        twitter INTEGER,
        instagram INTEGER
    ) ''')

    insert = curs.execute(
        'insert into shg_stats values ("%s",%s,%s,%s)' % (
            record['date_time'], record['youtube'], record['twitter'], record['instagram']
        )
    )
    connection.commit()
    connection.close()


# instance and setup webdriver
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path='./geckodriver', options=options)
driver.implicitly_wait(10)

# youtube
driver.get('https://www.youtube.com/channel/UC6Oowe4rpbQXo6AmRHmDMYg')
youtubecount = int(driver.find_element_by_id(
    'subscriber-count').text.split(' ')[0])

# twitter
driver.get('https://twitter.com/MoonlightLuke')
twitter_count = int(driver.find_element_by_css_selector(
    'a[href="/MoonlightLuke/followers"] > span > span').text)

# instagram
driver.get('https://www.picuki.com/profile/lukepeterscodes')
insta_count = int(driver.find_element_by_css_selector('.followed_by').text)


saveing_data(youtubecount,twitter_count,insta_count)

# close webdriver
driver.close()
