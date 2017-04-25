# INCOMPLETE!

### About the project

The Penalty Tracker is, without a doubt, the most influential project I have worked on outside of the office. It is also one that has really driven home the importance of making a design that you can change really quickly.

The project is rather simple. Every night at 2AM (EST), the script goes out to the NHL's website and grabs a JSON file of all the games that were played throughout the course of the previous day. After it gets the JSON file, it parses through each game reading the critical details such as who was playing, where the game was, the refs (if they are available) before diving deeper into it to find all of the penalties that occurred during the game.

Once it has obtained all of the penalty data, it uses the SQLite library to put all of that data into a database which then gets used by this website to present the user with the data they are interested in. You can see the current iteration here(url).

### Design Considerations

* Separate Databases
* How I get the data
* How I display the data to the user
* Future Improvements
