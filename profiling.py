import pandas as pd
from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file

df = pd.read_csv('data/dataset.csv')

profile = ProfileReport(df, title="Spotify Dataset")
profile.to_file("spotify_tracks.html")