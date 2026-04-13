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

    profiles = [
        # ── Standard profiles ──────────────────────────────────────────
        ("indie pop / happy (original)", {
            "favorite_genre":      "indie pop",
            "favorite_mood":       "happy",
            "target_energy":       0.75,
            "target_valence":      0.80,
            "target_danceability": 0.78,
            "target_acousticness": 0.30,
            "target_tempo_bpm":    118,
            "energy_weight":       0.30,
            "valence_weight":      0.15,
            "danceability_weight": 0.10,
        }),
        ("Alex — High-Energy Pop Listener", {
            "favorite_genre":      "pop",
            "favorite_mood":       "happy",
            "target_energy":       0.90,
            "target_valence":      0.85,
            "target_danceability": 0.90,
            "target_acousticness": 0.08,
            "target_tempo_bpm":    130,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
        ("Maya — Chill Lofi Listener", {
            "favorite_genre":      "lofi",
            "favorite_mood":       "chill",
            "target_energy":       0.35,
            "target_valence":      0.58,
            "target_danceability": 0.60,
            "target_acousticness": 0.80,
            "target_tempo_bpm":    75,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
        ("Marcus — Deep Intense Rock Listener", {
            "favorite_genre":      "rock",
            "favorite_mood":       "intense",
            "target_energy":       0.92,
            "target_valence":      0.45,
            "target_danceability": 0.65,
            "target_acousticness": 0.08,
            "target_tempo_bpm":    152,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
        # ── Adversarial / edge-case profiles ──────────────────────────
        # No rock+sad song exists — genre weight (+2) should beat mood (+1)
        ("Jordan — High Energy + Sad Mood (Conflicting)", {
            "favorite_genre":      "rock",
            "favorite_mood":       "sad",
            "target_energy":       0.90,
            "target_valence":      0.20,
            "target_danceability": 0.55,
            "target_acousticness": 0.12,
            "target_tempo_bpm":    145,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
        # Reggae is not in the catalog — no song ever earns the genre bonus
        ("Riley — Reggae Fan (No Genre Match in Catalog)", {
            "favorite_genre":      "reggae",
            "favorite_mood":       "happy",
            "target_energy":       0.65,
            "target_valence":      0.75,
            "target_danceability": 0.80,
            "target_acousticness": 0.40,
            "target_tempo_bpm":    95,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
        # All targets at 0.5 — no directional pull, only one ambient song exists
        ("Sam — Perfectly Neutral (All Targets = 0.5)", {
            "favorite_genre":      "ambient",
            "favorite_mood":       "chill",
            "target_energy":       0.50,
            "target_valence":      0.50,
            "target_danceability": 0.50,
            "target_acousticness": 0.50,
            "target_tempo_bpm":    100,
            "energy_weight":       1.5,
            "valence_weight":      0.5,
            "danceability_weight": 0.5,
        }),
    ]

    for label, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print("  TOP RECOMMENDATIONS")
        print(f"  Profile: {label}")
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
