# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on user selection. Built with Streamlit, pandas, and TMDB API integration for fetching movie posters.

## Features

- Recommends top 5 movies similar to the user's choice.
- Displays movie posters alongside recommendations.
- User-friendly interface with a dropdown selection.

## Prerequisites

- Python 3.7+
- TMDB API key (optional - [Get here](https://www.themoviedb.org/documentation/api))
- Required Python packages: `streamlit`, `pandas`, `requests`, `pickle`

## Installation

1. Clone the repository:

````bash
git clone https://github.com/rushabhlathiya/Movie-Recommendation-System.git
cd Movie-Recommendation-System

```bash
pip install streamlit pandas requests
````

## Usage

Ensure the project structure matches:

```bash
movie-recommender/
├── app.py
└── models/
    ├── movies_list.pkl
    └── similarity.pkl
```

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

Select a movie from the dropdown and click "Recommend" to see results.

## Project Structure

app.py: Main application code
models/: Contains preprocessed data files
movies_list.pkl: Movie titles and IDs dataset
similarity.pkl: Precomputed similarity matrix

API Integration
The app uses TMDB API to fetch movie posters. An API key is included in the code, but you can replace it with your own by modifying:

```bash
response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=YOUR_KEY_HERE...")
```

## License

Distributed under the MIT License. See LICENSE for more information.

## Acknowledgments

Movie data from TMDB API

Dataset preprocessing with scikit-learn

Streamlit for UI components

```bash
Note: Replace "yourusername" in the clone URL with your actual GitHub username. For a complete deployment, ensure:
1. You include actual pickle files or provide instructions to generate them
2. Add a LICENSE file if needed
3. Consider adding screenshots in a `images/` directory if demonstrating UI
```
