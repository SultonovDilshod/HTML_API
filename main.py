from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("home.html")

@app.route('/api/v1/<station>/<date>')
def api_data(station, date):
    df = pd.read_csv("")
    temperature = df.station(date)
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route('/home/')
def home():
    return render_template("tutorial.html")

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
