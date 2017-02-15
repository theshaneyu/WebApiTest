import requests

res = requests.post('http://140.120.13.243:6655/cut/', data = {'sen':'高效的框架不僅是網站設計的基礎，它提供的各種豐富多彩的功能，還提高整體的功能和性能。一個網站的外觀和設計完全可以通過一些完美和可靠的工具而徹底改頭換面。現在，越來越多的網頁設計師和編輯人員選擇使用 CSS 框架來創建網站。'})

# print(res.json())

for item in res.json():
    print(item, end = ' ')
