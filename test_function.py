from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time 

def test_check_description(driver):
    driver.get("https://ylab.io")
    driver.find_element(By.XPATH, "//a[@href='/projects']").click()
    clickable = driver.find_element(By.XPATH, "//div[@class='ant-select-selector']//span[@title='Все стеки']")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .send_keys(Keys.ARROW_UP)\
        .perform()
    driver.find_element(By.XPATH, "//div[@class='rc-virtual-list-holder-inner']//div[@title='Java']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//p[contains(text(), 'Конструктор сервисов B2B')]").click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//div[@class='Project__rowInfo']//p")
    assert element.text == 'Включает такие сервисы как: электронный документооборот (ЭДО), проверка контрагентов, взыскание дебиторской задолженности и прочие.'
    driver.quit()