import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)


# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# SQLite
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # If add-to-cart button is clicked

        # get donut name
        donut_name = request.form.get("donut_name")

        # donut information from SQL table
        donut_info = db.execute("SELECT name, src, price FROM donuts WHERE name = ?", donut_name)

        donut_name = donut_info[0]["name"]
        donut_src = donut_info[0]["src"]
        donut_price = donut_info[0]["price"]

        # Insert the donut into cart
        donutExists = db.execute("SELECT name FROM cart WHERE name = ?", donut_name)

        # if donut is not in the cart yet, insert the donut with quantity 1
        if not donutExists:
            db.execute("INSERT INTO cart (name, src, price, qty) VALUES (?, ?, ?, ?)", donut_name, donut_src, donut_price, 1)
        # if donut is already in the cart, no need to insert, increase quantity by 1, increase price
        else:
            currentQty = db.execute("SELECT qty FROM cart WHERE name =?", donut_name)
            currentQty = currentQty[0]["qty"]
            currentQty += 1
            db.execute("UPDATE cart SET qty = ? WHERE name = ?", currentQty, donut_name)
            newPrice = currentQty * 3
            db.execute("UPDATE cart SET price = ? WHERE name = ?", newPrice, donut_name)
        # trigger alert
        return """
            <script>
                alert("Donut added to your cart!");
                window.location.href = "/";
            </script>
        """


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method == "GET":
        # render cart page (prices, quantity, etc.)
        cartList = db.execute("SELECT * FROM cart")
        cartLength = len(cartList)
        subTotal = db.execute("SELECT SUM(qty) FROM cart")
        subTotal = subTotal[0]["SUM(qty)"]
        totalPrice = 0
        if not subTotal:
            subTotal = 0
        else:
            subTotal = subTotal * 3
            totalPrice = subTotal
            totalPrice = totalPrice + (totalPrice * 0.1)
            totalPrice = f"{totalPrice:.2f}"

        return render_template("cart.html", cartlist=cartList, items=cartLength, subtotal=subTotal, total=totalPrice)
    else:
        # if X (remove 1 donut) gets clicked
        donut_name = request.form.get("donut_name")
        currentQty = db.execute("SELECT qty FROM cart WHERE name =?", donut_name)
        currentQty = currentQty[0]["qty"]
        # if there is only 1 donut, delete donut from SQL table
        if currentQty <= 1:
            db.execute("DELETE FROM cart WHERE name = ?", donut_name)
        # if there are more than 1 donuts, reduce quantity by 1, reduce price
        else:

            currentQty = currentQty - 1
            db.execute("UPDATE cart SET qty = ? WHERE name = ?", currentQty, donut_name)
            newPrice = currentQty * 3
            db.execute("UPDATE cart SET price = ? WHERE name = ?", newPrice, donut_name)

        return redirect("/cart")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        # if send message gets clicked
        return redirect("/contact")