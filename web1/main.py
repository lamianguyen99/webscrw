'''
import time
from playwright.sync_api import sync_playwright
import os

# Tạo thư mục profile nếu chưa tồn tại
profile_dir = 'my_profile'
os.makedirs(profile_dir, exist_ok=True)

with sync_playwright() as p:
    # Khởi động trình duyệt với context trống
    browser = p.chromium.launch_persistent_context(
        user_data_dir=profile_dir,  # Đường dẫn đến thư mục profile
        headless=True, # Chạy ở chế độ không ẩn
        slow_mo=500
    )
    
    cookies=input('Do you want clear cookies? Y/N')
    if cookies.lower() == "y":
        # Xóa các cookie và bộ nhớ cache
        browser.clear_cookies()
        browser.clear_permissions()
        browser.set_geolocation({'longitude': 0, 'latitude': 0})  
        print('clear cookies')    
    
    # Mở một trang mới với User-Agent
    page = browser.new_page()
    page.goto('http://demo73v2.ninavietnam.org/xaydungdangtuan_1674824/admin')
    print(page.content())
    time.sleep(200)
    # Đóng trình duyệt
    browser.close()

'''
import json
import requests
from lxml.etree import tostring
from lxml import html
response = requests.get('https://shopsuatramanh.com/')

with open ('filex.html', 'w', encoding='utf8') as file:
  file.write(str(response.text))

tree = html.fromstring(response.text)

links = tree.xpath("//ul[@class='menu-product']/li")

dsx = []

for link in links:
  outer_html = tostring(link, encoding='unicode')
  tree2 = html.fromstring(outer_html)
  print(outer_html+ '\n+===========+')
  ds1 = link.xpath('(.//a)[1]')[0].text_content()
  print(ds1)
  ds2_paths = tree2.xpath("//li/ul/li")
  ds = {}
  arr = []
  print(len(ds2_paths))
  #for ds2_path in ds2_paths:
  #  ds2 = ds2_path.xpath('(.//a)[1]')[0]
  #  print(' ' + ds2.text_content() +'\n')
  #  arr_in_ds2 = []
  #  next_ds2 = ds2_path.xpath('.//ul/li')
    #for child_ds2 in next_ds2:
    #  child = child_ds2.xpath('(.//a)[1]')[0].text_content()
    #  print('   ' + child +'\n')
    
  ds[ds1] = arr
  dsx.append(ds)

with open('ds_file.json','w', encoding="utf-8") as file:
  json.dump(dsx, file, ensure_ascii=False, indent=4)
n=input(response.status_code)

