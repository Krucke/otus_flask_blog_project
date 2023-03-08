from flask import Blueprint, render_template, request, url_for, redirect, flash
from http import HTTPStatus
user_app = Blueprint("user_app", __name__)
from models import db
from models.model import User



@user_app.post('/signup')
def signup():
    print(request.form)
    return 'ok'



# @product_app.get("/")
# def product_list():
#     # products = Product.query.all()
#     # print('prods', products)
#     return 'ok'
#     return render_template('products/index.html', products=products)


# @product_app.route('/create_product', methods=['GET', 'POST'], endpoint='create_product')
# def create_product():
#     form = ProductForm()
#     if request.method == "GET":
#         return render_template('products/create_product.html', form=form)

#     # if not form.validate_on_submit():
#     #     return render_template('products/create_product.html', form=form), HTTPStatus.BAD_REQUEST
#     # name = form.name.data
#     # product = Product(name=name)
#     # db.session.add(product)
#     # db.session.commit()
#     # url = url_for('product_app.detail', product_id=product.id)
#     # flash('product '+str(product.id)+' created')
#     # return redirect(url)
#     return render_template('products/create_product.html', form=form)

# @product_app.get("/<int:product_id>", endpoint='detail')
# def product_detail(product_id):
#     return {"product_id": product_id}