from flask import Flask, render_template, request, redirect, flash
from logic import getAllCards, addCard, deleteCard, searchCard
from database import get_connection, create_tables

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def home():
    cards = getAllCards()
    return render_template("index.html", cards=cards)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        cardName = request.form["cardName"]
        cardID = request.form["cardID"]
        quantity = request.form["quantity"]
        location = request.form["location"]
        
        if cardName == "" or cardID == "":
            flash("Please enter a valid card name and card number.")
            return redirect("/add")
        
        addCard(cardName, cardID, quantity, location)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete", methods=["POST"])
def delete():
    cardName = request.form["cardName"]
    cardID = request.form["cardID"]
    
    deleteCard(cardName, cardID)
    
    return redirect("/")

@app.route("/search", methods=["GET", "POST"])
def search():
    cards = []
    
    if request.method == "POST":
        cardName = request.form["cardName"]
        cardID = request.form["cardID"]
        
        cards = searchCard(cardName, cardID)
    
    return render_template("search.html", cards=cards)

if __name__ == "__main__":
    app.run(debug=True)
   