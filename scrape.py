from selenium import webdriver


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
        elements = self.driver.find_element_by_class_name(
            'ep-controls__button ep-controls__button--download button')
        for element in elements:
            print(element)


SGU_scrype().get_links()
