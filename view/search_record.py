from flask import  Blueprint, jsonify, request,render_template,session
from util.util_sql import util_sql
import config
sql = util_sql()
search_record_bp = Blueprint("search_record", __name__)


@search_record_bp.route("/search_data")
def search_record():
    return_json = {"results": None}
    status = ""
    if "tel" in request.args and "Invitation_code" in request.args:
        if request.args["Invitation_code"] != config.Invitation_code:
            print(request.args["Invitation_code"])
            status = "fatal"
        else:
            status = "success"
            return_json["results"] = sql.select(request.args["tel"])
           # print(return_json["results"])
            if return_json["results"]!=None:
                for i in return_json["results"]:
                
                    i["ip"]=i["ip"][:-1]+"*"
    else:
        status = "error"
    return_json["status"]=status
    return jsonify(return_json)
@search_record_bp.route("/search")
def search():
    telephone=""
    Invitation_code=""
    if "telephone" in session:
        telephone = session["telephone"]
    if config.debug:
        Invitation_code = config.Invitation_code
    return render_template("record.html",telephone=telephone,Invitation_code=Invitation_code)