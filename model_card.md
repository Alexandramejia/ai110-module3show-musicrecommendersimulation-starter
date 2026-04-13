# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
SoulMusic 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

SoulMusic is a music recommender that suggests songs based on your mood, favorite genre, and how you want a song to feel — things like energy level, how danceable it is, and how fast or slow it should be. It generates a ranked list of the top 5 songs from the catalog that best match what you are looking for.

The system assumes the user already knows what kind of music they like and can describe it — it does not learn from listening history or past behavior. It also assumes there is a song in the catalog that is a reasonable match, which is not always true given how small the dataset is.

This app is meant for classroom exploration, not real users. It is a learning project built to understand how recommender systems work under the hood. It has known limitations — like a small catalog and genre bias — so it should not be used to actually guide someone's music taste in a real-world setting.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Every song in the catalog gets a score based on how well it matches what a user says they like. The system looks at genre, mood, energy, how danceable the song is, how positive it sounds (valence), and how fast it is (tempo). The user tells the system their favorite genre and mood, and also sets targets for energy, danceability, and tempo on a scale from 0 to 1.

Genre is worth the most — if a song matches your favorite genre it gets 2 bonus points right away. Mood match gives 1 bonus point. After that, the system checks how close each song's energy, danceability, and valence are to your targets. The closer the match, the more points it adds. Tempo is also checked but only adds a tiny amount.

Once every song is scored, they get sorted from highest to lowest, and the top 5 are shown with a short reason explaining why each one ranked where it did.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 18 songs stored in a CSV file. Each song has a genre, mood, and numerical values for energy, tempo, valence, danceability, and acousticness.

Genres included: pop, lofi, rock, indie pop, ambient, jazz, synthwave, hip-hop, country, classical, metal, r&b, blues, soul, and electronic. Moods included: happy, chill, intense, focused, moody, sad, relaxed, energetic, melancholic, angry, romantic, euphoric, and uplifting.

No songs were added or removed from the original dataset. The catalog is small and mostly covers mainstream western genres — it is missing reggae, Latin, K-pop, funk, and many others. It also only has one or two songs per genre, so variety within a genre is basically zero. The data reflects a pretty narrow slice of musical taste overall.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works best when a user has a clear and specific taste — someone who knows exactly what genre they want and has a strong energy preference. For example, Maya (chill lofi) and Marcus (intense rock) both got results that felt accurate right away because their preferences pointed clearly in one direction and matching songs existed in the catalog.

It also does a good job of showing its reasoning. Every recommendation comes with a breakdown of exactly why each song ranked where it did, which makes it easy to understand and spot when something feels off. That transparency is something a lot of real apps don't give you.

For users whose genre is well represented in the catalog, the top result is almost always a logical pick. The genre and mood bonuses together do a decent job of locking onto the right vibe quickly.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

**Findings from experiment:**

**Genre takes over everything.** If a song matches your favorite genre, it almost always lands at #1 — no matter what. Even if a song from a different genre is a way better fit for your energy or mood, it still loses. The system basically just picks your genre and stops thinking.

**Acousticness is collected but completely ignored.** The system asks how acoustic you like your music, and the songs even have that info — but the code never actually uses it. So it doesn't matter if you want soft acoustic guitar or heavy synths, the score comes out the same either way.

**Energy can drown out mood.** When we turned up the energy weight during the experiment, the system started recommending angry metal songs to a user who wanted sad music — just because the energy level happened to match. The system doesn't check if the vibe actually makes sense together.

**Too few songs means too little variety.** There are only 18 songs in the catalog, with about one or two per genre. If your favorite genre isn't in there at all (like reggae), the system has no idea what to do with you and just guesses based on numbers. That's a pretty unfair experience compared to someone whose genre is included.

**Tempo barely matters.** Tempo — how fast or slow a song is — is worth almost nothing in the final score compared to energy. So even if you want a slow, chill 70 BPM song and the system gives you something at 140 BPM, that huge difference barely changes the result.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**What I tested:**

I ran seven different listener profiles through the system to see if the results made sense.

The ones that worked fine were Alex (pop lover), Maya (lofi fan), and Marcus (rock fan). They all got songs that matched what they asked for, which felt right.

The weird ones were more interesting. Jordan wanted rock music but in a sad mood — there are sad songs in the list (a country one and a blues one), but no sad rock song. So the system gave Jordan a rock/intense song at #1 because the genre matched, then fell back on the country and blues sad songs for #2 and #3. The sad mood got answered, just not in the right genre. That felt a little off.

