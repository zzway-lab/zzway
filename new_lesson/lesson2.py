#除了url,其他任何输入的数据必须以字典形式输入
# import requests
import pprint #更加明显显示如jmeter一样的内容
# url_api = "http://8.129.91.152:8766/futureloan/member/login"
# api_data = {
#   "mobile_phone":"15815541767",
#   "pwd":"lemon123456",
  # "type":"1",
  # "reg_name":"lllllemon"
# }
# head = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# repsons = requests.post(url=url_api,json=api_data,headers=head)
# print(repsons.json())
# pprint.pprint(repsons.json())
# res = repsons.json()#这里面的就是我们要的包含结果的数据
# recharge(方式一）
# import requests
# import pprint #更加明显显示如jmeter一样的内容
# url_api_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# member_id_recharge = res["data"]["id"]#这样子取是指取单一的元素
# token = res["data"]["token_info"]["token"]#这样子取是指取单一的元素
# api_data_recharge = {
#   "member_id": member_id_recharge,
#   "amount": 6000
# }
# head_charge = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer "+ token}
# repsons = requests.post(url=url_api_recharge,json=api_data_recharge,headers=head_charge)
# # print(repsons.json())
# pprint.pprint(repsons.json())
# ------------------------------------------------------------------------------------------------------------
# recharge(方式二）使用jsonpath
# import requests
# import pprint #更加明显显示如jmeter一样的内容
# import jsonpath
# url_api_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# member_id_recharge = jsonpath.jsonpath(res,"$.data.id")[0]#这样子取是指列表形式 #可直接（res,"$..id)去取任意一次
# token = jsonpath.jsonpath(res,"$.data.token_info.token")[0]#这样子取是指列表形式 #可直接（res,"$..id)去取任意一次
# api_data_recharge = {
#   "member_id": member_id_recharge,
#   "amount": 6000
# }
# head_charge = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer "+ token}
# repsons = requests.post(url=url_api_recharge,json=api_data_recharge,headers=head_charge)
# # print(repsons.json())
# pprint.pprint(repsons.json())

# 访问百度的请求--------扩展内容
#1.不是正确的页面---爬虫 --- 反爬机制
#2.乱码 --- 手动解码
import requests
baidu_url = "https://www.baidu.com/s"
param = {"wd":"sona大小姐"}
head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
response = requests.get(url=baidu_url,headers=head,params =param)
# print(response.text)#自动解码页面--不能解码成功--再换另一种方法
print(response.content.decode("utf8"))#手动指定解码




