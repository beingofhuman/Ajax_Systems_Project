class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def click_element(self, id):
        self.driver.find_element_by_id(id).click()
