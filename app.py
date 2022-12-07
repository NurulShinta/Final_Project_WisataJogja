# import pycaret
# import sklearn
from model_ds import Predik
from flask import Flask, render_template, request
import pandas as pd
# from pycaret.classification import *
#
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index_model.html')

@app.route("/predict", methods=["POST"])
def predict():
    # menangkap data yang diinput user melalui form
    Rating = float(request.form['Rating'])
    Ulasan = int(request.form['Ulasan'])
    rata2_tiket = int(request.form['rata2_tiket'])

    # melakukan prediksi menggunakan model yang telah dibuat
    data= [[Rating, Ulasan, rata2_tiket]]
    # new_data = pd.DataFrame(data, columns=['Rating','Ulasan','rata2_tiket'])
    Tempat, Tipe = Predik(data)
    return render_template('index_model.html', rec_str=Tipe, rec=Tempat)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)