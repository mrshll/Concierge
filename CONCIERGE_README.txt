CONCIERGE: DESIGN DOC

================================================================================

idea: finding things to do and planning them is hard. there are lots of sources
	of data out there - no source of personalized information.

Sources: facebook, yelp, 4sq, last.fm, twitter, etc. no personalized way to
	generate "event" recommendations

"event": meal, hike, movie, sightseeing, road trip, camping, you name it

analogies: imdb provides data, netflix provides recs, google reader provides
	data, stumbleupon/prismatic provides recs, 4sq provides data (where your
	friends have been & what they like), does not provide personal recs
	(i.e., you should do this, because it fits your prefs) yelp provides
	data, does not provide personal recs, (same as above))

	Even though some of the above provide recs, they do not do so in a
	personalized delivery either. The market for soulless, impersonal
	systems is oversaturated.

characterize users by variables that indicate preference 
  -attributes: age, gender, orientation, geography, income, likes/doesn't like
   to travel, hates/doesn't hate traffic, &c 
  -instantaneous attributes: time-of-day, location, &c 
  -preference attributes: profligate/frugal, outdoorsy/urban, music prefs, &c

characterize events by event attributes 
  -location, cost, type-of-event, time-of-day, &c 
  -variables specific to type-of-event (i.e., if a music event, the type of
   music and the artist(s); if a meal then the cuisine and location/cost of
  restaurant, etc.), &c 
  -rating of the event in general 
  -rating of the event by people similar to user

characterize request by request attributes 
  -immediate or in the future?
  -willing to travel or not? in a car or not?  
  -how much to spend?  
  -time of day
  -type-of-event -etc.

output: 
  -the solution of what to do, how to do it, and all necessary planning /
   arrangements made.
  -i.e.: "We think you would have fun going to the celtics game tonight. if you 
   want we can buy you tickets and arrange a taxi to pick you up."

learning: 
  -based on response to output: (accept / decline), concierge learns more about
   the prefs of the user
  -we learn based on feedback on which concierges match best with which users.
   Because we are trying to make it as personal as possible, we want to pair
   users with Concierges they enjoying interacting with, as this will improve

sources of information: 
  -events: 4sq, yelp, fbook, etc.  
  -users: 4sq checkins (by them and by similar people), yelp (reviews by them 
   and similar peeps), fbook, twitter, surveys 
  -request: user input, feedback


PLAN OF ATTACK:
  -the user experience has to be as seemless as possible. there are two ways to
   proceed:
	    1. Focus first on UX
	      -Create one touch app that puts you in the Concierge Q. They call
	       YOU as soon as they can so that you aren't waiting on the phone
	      [TOM] you can probably use twilio for this piece
	      [TOM] think that the calling infrastructure is imprtnt, but the most
	      important thing is getting the natural language/symbolic query part of it
 	      up because that's what the concierges will use anywar

	      -Create infastructure for email, text reception too.
	      -Create infastructure for spending clients money for them
		(Approval on app/Approval by email/etc)
	    2. Focus on Machine Learning
	      -Set up web interface to connect to all the api's we are mining
	      -Build database infastructure to make learning possible. We need
	       to figure out what the features are and which points are
	       significant.
	      [TOM] - we need to think about what semi-static and what dynamic
	      databases we want to build and what data we will get to form the
	      backbone of it. an example of a semi-static database  would be the database of "events" 
	      -Figure out which algorithm best classifies this type of data
	      -Test, test, test...

  -DO MORE RESEARCH ON THE MARKET 
	-my (Tom's)  view is that this is the LEAST important thing to do
	-we know that what we want to do is not being done exactly the way we plan to,
	-and furthermore we know that this shit is hard.
