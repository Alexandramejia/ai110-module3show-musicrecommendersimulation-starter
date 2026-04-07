from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read a songs CSV and return a list of dicts with numeric fields cast to int/float."""
    import csv
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Award points for genre/mood matches and numerical proximity to user targets; return (score, reasons)."""
    score = 0.0
    reasons = []

    # Categorical matches
    if song['genre'] == user_prefs.get('favorite_genre'):
        score += 2.0
        reasons.append('genre match (+2.0)')

    if song['mood'] == user_prefs.get('favorite_mood'):
        score += 1.0
        reasons.append('mood match (+1.0)')

    # Numerical proximity: 1 - abs(song_val - target_val), scaled by weight
    energy_weight = user_prefs.get('energy_weight', 1.5)
    energy_contrib = (1 - abs(song['energy'] - user_prefs.get('target_energy', 0.5))) * energy_weight
    score += energy_contrib
    reasons.append(f'energy score (+{energy_contrib:.2f})')

    valence_weight = user_prefs.get('valence_weight', 0.5)
    valence_contrib = (1 - abs(song['valence'] - user_prefs.get('target_valence', 0.5))) * valence_weight
    score += valence_contrib
    reasons.append(f'valence score (+{valence_contrib:.2f})')

    dance_weight = user_prefs.get('danceability_weight', 0.5)
    dance_contrib = (1 - abs(song['danceability'] - user_prefs.get('target_danceability', 0.5))) * dance_weight
    score += dance_contrib
    reasons.append(f'danceability score (+{dance_contrib:.2f})')

    # Tempo: normalize difference over a 200 BPM range
    tempo_contrib = max(0.0, 1 - abs(song['tempo_bpm'] - user_prefs.get('target_tempo_bpm', 120)) / 200.0) * 0.3
    score += tempo_contrib
    reasons.append(f'tempo score (+{tempo_contrib:.2f})')

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song in the catalog using score_song and return the top k results sorted highest to lowest."""
    scored = [
        (song, score, ', '.join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
