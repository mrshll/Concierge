Learn
=====
This is the learning engine for the concierge app

Signature for learning function
-------------------------------

gets: lat, long, username

returns: ranked list of restaurants

v0.1
----

a simple scoring system that ranks restaurants by the following equation:

`w_1 * cuisine_sim + w_2 * rating + w_3 * decay( distance ) + w_4 * price_diff`

where cuisine_sim is the cosine similarity of the user's average cuisine vector
and the restaurant's cuisine vector

`decay( x ) = x^2`

`price_diff = | price_u - price_r |`


