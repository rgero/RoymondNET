### History

For the last three years, a group of friends and I have participated in the Extra Life. This event is a 24 hour gaming marathon and the intent of the event is to raise as much money as possible for children’s hospitals around the United States and Canada. Over the course of these three years, our team has raised over 4,000 dollars for the Boston Children’s Hospital.

The way that we raise money was by putting ourselves through slight tortures or challenges to encourage our friends and families to donate money to the cause. These challenges could have been as simple as “No Swearing throughout the Entire Event” to one that I took up this past year in which I donated 5 dollars for every point I got in my hockey games over the course of several months.

One of the largest challenges however was taken up by my friend Josh. He insisted on playing every Rainbow Road that has ever existed through out the history of Mario Kart. This was his third year doing it and it often drew a large number of viewers mostly because he is terrible at Mario Kart. This meant that throughout the challenge he would often be swearing, frustrated and people wanted to see his frustration.

This year, we came up with the idea of making him his own version of Rainbow Road. One that was set to be his own personal hell. The four of us quickly set off to make this idea a reality.

### The Game Itself

The game was meant to be a clone of Mario Kart with some inherit challenges in it. We built it in Unity with mostly custom assets. The only thing that was not custom was the car itself. Due to time constraints we went with a standard asset car.

Here is a brief list of the things we implemented into the game, starting with my direct contributions.

### The Track

I created the track out of a series of segments, these segments were created in CATIA V5, exported to the STL format, brought into Blender where they were cleaned up and then brought into Unity. Once all the pieces were in Unity, I positioned them until I felt that it was of adequate length and difficulty. In the end, there were less than 10 unique track pieces.

#### Pranks / Twitch Integration

One of the biggest things I wanted for this game was to involve the audience. I wanted them to be able to participate in the fun and make things more difficult for Josh. The way that I did this was by integrating the game with our twitch channel’s chatroom. When the game started, it connected to the chatroom and the users were able to enter the following commands to cause pranks happen on the screen.

* !flip - flipped the camera
* !reverse - reversed the controls
* !disappear - made the track disappear
* !say - printed a message on the screen to Josh.

It goes without saying that we couldn’t just open the floodgates to a twitch chat and let them have their way with the game, so we implemented a simple queue that had a limit of 3 commands at a time. The only command that was able to bypass the queue was the “!say” command since we wanted people to be able to give inspiration to him

#### Waypoints

In order to track his progress through the course, we had a simple waypoint system. If he fell off the track, or somehow ended up with the car flipped, I gave him the option to reset the car with a simple button to press.

#### The "Bad" Colliders

When we first tried the completed track, it felt a bit too easy, especially on the corners. The idea came up of having some of the unity colliders move “in” on the curves so that way you’d have to take them much more carefully or else you’d be thrown off the track.


#### Non-Twitch Pranks

The others designed a couple pranks that were not twitch integrated. The first one was a cannon that fired pineapples (similar to a bullet bill in the Mario games), another was invisible track segments, and the final one was a pipe that just spewed out pineapples. The reason pineapples were chosen was because Josh hates the fruit.

#### Final Lap Television Torture

When we set out to make this, we decided that three laps were all that we were going for. However on that third lap it should really be annoying. To do this, giant TV’s would play the a couple highlights from the Patriots vs Giants Super Bowl that ruined their perfect season.

### The Reception

Unfortunately, the game was not well received by Josh. I thought he was going to be able to handle the controls much better than he did. Eventually I had to disable the twitch pranks completely in an effort to make things easier. Throughout the duration of the race, he cursed at us throughout the entire thing and finished the entire race out of spite. This whole event caused a quite significant change to the environment for the rest of the event. I remember personally wanting to leave after it happened but that would not have been in the spirit of Extra Life.

I did talk to several friends who thought the entire thing was rather hilarious and that it was a perfect end to the Rainbow Road segment of the event.

### Lessons Learned

I think the biggest lesson I learned throughout this was really how to work with a team on the development side of the wall. Usually in my professional career, I am a bit removed from the team aspect of things. By this I mean if I am developing something, it is usually on my own and I present it when it is done. This was a much appreciated change of pace.

Another lesson would be that I have to remember the target audience more. Looking back I can tell that I put myself in the shoes of the player, and my skill set was much different than the intended player. I feel that if we had more time, we might have realized this and backed out some of the more aggravating challenges from it.
