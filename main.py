from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           name="Akriti Jha",
                           roll="12345")   # change roll number

app.run(host='0.0.0.0', port=81)