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
        self.driver.get(self.url)

    def get_links_to_mp3(self):
        links_to_mp3 = {}
        elements = self.driver.find_elements_by_xpath(
            '//*[starts-with(@id, "mCSB_") and contains(@id, "_container")]/div[*]/ul/li[2]/a')

        for element in elements:
            audio_url = element.get_attribute('href')
            date_published = re.search('cast(.*).mp3', audio_url).group(1)
            links_to_mp3[date_published] = audio_url
        return links_to_mp3

    def get_links_to_podcast(self):
        links_to_podcast = []
        elements = self.driver.find_elements_by_xpath(
            '//*[starts-with(@id, "post")]/h3/a')

        for element in elements:
            podcast_url = element.get_attribute('href')
            print(podcast_url)

    def get_current_episode_number(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/div[2]/div[1]/div/div[2]/h1/a').text
        # remove first 9 characters e.g. EPISODE #818 will be just 818
        lates_episode_number = element[9:]
        return lates_episode_number


SGU_scrype().get_current_episode_number()
# links = SGU_scrype().get_links_to_mp3()
# for k, v in links.items():
#     print('{} : {}'.format(k, v))


# "https://www.theskepticsguide.org/podcasts/episode-817"
