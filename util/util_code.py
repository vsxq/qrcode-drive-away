import string
import re
import math



def is_number(s):
    try:
        int(s)
        return True
    except BaseException:
        pass
    return False

class virtual_64hex(object):
    __instance=None
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,system =64):
        # 生成指定的64字符串
        if system > 1:

            virtual_hex = re.findall(r".{4}", "".join(
                [string.ascii_uppercase, "#", string.ascii_lowercase[::-1], ")", string.digits]))[::-1]
            _frist = "".join(virtual_hex[::2])[::-1]
            _end = "".join(virtual_hex[::-2])

            self.code = (_frist+_end)[0:system]
            self.decrypt_code = {v: i for i, v in enumerate(self.code)}
            self.system = system
            print(self.system)
        else:
            print("params error,force exit")
            exit()
    
    def is_virtual_64hex(self, s):
        for i in s:
            if i not in self.code:
                return False
        return True
    
    def encrypt(self, test_str):
        # 转为任意进制为 num = num
        if(is_number(test_str)):
            l = []
            _c = int(test_str)
            status = True
            while(status):
                _c,remainder = divmod(_c,self.system)
                l.append(self.code[remainder])
                if(_c == 0):
                    status = False
            return "".join(l)
        else:
            return None

    def decrypt(self, test_str):
        if(self.is_virtual_64hex(test_str)):
            sum = 0
            for i, v in enumerate(test_str):
                sum = self.decrypt_code[v] * math.pow(self.system, i)+sum
            return int(sum)
        else:
            return None


