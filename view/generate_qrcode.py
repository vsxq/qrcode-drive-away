
from  flask import Blueprint,render_template,request,jsonify,redirect,session
from  util.util_code import virtual_64hex 
from util.util_qrcode import make_qrcode
code_class = virtual_64hex()
generate_qrcode_bp = Blueprint("generate_qrcode",__name__)


@generate_qrcode_bp.route("/address_img")
def show():

    if "tel" in request.args:
        _c = request.args["tel"]
        code_64 = code_class.encrypt(_c)
        if(code_64):
            _c = int(_c)
            img_name = make_qrcode(tel=_c, code=code_64)
            session["telephone"]=_c

            return jsonify({"img_name": img_name})
        else:
            return redirect("/")
    else:
        redirect("/")