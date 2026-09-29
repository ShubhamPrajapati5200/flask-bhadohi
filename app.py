from flask import Flask, request
import os
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
if __name__ == "__main__":
    app.run(host=0.0.0.0", port=int(os.environ.get("PORT",5000)))
