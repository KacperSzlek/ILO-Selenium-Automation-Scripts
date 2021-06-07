from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
profile = webdriver.FirefoxProfile()
capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities['acceptSslCerts'] = True
profile.set_preference("security.ssl3.dhe_rsa_aes_128_sha", True)
profile.set_preference("security.ssl3.dhe_rsa_aes_256_sha", True)
profile.set_preference("app.normandy.startupRolloutPrefs.security.tls.version.min", 1)
profile.set_preference("security.tls.insecure_fallback_hosts", '***********')
#profile.set_preference("security.warn_leaving_secure", False)
#profile.set_preference("security.warn_leaving_insecure", False)
#profile.set_preference("browser.aboutConfig.showWarning", False)
browser = webdriver.Firefox(executable_path="./drivers/geckodriver", firefox_profile=profile)
browser.get('***********')
sleep(10)
searchInput = browser.find_element_by_name('UN')
searchInput.send_keys('***********')
searchInput = browser.find_element_by_name('PW')
searchInput.send_keys('***********')
button = browser.find_element_by_name('LI')
button.click()
browser.switch_to_frame("dataframe")
button = browser.find_element_by_xpath('//input[@type="submit" and @value="Momentary Press"]')
button.click()
sleep(1)
popup = browser.switch_to.alert
sleep(1)
popup.accept()
sleep(1)
browser.quit()
