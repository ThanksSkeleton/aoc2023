# To a 5 year old

Hey kid! Let's talk about my solution to this puzzle!

Now, like a lot of these puzzles, there's a story about elves and what they're doing.
The puzzle wants you to translate a original number, through a bunch of different translations, down and down until you get to the end, and then give the best number.

What I like to do is visualize things with little monsters or creatures moving around, because it makes it easier to think about it. Imagine a little frog running towards alligators, it becomes more emotional and you can imagine what can go right (and wrong!) for the frog. What should the frog do, could it get eaten? This is a cool tip that can help you when you're thinking about puzzles.

# Part 1 - Frogger

I imagined

* each number was a little frog
* each table was a river
* each table entry was an alligator

and each frog had to get through all the rivers of alligators to get to the end. 

Then we pick the greenest frog. This is like Frogger, a very old video game, you ever seen that?

This story is a little strange and funny, because even if a frog gets eaten by an alligator, the frog changes color in the alligator's stomach, and the alligator just poops it out. So all the frogs get through at the end, none of them die. But most of them will change color.

We could be very smart and make predictions on which alligators are best (who makes the frog greener?), or what paths are best, or which frogs are in the best positions - but all of that is really hard, so we should just let the frogs run and see what happens!

```
For each river,
	For each frog that starts at that river,
		For each alligator,
			If it can eat the frog,
				it eats the frog, which changes color for the next river
		If no alligators eat the frog it goes to the next river	
After the final river, take the greenest frog
```

We did it!

# Part 2 - Logger

Now. Let's talk about the second part of the puzzle. It's a lot harder, but if we carry forward the ideas and alligators from the first part it can help us.

Instead of being little tiny FROGS (single numbers) trying to get across, now we have *big* *wide* LOGS (ranges) of all different lengths.

When an alligator takes a bite out of a log, it's more complicated. This could create new pieces of logs, that we have to keep track of, and they go all the way through ALL the rivers.

* An alligator could swallow the whole log
* or it could take a bite off the left side, leaving a piece
* or it could take a bite off the right side, leaving a piece
* or it could take a bite out of the middle, leaving two pieces
* or it could miss all of the log

... and EVERY alligator gets to try to take a bite out of EVERY log!

Wow, that's kinda complicated. But we can do it. Its not that bad.

Here are some things that we know that can make this problem easier:

* A log can get bitten by multiple alligators, but no alligators can fight over the same PART of the log
* Because of that, it doesn't matter in what order you offer the logs to them
* There's not THAT many alligators
* They make at most 2 additional pieces per bite. 
* They won't make sawdust because they can't bite THAT much!

We can figure out what happens and make sure we track all the logs and the pieces.

```
For each river,
	For each log that starting at that river, plus any NEW log pieces
		For each alligator,
			If it can take a bite out of the log:
				Take the eaten piece, change its color, and pass it to the next river
				Take all the leftovers and for the pile of logs for THIS river. 
	For all the logs that no alligators want to eat, pass it to the next river
After the final river, take the greenest log.
```

We're done!
