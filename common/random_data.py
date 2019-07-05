#  coding utf-8
# @time      :2019/6/12 17:14
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :random_data.py
import random, string


class RandomData:

    def StationNumber(self):
        num = string.ascii_letters + string.digits
        return "".join(random.sample(num, 10))

    def StationName(self):
        name = ''
        for i in range(6):
            val = random.randint(0x4e00, 0x9fbf)
            name += chr(val)
        print(name)

if __name__ == '__main__':

    c = RandomData().StationNumber()
    print(c)
    RandomData().StationName()