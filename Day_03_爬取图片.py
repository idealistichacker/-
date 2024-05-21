# 1.拿到主页面源代码，从中找到图片的url地址。
# 2.拿到图片的url地址后，下载图片到本地。
# 3.将图片保存到本地的时候，要注意文件的命名问题，最好是用图片的url地址命名，这样不会重复。
import requests
from bs4 import BeautifulSoup
import re
import time
# 目标网站的url
url = 'https://www.16personalities.com/ch/%E7%B1%BB%E5%9E%8B%E6%8F%8F%E8%BF%B0'
# 添加请求头处理网站的反爬虫机制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Cookie': '16personalities_session=eyJpdiI6Im9TcGhMckxjamdCeC9GaWNJd2FZM0E9PSIsInZhbHVlIjoiYmdmVHdVY2pZaCtzY0xLenhmalpHdEFkdjl0RnZFT3VuTTNvS3BKR1AwSjExUjV4TVVmUk13Z0FQbUJvaVBxOTdOSE1FNk5UQVlMbXJ0d0x5MVZPbUYrNGV5dHlGZGJ5TXpvRUFyLzVGM1Axa0xaSUVSd1kxeFpOTkV2dVZTQ1MiLCJtYWMiOiI5NjRkMTNjMjc3ODY4ZjkzYTQ4YmZiYmIwY2QxNzI3YThjNTdkYTFjNDg3ZDVmNmMzZDMxZWZkYzU2NjliNjhlIiwidGFnIjoiIn0%3D; testResults=eyJpdiI6IjdrWm1zU05UaVhmd0Jnb2gvQlZlcHc9PSIsInZhbHVlIjoic0RKM1J6dVlLK29CMlc0YnFrNmhIVTcwTWlKT2lKUmtFWkl0TkNPQ1dqWkxYWWhrdTlUM2lUUVhEL3dPa1gzNiIsIm1hYyI6Ijk2Njc5NmNkODg3NzE1OWY0NzdkZTk5MjQzNDA5OWIwMTVkMDAyZTdlODNmNjE3YTYwZWI4MTA3MzZmYmNmZjAiLCJ0YWciOiIifQ%3D%3D; DTbCCclQo13dQF37DFy9N3HoxmSCrWYgnsRt4Xem=eyJpdiI6InBRRHAvYkdLdG82TzVlclR3ZmVWdUE9PSIsInZhbHVlIjoiZk4wa1pUTVhKcHB4eUszOG1GTXA3OHFtSDJTZTJiNjB3U1Y2V1o4Z0pydW0ySmpBTW54b0E0UU96RFV1U2lrVWRqQW9lSUQza0lVNnVTdWg3bG9kZ2ZjY21pSHFKeXFpVktEWEVIaGM2T21zc0VScHdyRjFBa3VvV2ZkRzlyQkt1c3FvZE8rUjU2YXllaTZDcmdZdFJuUDN5OEcrZ1pqb21ZRm1SUEVZSGJtR0NNQ3JsTG1hanRqMHNVWEhsUE9NY2xtRmF3K3haNVB4UXYxaDZ3b0VaVDNGSitwditManJiS0kxc29rNW9jUU9HYVV3ZDVQNkdQcWlIL1lNNVo5ZlZYd1RLWGN5ZHdvK0tRZkxMVlB6VHZmakU0SEJyN3BPcllINWZaaG5tQlI4K0tVblhBMzV6dUk0eU5SNXRzQ0F3dFovTkZDTG5PemhCTTdOL212UW5FWi9GWDBVY05aWFk5SWxKY3lkWDNCbWFYMmhRMmNaTVFhQTcrZDM0cHd3Q1ozcmRrSUxOcGI0MWc4WVhjMmFodGVTWUZudVhFZldQaGFtWlVkQVdkNGtkRTBVV2FuM3dFTHBkZ3pJOGJRWGttNXdGS3lOM1VGTDdEM1BtOWdGTWF3b1dtc1d5K0xFWkN2bXF6TDNyamU5d1JVbXFkbXhnZ2NCNk54Y1Vob0dscFovcGRZUnlGU1NQNEoySTEwWk8rOURVUUZ1RU5wVzdHc3RPS0ZmNjlzRVlnbDl2ZWJwbmhGR3dmMmlrK2VGKzZYVk92eS8vd1Z3MExEckhrNTZHWkIvaU9LcENHbE1hMlVmczBpa3BseHAxMDJ2Snp6b1ViejZFYUJJZWRQMkUvWHhxMkFwUTBzbSs2QTlwWUFtMStGK3dDR3A4RUt2QU0xS21GWUVPdEk0alQvV1JlVE5CM2xvNTJOeXFMZ2pLQU1ieTJhSmZZcUlPcjIzUlZpNzdjWXlYUGJTK3FnWldUcUFhRWVWRm5CbnNOY21CaDBNOXd1WGdlKzRNOG10U3dYdmtoZFNLemUyK2JQWS81d3ZqN0RHMXVITFBNYVYySmx4MWVjRGtzNFkvbzg3QWV0ZVFvclBsZnB6bGxXYTBoQXBaYlo0bTM1QWZBdDFxNkY0QW1JcVRJZ2tHeU03L1I3b1hjdmRUV0tjb2dpZ3YxSDRadUZJSmpNMi84N1ZwTHlMTituN3ZTN1g5RXFrOGNDVzFlYjgyaUFGd29kOHR6SjhiQU1KYWJTN2lSU2RFT0tMYktkYi92RzV4NUhUbWtnU3FxRThIRXoxUUh2WEYxaEVSSEE1akcxVFJuUmlDaUthZjJFY1hqdmJOczhBNEFnenc4Z0ladWU1ZXo4Rjc4TkViNmNSMVVvWFBYYXUvd1JSWjVqR2luSDhBUjR5TEZTOC80WDloMHNUdWFSR0xIZ1hUZUgvOVJzRWpTQnlmU0FhREhjbnBiak1qWTkxREJuN3VMc0VBSFRmMERCVm5odlRjWjNHeVNldWlCN0tGLzBad1V0OWhNQzlWdnV4ZHl4azZJeTBsa0VNTEp3OUZIazVSRHpESURmb05SL3lwK2VyRzhpUHNSNG8vWHQ2aVV5RVcyaXpXYXVPdVY0OVVVSU1LSGkvNWRhKzdBYVJEQWhyVDBwKzc0aENZVGY4blAzSGhtaU1JbzFJMmk3MkRQcy9DNG1RcU00R25DVTZKOW1CN2R1M0Z4TEZJcUdRRzl1a25CS0gwT0owMHU4U1FnbCsyYlBjdGo0PSIsIm1hYyI6IjYxOTE1NzQzNTgyNjYyNjMwODNjMTBmMjNlZDc5OWU1MWIyMWZiZDFmNWMxZTA4MzJlYzA4NGIyOWEwNDkzMzUiLCJ0YWciOiIifQ%3D%3D',
    'Referer': 'https://www.16personalities.com/ch/%E7%B1%BB%E5%9E%8B%E6%8F%8F%E8%BF%B0',
}
# 发送GET请求
res = requests.get(url, headers = headers)
# 检查请求是否成功
if res.status_code == 200:
    res.encoding = 'utf-8' # 设置编码格式,防止乱码
    # 使用BeautifulSoup解析HTML，找到.svg图片的URL
    soup = BeautifulSoup(res.text,'html.parser')
    img_url_list = soup.find_all('img', {'class': 'image'})
# 下载图片
    #用for循环拿到每个svg图片的url地址
    for img_url in img_url_list:
        # 发送GET请求下载图片
        img_res = requests.get(img_url['src'], headers = headers)
        # 检查请求是否成功
        if img_res.status_code == 200:
            # 从URL中提取文件名
            img_name = re.search(r'[^/]*$', img_url['src']).group()
            # 将图片保存到本地
            with open(img_name, 'wb') as img_file:
                img_file.write(img_res.content)
            print(f'图片已保存到{img_name}')
            # 休眠1秒，防止请求过于频繁对目标服务器造成破坏，而被封IP
            time.sleep(1)
        else:
            print('下载图片失败')
