from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome("./chromedriver")
driver.get(
    "https://www.google.com/search?q=고양이&tbm=isch&hl=ko&tbs=il:ol&sa=X&ved=0CAAQ1vwEahcKEwigpLGVq_7xAhUAAAAAHQAAAAAQAg&biw=1126&bih=682"
)
firstImage = driver.find_element_by_css_selector(
    "#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img"
)
firstImage.click()

time.sleep(0.2)

image = driver.find_element_by_css_selector(
    "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img"
)
imageSrc = image.get_attribute("src")
urllib.request.urlretrieve(imageSrc, "cat_image.jpg")

time.sleep(10)
driver.quit()
