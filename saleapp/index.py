import math
from flask import render_template, request
from . import dao
from . import app



@app.route("/")
def index():
    q= request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")

    pages = math.ceil(dao.count_product() / app.config["PAGE_SIZE"])
    products = dao.load_products(q,cate_id,page)

    return render_template("index.html", products=products,pages=pages)



@app.route("/products/<int:id>")
def product_details(id):
    p = dao.get_product_by_id(id)
    return render_template("product-detail.html",p=p)

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)