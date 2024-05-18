import csv
import requests
import re
import json
date_list = []
wfsy_list = []
nhly_list = []
for page in range(1,30) :

    # 这是你请求的JSONP服务的URL
    url = f'https://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183030076578433811973_1714478067514&fundCode=003042&pageIndex={page}&pageSize=40&startDate=&endDate=&_=1714478067543'
    # 防爬伪装
    headers = {

    'Cookie':'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; qgqp_b_id=be30aae3c9ad17e47ac1f5cd7e3e6cb0; EMFUND0=null; EMFUND9=04-19%2023%3A14%3A48@%23%24%u4EA4%u94F6%u88D5%u9686%u7EAF%u503A%u503A%u5238A@%23%24519782; websitepoptg_api_time=1714473657127; Eastmoney_Fund=003042_000001_000011; EMFUND8=04-30 19:53:32@#$%u4EA4%u94F6%u6D3B%u671F%u901A%u8D27%u5E01A@%23%24003042',
    'Host':'api.fund.eastmoney.com',
    'Referer':'https://fundf10.eastmoney.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',

    }

    # 发送GET请求
    res = requests.get(url, headers = headers)

    # 检查请求是否成功
    if res.status_code == 200:
        # JSONP响应文本
        data = res.text  # 更正变量名以反映其内容

        # 正则表达式匹配JSONP中的JSON部分
        obj = re.compile(r'jQuery183030076578433811973_1714478067514\((?P<json>.*?)\)')

        # 使用search方法查找匹配项，并从命名组'json'中获取JSON字符串
        match = obj.search(data)

        if match:
            content = match.group('json')  # 提取JSON字符串

            # 现在您可以解析JSON字符串为Python对象
            json_data = json.loads(content)
            for data1 in json_data['Data']['LSJZList']:
                date = data1['FSRQ']
                wfsy = data1['DWJZ']
                nhly = data1['LJJZ']
                date_list.append(date)
                wfsy_list.append(wfsy)
                nhly_list.append(nhly)
                #调试用
               # print(f'日期{date}，万份收益{wfsy}, 年化利率{nhly}')
                #调试用
           # print(json_data)
        else:
            print('No JSONP data found.')
    else:
        print('Failed to retrieve JSONP data.')
res.close



# 要写入的数据列表:
total_list = [
    date_list,
    wfsy_list,
    nhly_list
              ]
# 标题列表：
head_list = ['日期', '万份收益', '年化利率']
#  打开文件用于写入
# 写入CSV文件
with open('../extra project/output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(head_list)  # 写入标题行
    for date, wfsy, nhly in zip(date_list, wfsy_list, nhly_list):
        writer.writerow([(date, wfsy, nhly)])  # 写入数据行

