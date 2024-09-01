from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options)

urls = [
    "https://www.tiket.com",
    "https://www.tokopedia.com",
    "https://www.orangsiber.com",
    "https://demoqa.com/",
    "https://www.automatetheboringstuff.com"
]

options.add_argument("--start-minimized")

for url in urls:
    driver.get(url)
    print(f"{url.split('//')[1]} - {driver.title}")

driver.quit()