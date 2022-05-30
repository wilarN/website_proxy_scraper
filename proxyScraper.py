from selenium import webdriver
import time
import sys
import os
from datetime import datetime

abc = str.maketrans('/', '-')
global_output_file = "./output/proxy_list_output"


cur_time = datetime.now()
dt_string = cur_time.strftime("%d/%m/%Y %H/%M/%S")
dt_string = dt_string.replace(" ", "")
dt_string = dt_string.translate(abc)


def scrape(scrape_type: str):
    if not os.path.exists('./output'):
        os.makedirs('./output')
    url = f'https://openproxy.space/list/{scrape_type}'
    browser = webdriver.Chrome()
    browser.get(url)
    log_file = open(global_output_file + "_" + dt_string + ".txt", "a+")
    log_file.write(browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/section[4]/textarea').get_attribute("value"))
    log_file.close()

    browser.quit()


def main():
    what_to_scrape = input("HTTP/HTTPS[HTTP], SOCKS4[S4], SOCKS5[S5]")
    time.sleep(0.5)
    if what_to_scrape.lower() == "http":
        scrape("http")
    elif what_to_scrape.lower() == "s4":
        scrape("socks4")
    elif what_to_scrape.lower() == "s5":
        scrape("socks5")
    else:
        print("Please input a valid proxy type...")
        sys.exit(0)


if __name__ == '__main__':
    main()
