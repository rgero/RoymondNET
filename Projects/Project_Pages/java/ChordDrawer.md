### About the Project

The Chord Drawer project came to me when I was working on the Guitar Trainer (link to this project is below). It started with the idea that it'd be really cool for me to allow people to load in custom chords, that they have drawn or obtained from the internet, into the Training program. This meant that they would be able to practice a much larger sampling and even choose specific areas that they wanted to work on (for example, say they wanted to work only on barre chords).

I started to think that if I was going to allow them to load in custom chords, I should find a way to recommend a standard format. I wanted to insure that their experience with the Guitar Trainer would be as beneficial and as easy as possible. After quickly searching the web, I decided that the most fun way for me to do this would be to write my own program.

### Iterations

There were several important changes that occurred while working on this initial release of the Chord Drawer. The biggest change was the method in which I determined the closest point to where the user clicked. Originally, I was going calculate the distance from the mouse click to each intersection point on the Fretboard. After calculating all of the distances, I inserted them into a BST to quickly find the ones closest to the click. I quickly realized that there was a flaw with this design where an invalid intersection point could be closer than the intended one. To solve this, I abandoned the BST and just used the fact the points were in a grid to my advantage.
