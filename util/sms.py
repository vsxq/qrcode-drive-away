from config import appid, appkey, template_id
from qcloudsms_py import SmsSingleSender  # 单发
import string
from qcloudsms_py.httpclient import HTTPError
import datetime


def send_sms(telephone):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在

    ssender = SmsSingleSender(appid, appkey)
    params = [nowTime]
    try:
        result = ssender.send_with_param(86, telephone,
                                         template_id, params)
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    print(result)
