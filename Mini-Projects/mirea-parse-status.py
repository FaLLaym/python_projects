from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")
options.add_argument("--headless")

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}


driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

kws = ['ИКБ', 'ИИТ']
blklst = ['40.05.01', '38.05.01', '12.03.01', '10.05.05']

def get_title_links() -> list:
    arr = []
    entry_link = 'https://priem.mirea.ru/accepted-entrants-list/'
    driver.get(entry_link)

    div_element = driver.find_element(By.CSS_SELECTOR, 'div#rates.rates')
    table_element = div_element.find_element(By.CSS_SELECTOR, 'table#ratesTable')
    tbody_elements = table_element.find_elements(By.CSS_SELECTOR, 'table#ratesTable tbody')

    for tbody_element in tbody_elements:
        tb = tbody_element.text
        if any(x in tb for x in kws) and (not(any(x in tb for x in blklst))):
            trs = tbody_element.find_elements(By.CSS_SELECTOR, 'tr.rowCommon')
            for tr in trs:
                td = tr.find_element(By.CSS_SELECTOR, 'td.competitionListing')
                a = td.find_element(By.CSS_SELECTOR, 'a.showListingBtn')
                href = a.get_attribute('href')
                if href:
                    #print(f'{tb[:8]} -> {href}')
                    arr.append(href)
    return arr


def get_result() -> None:
    for link in get_title_links():
        driver.get(link)

        name = driver.find_element(By.TAG_NAME, 'h1').text.split('Текущий конкурс')[1][1:]
        last_place = driver.find_element(By.XPATH, '/html/body/div/div[1]/p[1]').text.split('Всего мест — ')[1]
        div_element = driver.find_element(By.CSS_SELECTOR, 'div#names.names')
        table_element = div_element.find_element(By.CSS_SELECTOR, 'table.namesTable')
        tbody_elements = table_element.find_elements(By.CSS_SELECTOR, 'table.namesTable tbody')

        for tbody in tbody_elements:
            bigArr = tbody.text.split('\n')
            for _ in bigArr:
                miniArr = _.split(' ')
                if miniArr[0] == last_place:
                    print(f'Имя направления: {name} \n'
                        f'Снилс: {miniArr[1]} \n'
                        f'Приоритет: {miniArr[2]} \n'
                        f'Подан аттестат: {miniArr[3]} \n'
                        f'Баллы за ЕГЭ до ИД: {miniArr[-3]} \n'
                        f'Итоговые баллы: {miniArr[-1]} \n')




get_result()
driver.quit()