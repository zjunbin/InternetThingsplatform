#  coding utf-8
# @time      :2019/6/12 16:59
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :orgmanagement.py
class org_data:
    success_data = {"txtPcNumber":"CZPCS12","txtPcName":"长庄警务室","drpAreas":"崇礼区","drpPLType":"普通类型"}

    error_data = {{"txtPcNumber":"","txtPcName":"常庄派出所","drpAreas":"东城区","drpPLType":"普通类型","excepted":"派出所编号不能为空!"},
                  {"txtPcNumber": "PLCA112", "txtPcName": "", "drpAreas": "东城区", "drpPLType": "管理类型", "excepted": "派出所名称不能为空!"},
                  {"txtPcNumber": "PLCA112", "txtPcName": "acccbd", "drpAreas": "东城区", "drpPLType": "普通类型", "excepted": "派出所名称必须为中文!"},
                  {"txtPcNumber": "PLCA112", "txtPcName": "常庄派出所", "drpAreas": "", "drpPLType": "", "excepted": "请选择区域部门类型!"},
                  {"txtPcNumber": "德州派出所", "txtPcName": "德州派出所", "drpAreas": "管理类型", "drpPLType": "", "excepted": "派出所编号只能含有数字,字母和下划线!"},
                  }