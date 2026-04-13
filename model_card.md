# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

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
