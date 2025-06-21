# AIAGENTS

# EmoteMind - A Smart Emotion-Aware Memory Agent

> _“Remind me to apply for this internship when I feel confident.”_  
> _“Surface this blog-post idea when I’m inspired again.”_

EmoteMind helps people act on goals when their mind is ready, not on a fixed-time deadline.  
Inspired by state-dependent recall in psychology and cognition, the AI agent stores intentions with an associated emotional tag (confident / focused / inspired / calm).  
When users later describe their current state, EmoteMind returns the most related intentions and nudges them to act, breaking the cycle of forgetting their original intention from when they weren't ready.

---

## Why It’s Different
| Existing To-Do App | EmoteMind |
|-------------------|---------------|
| Time-based pings  | Emotion-based pings |
| Ignores motivation | Waits for aligned mental state |
| Generic reminders | GPT-generated, contextual nudges |
| No cognitive model | Mirrors emotion-based memory |

> **Agentic Behavior**  
> 1. Perceives user input (goal or mood)  
> 2. Stores structured state memory  
> 3. Decides what matches current inputted state  
> 4. Acts by generating a motivational message 

---
## Architecture
> 1. React Vite (HTML/JS)
> 2. Gemini API?

graph TD
  A[User types intention] -->|Gemini parse| B{Intent JSON}
  B --> C[Memory Store (localStorage)]
  D[User types current mood] -->|Gemini parse| E{Mood}
  E -->|Match| F[Filter memory by emotion tag]
  F --> G[Gemini reframe → “Now’s a great time!”]