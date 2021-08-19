# Wishlist-Bot 

#### Concept

This has been a small project I've been working on to brush up on Python a bit. Mostly a proof of concept at this point, but I've had a ton of fun writing this. Essentially, when the emoji react 💖 is added to a Discord message, this code will pull the body, user that made the reaction and the string of the message ID into a Google Sheet as a new row.

When a 💸 react is added by a user, it will parse through the code for that particular message ID and delete all rows with that ID. Fairly simple in scope so far, but I have learned a ton about APIs and working with them.

Configuration values (API tokens, sheet values, worksheet names etc.) are all kept in configuration files. You will need to create the files for yourself. Perhaps I'll upload a template later when I have the time. Credentials.json is the file you would get from Google Cloud when authorizing the API access.

#### TODO:

Add prioritization system, possibly based on number of reacts added.
Add categorization system to allow for multiple lists in different worksheets (This would be a pretty major change from the current code).
Add template file for variables.
Add help file for Discord.
