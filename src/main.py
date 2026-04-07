"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile — categorical preferences
    user_prefs = {
        "favorite_genre":      "indie pop",
        "favorite_mood":       "happy",

        # Numerical targets (0.0–1.0 unless noted)
        "target_energy":       0.75,
        "target_valence":      0.80,
        "target_danceability": 0.78,
        "target_acousticness": 0.30,
        "target_tempo_bpm":    118,

        # Scoring weights (must sum to 1.0)
        "energy_weight":       0.30,
        "mood_weight":         0.25,
        "genre_weight":        0.20,
        "valence_weight":      0.15,
        "danceability_weight": 0.10,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  TOP RECOMMENDATIONS")
    print(f"  Profile: {user_prefs['favorite_genre']} / {user_prefs['favorite_mood']}")
    print("=" * 50)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        print(f"    Score : {score:.2f}")
        print(f"    Genre : {song['genre']}  |  Mood: {song['mood']}")
        reasons = explanation.split(', ')
        print(f"    Why   : {reasons[0]}")
        for reason in reasons[1:]:
            print(f"            {reason}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
