import requests
import json

# url = "https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html"
#
# url = "https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal"
#
#
#
#
# data = {"locale":"en","zoneId":"1","districtId":"5","estateId":"2153","blockId":"nil,8973,804","floor":"4","flat":"B"}
#
#
# data_json = json.dumps(data)
# headers = {}
# result = requests.post(url = url, data = data_json, headers= headers)
#
# # r = requests.post(url, data=json.dumps(payload), headers=headers)
#
# print(result)
# print(result.content)
# print(result.text)

# {"responseInfo":{"reasons":[],"correlationId":null},"localFields":null,"extensions":[],"propAddr":"Flat 1,5/F,Block/Tower A,Abba House,Aberdeen/Ap Lei Chau,Hong Kong","valn":"4690000","grossFloorArea":"405","saleableArea":"304","propAge":35,"valnDt":"2018-10-01 12:42:26 +0000"

with requests.Session() as c:
    # headers = {"referrer" : "https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html"}
    headers ={'Content-Type': 'application/json','User-Agent': 'Safari/537.36'}

    url = "https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal"
    data = {"locale":"en","zoneId":"1","districtId":"5","estateId":"2153","blockId":"nil,8973,804","floor":"4","flat":"B"}
    result = requests.post(url, json=json.dumps(data), headers=headers)
    page = requests.get("https://www.hsbc.com.hk/personal/mortgages/property-valuation-tool.html")
    # page2 = requests.get("https://www.hsbc.com.hk/gpib/channel/proxy/mortgageSvc/enqPropVal")
    # print(page.content)
    # print(page2.content)
    # print(page2)
    print(result.headers)
    print(result.status_code)
    print(result.content)
    print(result.text)
