from flask import Flask, request
app  = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        naam = request.form.get("naam")
        return f"<h1>Hello {naam}! Bhadohi me swagat hai!<h1><a href='/'>Wapas jao</a>"
    return """

        <h2>Naam likho</h2>
        <form method="POST">
            <input type="text" name="naam" placeholder="Apna naam likho">
            <button type="submit">Bhejo</button>
        </form>
    """    
app.run(debug=True)