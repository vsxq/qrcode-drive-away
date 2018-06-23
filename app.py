from flask import Flask,render_template
from view.generate_qrcode import generate_qrcode_bp
from view.scan_qrcode import scan_bp
from view.search_record import search_record_bp
from view.static_html import static_html_bp
from config import base_url
def create_app():
    app = Flask(__name__)
    app.secret_key = "1772441"
    app.register_blueprint(generate_qrcode_bp)
    app.register_blueprint(scan_bp)
    app.register_blueprint(search_record_bp)
    app.register_blueprint(static_html_bp)

    @app.errorhandler(404)
    def page_not_food(e):
        return render_template("404.html",base_url = base_url)
    return app



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
