### About the Project

Immediately after completing the CodeAcademy.com Python course, I started to pick my mind for a project to work on. The goal of the project was to reinforce what I had just learned and to develop something that could help me. The result was this, a program with the purpose of helping me remember and learn the locations of notes on a six string guitar.

The way that I chose to do this was to create a rather simple memory game. The user would first choose what difficulty they wanted. Easy mode was just the whole notes and hard was every note on the fretboard. Both modes consisted of the notes from the open string to the first octave (the 12th fret). Once the mode was selected, the script would draw a fretboard on the screen and mark a random location with an "X". The user would then have to input what note that "X" corresponded to. If the user got it right, a new note was selected and the score would be incremented. If they got it wrong, they were told what the correct answer was and the game would select a new note.

This would keep going until the user entered "quit" into the input. It was at that point, the user was allowed to enter their name if they received a high score and the other scores were displayed. The way that I stored the high scores was by writing two text files to the same directory as the script itself. This was to allow for the script to run on both Linux and Windows without having to worry about file path issues.

I remember how excited I was with the script when I first saw it working properly. I instantly started thinking of new ways to make it better, to distribute it to others that would be interested in giving it a shot. But sadly, I never got around to it. I got sucked into another project or course, and kept moving forward never looking back at the project that started it all.
### Looking back at the script

Today, I can look back at the script and see a lot of things that I would have handled differently if I were to do it again.

The first thing that jumps out at me is the fact I had two functions for the actual gameplay, one for each difficulty. But if you dig into these functions a bit more, they are almost identical. It looks like I just copy/pasted the function and changed a couple keywords and called it done. If I were to do this again, I could easily combine these two functions into one and save some lines of code (and make maintenance easier in the future).

The second change would be error handling. In this game, I never thought of what would happen if the user entered a completely invalid answer. From what I can see, the game wouldn’t break, but it would say their answer was incorrect, not invalid. If I were to do it again, I would handle it more gracefully so that they get a second shot if they enter an invalid answer.

The third change would probably be how I displayed the fretboard. As you can see from the screenshots, it’s pretty basic, and can be a bit confusing.

Ultimately though, I am really glad that I kept this and it didn’t get lost over time. It was a fun little game and it served its purpose. It definitely made me better at remembering notes.
