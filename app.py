from selenium import webdriver
import time
import urllib.request

search = "고양이"
fileName = "cat_image"
number = 30
interval = 0.2

driver = webdriver.Chrome("./chromedriver")
driver.get(
    f"https://www.google.com/search?q={search}&tbm=isch&hl=ko&tbs=il:ol&sa=X&ved=0CAAQ1vwEahcKEwigpLGVq_7xAhUAAAAAHQAAAAAQAg&biw=1126&bih=682"
)
firstImage = driver.find_element_by_css_selector(
    "#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img"
)
firstImage.click()

for i in range(number):
    try:
        time.sleep(interval)
        image = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img")
        imageSrc = image.get_attribute("src")
        urllib.request.urlretrieve(imageSrc, f"{fileName}_{i+1}.jpg")
    except:
        print(f"{i+1}번째 이미지 저장 오류 발생!")
    else:
        print(f"{i+1}번째 이미지 저장 성공!")
    finally:
        nextButton = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.mWagE.fDqwl > a:nth-child(4)")
        nextButton.click()

driver.quit()
