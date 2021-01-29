from new_lesson import practicing
# cases = practicing.data_abstract("test_case_api.xlsx","register")
# for case in cases:
#     url_ = case['url'] #多键值中取值时需明确到取哪个值
#     data_ = case['data']
#     data_ = eval(data_)
#     expected_result_ = case['expected_result']
#     expected_result_ = eval(expected_result_)
#     expected_msg = expected_result_["msg"]
#     real_result = practicing.register_auto(url= url_,register_data= data_)
#     real_msg = real_result.get("msg")
#     cases_id = case['case_id']
# # print(real_result)
#     print(real_msg)
#     if real_msg == expected_msg:
#         final_result = "passed"
#         print("第%s测试用例执行通过"%(cases_id))
#     else:
#         final_result = "failed"
#         print("第%s测试用例执行失败"%(cases_id))
#     print('*'*105)
#     data_writting_ = practicing.data_writting("test_case_api.xlsx","register",final_result,cases_id+1,8)
#重新做 -------------------------------------------------------------------------------------------------------------------
from new_lesson import practicing
def executed_command(filename,sheetname):
    case1 = practicing.data_abstract1(filename,sheetname)
    for a in case1:
        url1 = a["sheet1_url"]
        data1 = a["sheet1_data"]
        data1 = eval(data1)
        expected_result_1 = a["sheet1_expection"]
        expected_result_1 = eval(expected_result_1)
        expected_msg = expected_result_1["msg"]
        data_input = practicing.function_display(url = url1,function_data= data1)
        real_result1 = data_input["msg"]
        case_id_1 = a["case_id1"]
        # print(real_result1)
        if real_result1 == expected_msg:
            data_return = "passed"
            print("第%s条用例实测通过"%(case_id_1))
            print("*" * 120)
        else:
            data_return = "failed"
            print("第%s条用例实测失败" % (case_id_1))
            print("*" * 120)
        practicing.data_writting1(filename,sheetname,case_id_1+1,8,data_return)

# executed_command("test_case_api.xlsx","register")


