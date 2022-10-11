from flask import Flask,request,render_template
import config
from utils import MovieRevenuePredictor
import numpy as np

app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def get_revenue():
    if request.method == 'POST':
        data = request.form
        Movie_Name         = data['Movie Name']
        Release_Period     = data['Release Period']
        Whether_Remake     = data['Whether Remake']
        Whether_Franchise  = data['Whether Franchise']
        Genre              = data['Genre']
        New_Actor          = data['New Actor']
        New_Director       = data['New Director']
        New_Music_Director = data['New Music Director']
        Lead_Star          = data['Lead Star']
        Director           = data['Director']
        Music_Director     = data['Music Director']  
        Number_of_Screens  =  int(data['Number of Screens'])
        Budget_INR         =  int(data['Budget INR'])
        predictor = MovieRevenuePredictor(Movie_Name, Release_Period, Whether_Remake, Whether_Franchise, Genre, New_Actor, New_Director, New_Music_Director, Lead_Star, Director, Music_Director, Number_of_Screens, Budget_INR)
        revenue = predictor.predict()
        return f"Movie,{Movie_Name}, can generate '\u20B9' {np.around(revenue,3)} of revenue"
    else:
        data = request.args
        Movie_Name         = data.get('Movie Name')
        Release_Period     = data.get('Release Period')
        Whether_Remake     = data.get('Whether Remake')
        Whether_Franchise  = data.get('Whether Franchise')
        Genre              = data.get('Genre')
        New_Actor          = data.get('New Actor')
        New_Director       = data.get('New Director')
        New_Music_Director = data.get('New Music Director')
        Lead_Star          = data.get('Lead Star')
        Director           = data.get('Director')
        Music_Director     = data.get('Music Director')  
        Number_of_Screens  = int(data.get('Number of Screens'))
        Budget_INR         = int(data.get('Budget INR'))
        predictor = MovieRevenuePredictor(Movie_Name, Release_Period, Whether_Remake, Whether_Franchise, Genre, New_Actor, New_Director, New_Music_Director, Lead_Star, Director, Music_Director, Number_of_Screens, Budget_INR)
        revenue = predictor.predict()
        return f"Movie,{Movie_Name}, can generate '\u20B9' {np.around(revenue,3)} of revenue"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.port_no)