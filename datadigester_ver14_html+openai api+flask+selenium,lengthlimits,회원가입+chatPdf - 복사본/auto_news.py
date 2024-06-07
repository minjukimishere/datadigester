import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def collect_news_titles(query):
    # 서비스 설정 및 드라이버 초기화
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    # URL 구성 및 페이지 로드
    url = f"https://search.naver.com/search.naver?where=newhit&ie=utf8&sm=nws_hty&query={query}"
    driver.get(url)
    time.sleep(3)  # 페이지 로드 대기
    
    # 뉴스 제목 수집
    news_titles = driver.find_elements(By.CSS_SELECTOR, "a.news_tit")
    titles = [title.text for title in news_titles]
    
    # 사용 완료 후 드라이버 종료
    driver.quit()
    
    return titles

if __name__ == "__main__":
    query = input("검색어를 입력하세요: ")
    news_titles = collect_news_titles(query)
    print("\n".join(news_titles))