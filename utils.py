import config
import pickle
import json
import numpy as np

class MovieRevenuePredictor:
    def __init__(self,Movie_Name,Release_Period,Whether_Remake,Whether_Franchise,Genre,New_Actor,New_Director,New_Music_Director,Lead_Star,Director,Music_Director,Number_of_Screens,Budget_INR):
        self.Movie_Name        = Movie_Name
        self.Release_Period    = Release_Period
        self.Whether_Remake    = Whether_Remake
        self.Whether_Franchise = Whether_Franchise
        self.Genre             = Genre
        self.New_Actor         = New_Actor
        self.New_Director      = New_Director
        self.New_Music_Director= New_Music_Director
        self.Lead_Star         = Lead_Star
        self.Director          = Director
        self.Music_Director    = Music_Director 
        self.Number_of_Screens = Number_of_Screens
        self.Budget_INR        = Budget_INR
    def load_data(self):
        with open (config.model_path,'rb') as f:
            self.movie_model = pickle.load(f)
        with open (config.encoded_data_path,'r') as f:
            self.encoded_data = json.load(f)
    def predict(self):
        self.load_data()
        details = np.zeros(len(self.encoded_data['columns']))

        details[0] = self.encoded_data['Release_Period'][self.Release_Period]
        details[1] = self.encoded_data['Whether_Remake'][self.Whether_Remake]
        details[2] = self.encoded_data['Whether_Franchise'][self.Whether_Franchise]
        details[3] = self.encoded_data['New_Actor'][self.New_Actor]
        details[4] = self.encoded_data['New_Director'][self.New_Director]
        details[5] = self.encoded_data['New_Music_Director'][self.New_Music_Director]
        details[6] = self.Number_of_Screens
        details[7] = self.Budget_INR
        genre_index = self.encoded_data['columns'].index('Genre_' + self.Genre)
        details[genre_index] = 1
        lead_index  = self.encoded_data['columns'].index('Lead Star_' + self.Lead_Star)
        details[lead_index]  = 1
        direc_index = self.encoded_data['columns'].index('Director_' + self.Director)
        details[direc_index] = 1
        music_index = self.encoded_data['columns'].index('Music Director_' + self.Music_Director)
        details[music_index] = 1

        revenue = self.movie_model.predict([details])[0]
        return revenue



        





