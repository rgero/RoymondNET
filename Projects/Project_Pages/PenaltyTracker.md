# INCOMPLETE!

### About the project

The Penalty Tracker is, without a doubt, the most influential project I have worked on outside of the office. It is also one that has really driven home the importance of making a design that you can change really quickly.

The project is rather simple. Every night at 2AM (EST), the script goes out to the NHL's website and grabs a JSON file of all the games that were played throughout the course of the previous day. After it gets the JSON file, it parses through each game reading the critical details such as who was playing, where the game was, the refs (if they are available) before diving deeper into it to find all of the penalties that occurred during the game.

Once it has obtained all of the penalty data, it uses the SQLite library to put all of that data into a database which then gets used by this website to present the user with the data they are interested in. You can see the current iteration here(url).

### Design Considerations

* Separate Databases

When I first started the Penalty Tracker, I did not have any real experience with SQL databases. Because of this, I decided that the best way to store the data was to simply place it into a single HTML file. At first, this was fine but as the season progressed I quickly learned that this was not the way I wanted to go. As the number of entries increased, the page's file size got larger and it took longer to load. This was not ideal.

So during the first off season, I decided that the way to solve this was to store all the data in a SQL database. This would allow me to set up a Search page, so the user can explicitly say what they are looking for and get it without having to load all of the data (unless they wanted to)

* How I get the data
* How I display the data to the user
* Future Improvements
  * Playoffs vs Regular Season
  * How to access past seasons
  * Emailing when the script fails to run.
