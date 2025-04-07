

# To run this file type "python -m streamlit run app.py" in Anaconda termial visit this folder and the n tyype this


import streamlit as st
import pandas as pd
import pickle
import requests


movies_list = pickle.load(open("../models/movies_list.pkl",'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('../models/similarity.pkl','rb'))


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data =response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    recommended_movies = []
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    temp = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])
    posters=[]
    for i in range(1,6):
        movie_id=(movies.iloc[temp[i][0]].id)
        # fetch poster from api
        posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[temp[i][0]].title)
    return recommended_movies,posters

st.title('Recommender')
selected_movie = st.selectbox(
    "Select you movie",
    movies['title'].values)
    
if st.button("Recommend"):
    recommended_movies,posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(recommended_movies[0])
    with col2:
        st.image(posters[1])
        st.text(recommended_movies[1])

    with col3:
        st.image(posters[2])
        st.text(recommended_movies[2])
    with col4:
        st.image(posters[3])
        st.text(recommended_movies[3])
    with col5:
        st.image(posters[4])
        st.text(recommended_movies[4])

