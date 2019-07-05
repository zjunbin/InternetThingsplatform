#  coding utf-8
# @time      :2019/7/5 11:57
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :PopTracking_data.py

class PopTrackingData:

    success_data = [{"idCard":"","startTime":"","mstarttime":"","endtime":"","mendtime":""}]
    error_data = [{"idCard": "", "startTime": "2019-6-12", "mstarttime": "09:00", "endtime": "2019-6-12",
                   "mendtime": "12:00","applyCause":"以车找人","excepted":"身份证号不能为空！"},
                  {"idCard": "140430199404286812", "startTime": "2019-6-12", "mstarttime": "09:00", "endtime": "2019-6-12",
                   "mendtime": "12:00", "applyCause":"以车找人","excepted": "身份证号无效！"},
                  {"idCard": "sdfdsfasdfasdf2342", "startTime": "2019-6-12", "mstarttime": "09:00", "endtime": "2019-6-12",
                   "mendtime": "12:00", "applyCause":"以车找人","excepted": "身份证号无效！"},
                  {"idCard": "140430199404286810", "startTime": "", "mstarttime": "09:00", "endtime": "2019-6-12",
                   "mendtime": "12:00", "applyCause":"以车找人","excepted": "开始时间年月日不能为空"},
                  {"idCard": "140430199404286810", "startTime": "2019-6-12", "mstarttime": "09:00", "endtime": "",
                   "mendtime": "12:00", "applyCause":"以车找人","excepted": "结束时间年月日不能为空"},
                  {"idCard": "140430199404286810", "startTime": "2019-5-12", "mstarttime": "09:00", "endtime": "2019-6-13",
                   "mendtime": "12:00", "applyCause":"以车找人","excepted": "时间差不能超过30天！"},
                  {"idCard": "140430199404286810", "startTime": "2019-6-12", "mstarttime": "09:00", "endtime": "2019-6-12",
                   "mendtime": "12:00","applyCause":"", "excepted": "申请原因不能为空！"},
                  {"idCard": "140430199404286810", "startTime": "2022-6-12", "mstarttime": "09:00",
                   "endtime": "2022-6-12","mendtime": "12:00", "applyCause": "", "excepted": "输入时间不能大于当前时间！"}]


