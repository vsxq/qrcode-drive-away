from flask import Blueprint, request, session, render_template, jsonify
from util.util_code import virtual_64hex
from util.sms import send_sms
from util.util_sql import util_sql
from captcha.image import ImageCaptcha
from datetime import datetime
import random
import base64
import string
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(2)
sql = util_sql(
)

code_class = virtual_64hex()
image = ImageCaptcha()
scan_bp = Blueprint('scan_qrcode', __name__)


def send_sms_event(telephone):
    send_sms(telephone)


# 异步事件
def insert_sql_event(telephone, ip):
    date = datetime.now()
    sql.insert(tel=telephone, date=date, ip=ip)


def generate_captcha():
    code = "".join(random.sample(string.digits, 4))

    data = image.generate(code).getvalue()
    c = "data:image/png;base64,"+str(base64.b64encode(data), "utf-8")
    return code, c


# 获取验证码


@scan_bp.route("/captcha")
def captcha_code():
    captcha_code, captcha_img = generate_captcha()
    session["captcha"] = captcha_code
    return captcha_img

# 扫码二维码主页面


@scan_bp.route("/scan")
def scan():
    if "code" in request.args:
        code = request.args["code"]

        session["telephone"] = code_class.decrypt(code)
        return render_template("scan.html")
    else:
        return "访问异常,非法访问,你的ip{}我们已经记录下来".format(request.remote_addr)


@scan_bp.route("/check")
def check():
    value = ""
    if "captcha" in session:
        if "captcha" in request.args:
            if request.args["captcha"] == session["captcha"]:
                if "telephone" in session:
                    telephone = str(session["telephone"])
                    if (len(telephone) == 11 and telephone.isdigit()):
                        # 异步事件
                        ip = request.remote_addr
                        executor.submit(send_sms_event, telephone)
                        executor.submit(insert_sql_event, telephone, ip)
                        value = "success"
                    else:
                        value = "fail"

    if value == "":
        value = "error"
    return jsonify({"code": value})
