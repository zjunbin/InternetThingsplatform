#  coding utf-8
# @time      :2019/5/2011:05
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :main.py.py

import pytest

pytest.main(["--html=output/res.html","--alluredir=output/my_reports","--reruns","2",
             "--reruns-delay","5"])