# RedditBot (Created October 2019)

## How to use it?
The function run_bot takes an assortment of arguments. The clientID and clientSecret are both given
in the set up of a bot account for reddit. These are taken in as strings. The username and password
are also taken in as strings. Reddit asks all bots to be associated with a real account so the
mainUsername argument is your main accounts username taken as a string. Reddit breaks its posts
into subReddits and so pic the desired subreddit and enter it as a string. trigerPhrases1,
trigerPhrases2 are lists of strings in which the bot looks for these strings in the posts
and if one of the strings is in the post it comments on the post. responses1, responses2
are a list of strings that will be the comments when the post has a trigger phrase. The bot
will take one of these strings at random from the list and post it. The bot allows for two
different lists of trigger phrases and 2 different response list associated with these.

## How it works?
The bot will search for posts within the past 2 hours. It will search for the triger phrases. 
If one is found it will make an appropriate response of one of your inputed response. Once
the post is made reddit has a safeguard in which users with a lower amount of karma (AKA 
new accounts) can only comment once every 10 minutes. The program will sleep to keep this
safeguard from being triggered. Once the 10 minutes is up it will continue searching. 
It will continue searching even if there are no more posts it hasnt checked. It will then
wait for any new posts to be posted and search those too.

## Example
In this example, the bot will be searching through neverbrokeabone.

<pre><code>run_bot(clientID = *****, clientSecret = *****, USERNAME = ******, PASSWORD = *******,
        mainUsername = *******, subReddit = "neverbrokeabone",
        trigerPhrases1 = ["sorry" ,"fail", "goodbye"],
        trigerPhrases2 = ["milk", "calcium"],
        responses1 = ["Get the hence!", "You have failed us","Mods you know what to do", "Should have drunk your milk" ],
        responses2 = ["The Nectar of the Gods","Love me some sweet milk", "MIIILLLLKKKKK", "Drink it up", "Calcium makes boy grow strong"])
</code></pre>   

This will search for phrases that are popular for someone who broke a bone and also
posts about milk. Which as you can imagine, this subredddit has a lot of.


