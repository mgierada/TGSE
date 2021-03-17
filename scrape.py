from selenium import webdriver
import re


class SGU_scrype():
    def __init__(self):
        self.url = 'https://www.theskepticsguide.org/podcasts'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('headless')
        options.add_argument('--test-type')
        DRIVER_PATH = '/Users/maciejgierada/Desktop/literature_survey/chromedriver'

        self.driver = webdriver.Chrome(
            executable_path=DRIVER_PATH, options=options)

    def get_links(self):
        self.driver.get(self.url)

        links_to_audio_url = {}
        elements = self.driver.find_elements_by_xpath(
            '//*[@id="mCSB_1_container"]/div[*]/ul/li[2]/a')

        for element in elements:
            audio_url = (element.get_attribute('href'))
            date_published = re.search('cast(.*).mp3', audio_url).group(1)
            links_to_audio_url[date_published] = audio_url
        return links_to_audio_url


links = SGU_scrype().get_links()
for k, v in links.items():
    print('{} : {}'.format(k, v))
