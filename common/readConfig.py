import os
import codecs # 专门用作编码转
import configparser  # 读取配置文件模块

#获取该文件的真实路径,然后分割路径和文件名存入一个元祖
# 获取路径方法一
proDir = os.path.split(os.path.realpath(__file__))[0]
print(proDir)

# 获取路径方法二
# proDir = os.getcwd()
# print(proDir)

#获取上层目录
parDir = os.path.dirname(proDir)
# print(proDir)

configPath = os.path.join(parDir,"config.ini")
# print(configPath)

class ReadConfig(object):
    def __init__(self):
        # 第一步：实例化configparser对象
        self.cf = configparser.ConfigParser()
        # 第二步：调用read方法读取该文件（传参：文件路径和编码格式）
        self.cf.read(configPath,encoding="utf-8-sig")

    #获取配置文件中的分组（eg:EMAIL）中的对应选项(eg:name)的值
    def get_email(self,name):
        # 第三步：获取某某section下的配置，name相当于key
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

if __name__ == '__main__':
    c = ReadConfig()
    print(c.get_email('mail_user'))