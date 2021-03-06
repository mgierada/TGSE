from selenium import webdriver
import json
import re
import os


class SGU_scrape():
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

    def get_publication_date_list(self):
        publication_date_list = []
        elements = self.driver.find_elements_by_xpath(
            '//*[starts-with(@id, "mCSB_") and contains(@id, "_container")]/div[*]/ul/li[2]/a')

        for element in elements:
            audio_url = element.get_attribute('href')
            date_published = re.search('cast(.*).mp3', audio_url).group(1)
            publication_date_list.append(date_published)
        return publication_date_list

    def get_latest_episode_number(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/div[2]/div[1]/div/div[2]/h1/a').text
        # remove first 9 characters e.g. EPISODE #818 will be just 818
        lates_episode_number = element[9:]
        return int(lates_episode_number)

    def get_all_podcasts_data(self):
        podcast_info = {}
        publication_date_list = self.get_publication_date_list()
        latest_episode_number = self.get_latest_episode_number()

        for date, ep in zip(
                publication_date_list,
                reversed(range(1, latest_episode_number))):

            link_to_mp3 = 'https://media.libsyn.com/media/skepticsguide/skepticast{}.mp3'.format(
                date)
            link_to_podcast = 'https://www.theskepticsguide.org/podcasts/episode-{}'.format(
                ep)

            inner_dict = {'date_published': date,
                          'link_to_mp3': link_to_mp3,
                          'link_to_podcast': link_to_podcast}
            podcast_info[ep] = inner_dict
        return podcast_info

    def get_json(self, json_fname='all_podcasts_data.json'):
        podcast_info = self.get_all_podcasts_data()

        path_to_json_dir = os.path.join(os.getcwd(), 'source')
        os.makedirs(path_to_json_dir, exist_ok=True)
        path_to_json = os.path.join(os.getcwd(), 'source', json_fname)

        with open(path_to_json, 'w') as f:
            json.dump(podcast_info, f, indent=4)


if __name__ == '__main__':
    SGU_scrape().get_json()
