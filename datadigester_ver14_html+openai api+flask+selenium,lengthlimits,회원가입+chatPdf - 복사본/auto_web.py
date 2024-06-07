import os
import time

from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def create_datadigester_folder():
    c_drive = "C:\\"
    folder_name = "datadigester"
    count = 1
    while True:
        new_folder_name = f"{folder_name}_{count}" if count > 1 else folder_name
        new_folder_path = os.path.join(c_drive, new_folder_name)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
            print(f"'{new_folder_name}' 폴더가 성공적으로 생성되었습니다.")
            break
        count += 1
    return new_folder_path

def set_download_path(download_dir):
    download_path = os.path.join(download_dir, "downloads")
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    print(f"다운로드 경로 '{download_path}'가 설정되었습니다.")
    return download_path

def download_pdf_and_extract_text(query):
    download_dir = create_datadigester_folder()
    download_path = set_download_path(download_dir)
    
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://scholar.google.co.kr/schhp?hl=ko')

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'pdf')]")
    
    for link in pdf_links:
        href = link.get_attribute('href')
        driver.get(href)
        time.sleep(5)  # Ensure files are fully downloaded

    driver.quit()

    downloaded_files = [f for f in os.listdir(download_path) if f.endswith('.pdf')]
    pdf_texts = [extract_text_from_pdf(os.path.join(download_path, f)) for f in downloaded_files]

    combined_text = "\n".join(pdf_texts)
    return combined_text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() or '' for page in reader.pages])
        return text

if __name__ == "__main__":
    query = input("검색어를 입력하세요: ")
    pdf_text = download_pdf_and_extract_text(query)
    print(pdf_text)