Riley wanted reggae, which is not in the list at all. The system had no idea what to do, so it just picked songs that had similar energy and speed. The songs were fine but not really reggae.

Sam had all their settings at 0.5 (perfectly in the middle) and ended up with sad country and blues songs in the bottom of the list — just because those songs happened to have energy close to 0.5. That was a surprise and didn't feel like a good fit.

When I changed the weights (made energy stronger, made genre weaker), the #1 song never changed for anyone. The system is pretty stubborn about its top pick.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

Since SoulMusic is still a classroom project with known bugs and limitations, there is a lot of room to grow. I would improve it by adding more music types, letting users save or build their own playlists from their results, and making tempo count more in the scoring so the speed of a song actually affects what gets recommended.

- **Add more music types.** The catalog only has 18 songs and is missing a lot of genres people actually listen to — like reggae, Latin, K-pop, and funk. Adding more variety would make SoulMusic feel less repetitive and more useful for people with different tastes.
- **Let users save and build playlists.** Right now the system just shows a list and that's it. It would be way more useful if users could save their top results, name a playlist, and come back to it later — more like how a real music app works.
- **Make tempo count more.** Tempo is almost ignored in the current scoring. Someone who wants slow chill music at 70 BPM should not be getting fast hype songs just because the energy matched. Giving tempo more weight would help SoulMusic understand the vibe better — like the difference between a study playlist and a workout playlist.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that this type of scoring algorithm is probably used in a lot of other apps and websites too — anything with a "recommended for you" feature is likely doing something similar, just with way more data. I also learned that the conditions and rules you set matter a lot depending on what kind of recommendation you are trying to make. Small decisions like how much weight to give genre vs. mood completely change what the user sees.

Something I found interesting was how diverse a single song can actually be. A pop song with a high tempo can still be sad, and a slow quiet song can feel happy — a lot of musical features can go in unexpected directions. That made me realize that labeling music with just one mood or genre is kind of an oversimplification, and a real recommender would need a lot more nuance to get it truly right.

**Profile Comparisons:** 

**Alex (High-Energy Pop) vs. Maya (Chill Lofi)**
These two got completely different results, which makes sense. Alex wants loud, fast, danceable pop — so she got Sunrise City and Gym Hero. Maya wants slow, quiet, calm music — so she got Library Rain and Midnight Coding. They have nothing in common in their top 5, which is exactly what you'd expect from two people with opposite tastes.

**Alex (High-Energy Pop) vs. Marcus (Intense Rock)**
These two both want high energy, but different genres. Alex got pop songs and Marcus got rock songs. The interesting part is Gym Hero (a pop song that is very loud and intense) showed up for Marcus too, because the energy and mood matched even though it's not rock. This shows that when a song is extreme enough in one feature, it can sneak into lists it doesn't quite belong in.

**Why does Gym Hero keep showing up for Happy Pop listeners?**
Gym Hero is tagged as pop, which means it instantly gets bonus points for any pop listener. It also has very high energy and danceability, so even when someone just wants light happy pop, the system sees "pop genre — give it points" and slides Gym Hero in. The system doesn't know the difference between gym music and chill background pop. To it, pop is pop.

**Maya (Chill Lofi) vs. Sam (Perfectly Neutral)**
Maya had clear preferences and got a focused lofi list. Sam had no real preferences — everything was set to the middle — and got a random mix of ambient, lofi, and even sad country songs. This shows that the system works best when it has something strong to aim at. When you give it nothing, it just grabs whatever happens to land near the middle numerically, and the results feel random.

**Marcus (Intense Rock) vs. Jordan (Rock but Sad)**
Both wanted rock, so both got Storm Runner at #1. But Marcus wanted intense and got more high-energy metal and synth in his list. Jordan wanted sad, and while the system couldn't find sad rock, it did pull in country and blues sad songs for #2 and #3. The genre locked in the top spot, but the mood shaped the rest of the list.

**Jordan (Rock/Sad) vs. Riley (Reggae, No Genre Match)**
Jordan at least got a genre match at #1. Riley got nothing — reggae isn't in the catalog — so the whole list was built on energy and tempo numbers alone. Riley ended up with indie pop and pop songs that happen to feel similar in speed and energy to reggae. The results aren't terrible but they feel generic, like the system just gave up on finding something personal.
