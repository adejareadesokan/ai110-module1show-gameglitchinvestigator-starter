# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The game told me to always go lower in every scenario. the secret number was a string rather than an integer. the difficulty range of normal was higher than that of hard. The logic of update score was wrong
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude and CoPilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI assisted me with my Unit testing. I got confused with the test  type on my assert statement it was able to help me resolve the error message and the test passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
After refactoring logic_utils, The Submit Guess button only started working for the right number, and the numbers changed on every click of the button. I was able to verify it because it displayed no prompt on the streamlit app but the secret number kept changing.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decide by checking the app. If I see the logic is fixed and I test the app and the error is fixed. I conclude that specific bug is fixed.
- Describe at least one test you ran (manual or using pytest)  
I tested the winning_guess function. I used an assert statement as well as pytedt to do it. It showed that the winning_guess worked fine.
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
It didn't help me understand any tests but helped me implement some However.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
 The sumbit guess logic was flawed and changed everytime you submitted a guess regardless of whether it was right or wrong.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
 I changed the submit guess logic and changed the range everytime the difficulty was changed
 ---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Unit tests is something I would want to reuse in future projects. I fell it's very effective in debugging and easy to use. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I learned that Ai doesn't necessarily act on accuracy but on the user's instruction so it's still prone to making mistakes
