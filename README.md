# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

This recommender works by taking what a user likes and comparing it to every song in the catalog. Each song gets a score based on how well it matches, and the top 5 results are returned with a short reason for each pick.

**Song features used in the system:**
- `genre` — the style of music (e.g. lofi, pop, rock, jazz)
- `mood` — the emotional feel (e.g. happy, chill, intense, moody)
- `energy` — how high-energy the song feels, from 0.0 to 1.0
- `valence` — how positive or upbeat it sounds, from 0.0 to 1.0
- `danceability` — how suited it is for dancing, from 0.0 to 1.0
- `acousticness` — how acoustic vs. produced it sounds, from 0.0 to 1.0
- `tempo_bpm` — the speed of the song in beats per minute

The system compares a user’s taste profile against every song in the catalog, scores each one, and returns the top 5.

**What the user profile stores:**
- Favorite genre and favorite mood
- Numerical targets for energy, valence, danceability, acousticness, and tempo

**How each song is scored:**
- Genre match adds 2 points — genre is weighted highest because it is the hardest preference boundary. If someone wants jazz, a rock song is a miss no matter how good the energy match is.
- Mood match adds 1 point — mood matters but is more forgiving than genre
- For each numerical feature, the system calculates `1 - abs(song_value - target_value)` and multiplies by a weight. Energy has the biggest weight (1.5) since it is the most immediately noticeable quality. Valence, danceability, acousticness, and tempo add smaller amounts on top.

**How recommendations are chosen:**
- Every song in the CSV gets scored
- They are sorted highest to lowest
- The top 5 are returned, each with a short explanation of why it ranked there

**Potential bias:** Genre has a strong pull in this system. A song in the right genre but wrong mood will usually outscore a song with the perfect mood but a different genre — meaning some good matches can get buried. With only 18 songs in the catalog, genres that appear just once (like country or metal) will almost always surface regardless of how poorly the rest of the features match.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tested six user profiles to evaluate the system. The high-energy pop listener got mostly pop results, though electronic and hip-hop songs crept in due to close energy scores. The chill lofi listener worked best — all three lofi songs ranked in the top three because the genre bonus and numerical targets reinforced each other. For the intense rock listener, a pop song with the "intense" mood label surprisingly outranked a metal song. The adversarial profile with high energy and a sad mood exposed a real weakness: the genre bonus outweighed the mood mismatch, so the top result was a rock song that was not sad at all. When I used a genre not in the catalog like reggae, no song earned the genre bonus and the rankings felt random. Finally, with all targets set to 0.5, the single ambient song dominated just because it was the only one to earn the genre bonus.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

- The catalog only has 18 songs, so the results feel repetitive fast. A few songs like Gym Hero and Rooftop Lights show up across multiple profiles just because no better option exists.
- Genre gets too much power. If your favorite genre is in the catalog, that song almost always wins — even if the mood or energy is a bad match.
- Acousticness is tracked but never used in scoring, so two people with totally different texture preferences will get the same results.
- If your genre is not in the catalog at all (like reggae), the system has nothing personal to offer and just guesses based on numbers.
- The system does not understand context. It cannot tell the difference between someone who wants chill background music while studying vs. someone who wants slow sad music to cry to — both might have similar settings but want very different things.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

Building this made me realize that a recommender is really just a point system in disguise. It does not actually "know" what good music is — it just adds up numbers based on rules you set. If you tell it genre is worth 2 points and mood is worth 1, it will follow that math every single time, even when the result feels wrong to a real person. The system is only as smart as the weights you give it, and small choices like making genre worth twice as much as mood end up shaping every single recommendation.

The bias part surprised me the most. I did not expect that a missing genre (like reggae) would give that user a totally different and worse experience than everyone else. Or that a song like Gym Hero — which is really made for working out — would keep showing up for people who just want happy background pop, just because it shares the "pop" label and has high energy. Real apps like Spotify probably have the same problem at a bigger scale, just hidden behind millions of songs. The more I looked at the results, the more I noticed the system was rewarding whatever was easy to measure, not whatever actually matched the vibe.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

---

## Screenshot outputs 

~ Phase 3 ~ 

The output showing the recommendations (song titles, scores, and reasons): 

![alt text](screenshots/image.png)


~ Phase 4 ~

The output for each profile's recommendations:

**Profile: Alex — High-Energy Pop Listener**

![Alex profile recommendations](screenshots/profile_Alex.png)

---

**Profile: Maya — Chill Lofi Listener**

![Maya profile recommendations](screenshots/profile_maya.png)

---

**Profile: Marcus — Deep Intense Rock Listener**

![Marcus profile recommendations](screenshots/profile_Marus.png)

---

**Profile: Jordan — High Energy + Sad Mood (Conflicting / Adversarial)**

![Jordan profile recommendations](screenshots/profile_Jordan.png)

---

**Profile: Riley — Reggae Fan (No Genre Match in Catalog)**

![Riley profile recommendations](screenshots/profile_Riley.png)

---

**Profile: Sam — Perfectly Neutral (All Targets = 0.5)**

![Sam profile recommendations](screenshots/profile_Sam.png)