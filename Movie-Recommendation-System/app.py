
import os
import pickle
import requests
import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="CineMagic | Movie Recommendations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. COLORFUL CUSTOM DESIGN
# ==========================================
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #10002b 0%,
        #240046 40%,
        #3c096c 75%,
        #10002b 100%
    );
    color: #ffffff;
}

/* Main content width */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Main heading */
.hero-title {
    text-align: center;
    font-size: 58px;
    font-weight: 900;
    letter-spacing: 2px;
    background: linear-gradient(
        90deg, #ff4ecd, #b794ff, #55e7ff, #ff4ecd
    );
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}

.hero-subtitle {
    text-align: center;
    color: #e0c3fc;
    font-size: 18px;
    margin-top: 8px;
    margin-bottom: 25px;
}

.hero-banner {
    background: linear-gradient(
        120deg,
        rgba(255, 78, 205, 0.18),
        rgba(85, 231, 255, 0.12)
    );
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 24px;
    padding: 28px 20px;
    margin-bottom: 25px;
}

/* Labels */
.stSelectbox label {
    color: #f3d9ff !important;
    font-size: 17px !important;
    font-weight: 700 !important;
}

/* Select box */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #2d1454;
    color: white;
    border: 1px solid #c77dff;
    border-radius: 12px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    min-height: 50px;
    font-size: 17px;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #ff4ecd, #8c52ff);
    transition: 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #55e7ff, #8c52ff);
    color: white;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(199, 125, 255, 0.35);
}

/* Movie captions */
.stCaption {
    color: #f3d9ff !important;
}

/* Divider */
hr {
    border-color: rgba(255,255,255,0.2);
}

/* Info and warning messages */
div[data-testid="stAlert"] {
    border-radius: 14px;
}

/* Movie images */
div[data-testid="stImage"] img {
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Section heading */
h2, h3 {
    color: #ffffff !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #cdb4db;
    font-size: 13px;
    padding: 25px 0 5px 0;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. LOAD RECOMMENDATION MODEL
# ==========================================
@st.cache_resource
def load_model():
    with open("movie_data.pkl", "rb") as file:
        return pickle.load(file)


try:
    movies, cosine_sim = load_model()
except FileNotFoundError:
    st.error(
        "movie_data.pkl was not found. "
        "Place it in the same folder as app.py."
    )
    st.stop()
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()


# ==========================================
# 4. RECOMMEND SIMILAR MOVIES
# ==========================================
def get_recommendations(title):
    matches = movies.index[
        movies["title"] == title
    ].tolist()

    if not matches:
        return movies.iloc[0:0][["title", "movie_id"]]

    idx = matches[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores.sort(key=lambda item: item[1], reverse=True)

    movie_indices = [
        movie_index
        for movie_index, score in sim_scores
        if movie_index != idx
    ][:10]

    return movies.iloc[movie_indices][
        ["title", "movie_id"]
    ]


# ==========================================
# 5. TMDB API SETTINGS
# ==========================================
API_KEY = "caebf0f00d8296320b250339cb8d658a"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


# ==========================================
# 6. FETCH MOVIE POSTERS
# ==========================================
@st.cache_data(ttl=86400)
def fetch_poster(movie_id, movie_title):
    if not API_KEY:
        return None
    try:
        # 1. Try by ID
        r = requests.get(f"https://api.themoviedb.org/3/movie/{int(movie_id)}", params={"api_key": API_KEY}, timeout=10)
        if r.status_code == 200 and r.json().get("poster_path"):
            return IMAGE_BASE_URL + r.json()["poster_path"]
        
        # 2. Try by Title Search
        s = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": API_KEY, "query": str(movie_title)}, timeout=10)
        results = s.json().get("results", [])
        for movie in results:
            if movie.get("poster_path"):
                return IMAGE_BASE_URL + movie["poster_path"]
    except Exception:
        return None
    return None


# ==========================================
# 7. COLORFUL HERO SECTION
# ==========================================
st.markdown("""
<div class="hero-banner">
    <h1 class="hero-title">🎬 CINEMAGIC</h1>
    <p class="hero-subtitle">
        Your next favorite movie is waiting.
        Discover something magical to watch ✨
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 8. MOVIE SELECTION
# ==========================================
movie_titles = sorted(
    movies["title"].dropna().unique().tolist()
)

if not movie_titles:
    st.error("No movie titles found in your dataset.")
    st.stop()

st.markdown("### 🍿 Find Your Next Movie")

selected_movie = st.selectbox(
    "Choose a movie you love",
    movie_titles
)

st.write("")

if st.button("✨ Discover Similar Movies"):

    recommendations = get_recommendations(selected_movie)

    st.markdown(
        f"## 💜 Movies similar to **{selected_movie}**"
    )

    if recommendations.empty:
        st.warning("No recommendations found for this movie.")

    else:
        # Display up to five movies per row
        for start in range(0, len(recommendations), 5):
            row = recommendations.iloc[start:start + 5]
            cols = st.columns(5)

            for col, (_, movie) in zip(cols, row.iterrows()):
                with col:
                    with st.container(border=True):
                        movie_title = movie["title"]
                        movie_id = movie["movie_id"]

                        poster_url = fetch_poster(
                            movie_id,
                            movie_title
                        )

                        if poster_url:
                            st.image(
                                poster_url,
                                use_container_width=True
                            )
                        else:
                            st.markdown(
                                """
                                <div style="
                                    height:220px;
                                    display:flex;
                                    align-items:center;
                                    justify-content:center;
                                    text-align:center;
                                    padding:10px;
                                    border-radius:12px;
                                    background:linear-gradient(
                                        135deg,#7209b7,#f72585
                                    );
                                    color:white;
                                    font-size:18px;
                                    font-weight:bold;
                                ">
                                    🎞️<br>Poster unavailable
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        st.markdown(
                            f"""
                            <div style="
                                text-align:center;
                                color:#f3d9ff;
                                font-weight:700;
                                padding-top:10px;
                                min-height:55px;
                            ">
                                {movie_title}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


# ==========================================
# 9. API KEY NOTICE
# ==========================================
if not API_KEY:
    st.warning(
        "TMDB API key is not configured. "
        "Recommendations work, but real movie posters "
        "require your API key."
    )


# ==========================================
# 10. FOOTER
# ==========================================
st.markdown("""
<div class="footer">
    MADE WITH 💜 PYTHON & STREAMLIT
    <br>
    Movie recommendations powered by content-based filtering
</div>
""", unsafe_allow_html=True)
