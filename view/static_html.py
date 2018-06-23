from flask import Flask,Blueprint,render_template,request,abort

static_html_bp = Blueprint("static_html",__name__)
@static_html_bp.route("/success")
def response_success_html():

    return render_template("success.html")
@static_html_bp.route("/about_us")
def response_about_us():
    return render_template("about_us.html")
@static_html_bp.route("/cheduzi")
def cheduzi():
    if "code" in request.args:
        print(request.args["code"])
        return render_template("cheduzi.html",code = request.args["code"])
    else:
        abort(404)
@static_html_bp.route("/")
def response_root_path():
    return render_template("index.html")
