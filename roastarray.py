from random import randint
import requests
import json

r=requests.get(url = "https://evilinsult.com/generate_insult.php?lang=en&type=json")
data = r.json()

returnJSON = {}
roast = ["I would ask how old you are, but I know you can't count that high.", 'You are so ugly that when your mama dropped you off at school she got a fine for littering.', 'Your mother mates with reindeer!', 'You Sir are an insult upon insults of a booble on an assortment.', "You're so fat the only letters of the alphabet you know are KFC.", 'It looks like your face caught on fire and someone tried to put it out with a fork.', "Here's 20 cents, call all your friends and give me back the change.", "Two wrongs don't make a right, take your parents as an example.", "You're so ugly when you popped out the doctor said aww what a treasure and your mom said yeah lets bury it", "Why don't you slip into something more comfortable? Like a coma.", 'Go and hide under something old!', 'Question: How could a person like you lose 50 pounds of ugly fat in 1 second? Answer: By cutting off your head!', 'Do you still love nature....despite what it did to you?', 'I hear when you were a child your mother wanted to hire somebody to take care of you, but the mafia wanted too much.', 'Do you have to leave so soon? I was just about to poison the tea.', "You're so ugly you made an onion cry.", 'May your wife give birth to a centipede so you have to work for shoes all your life.', 'Some cause happiness wherever they go; others, whenever they go.', 'Do your keepers a huge favor: do a triple summersault through the air, and disappear up your own asshole.', "You're as ugly as a salad!", 'Your mamma so fat she has to wear 2 watches because she covers two time zones.', 'fuckwit', 'I could eat a bowl of alphabet soup and crap out a smarter comeback than what you just said.', "It's not pretty watching a jackass trying to eat a pomegranate.", 'You must be the arithmetic man; you add trouble, subtract pleasure, divide attention, and multiply ignorance.', 'Your family tree is a cactus, because everybody on it is a prick.', "Please, I could remove 90% of your 'beauty' with a tissue.", "Shut up, you'll never be the man your mother is.", "Your value doesn't even amount to the juice squeezed from an old whore's soiled Tampon."]
roast.append('If I wanted to kill myself, I would climb to the number of your chromosomes and then jump to your IQ.')
roast.append ("'Ugly ass, motherfucker.' 'That's not what your mother said last night.'")
roast.append('Your forehead is a bigger wasteland than Chernobyl.')
roast.append('Shrek called me and told me to tell you he wants his face back.')
roast.append('Is that your face or did your neck just throw up?')
roast.append('Your birth certificate is more like an apology letter from the condom factory.')
roast.append('Were you born on a highway? I heard most accidents take place there.')
roast.append('You are so ugly that I bet if you go into a haunted house, you’ll come out with a job application.')
roast.append('I bet God said, \'Let there be light\' because you were standing in the way.')
roast.append('Shut up, you\'ll never be the man your mother is.')
roast.append('Your family tree must be a cactus, because everyone on it is a prick.')
roast.append('You’re so ugly Hello Kitty said goodbye to you.')
roast.append('It looks like your face caught fire and somebody tried to put it out with a fork.')
roast.append('You are so ugly that when your mama dropped you off at school she got a fine for littering.')
roast.append('If you were twice as smart, you\'d still be stupid.')
roast.append('You’re so ugly when you popped out the doctor said, \'Aww what a treasure!\' and your mom said, \'Yeah let’s bury it.\'')
roast.append('So, how\'s life? Oh wait, I forgot you don\'t have one.')
roast.append('We all sprang from apes, but you didn\'t spring far enough.')
roast.append('I hear when you were a child your mother wanted to hire somebody to take care of you, but the mafia wanted too much.')
roast.append('I would ask how old you are, but I know you can\'t count that high.')
roast.append('Out of , sperms, you were the fastest?')
roast.append('If you really want to know about mistakes, you should ask your parents.')
roast.append('When you were born, the police arrested your dad, the doctor slapped your mom, animal control euthanized your brother, and A&E made a documentary that saved your life.')
roast.append('You\'re so fat the only letters of the alphabet you know are KFC.')
roast.append('You\'re so fat you need cheat codes to play Wii Fit.')
roast.append('With a face like yours, I wish I was blind.')
roast.append('Do you still love nature, despite what it did to you?')
roast.append('Why don\'t you check up on eBay and see if they have a life for sale?')
roast.append('You must be the arithmetic man; you add trouble, subtract pleasure, divide attention, and multiply ignorance.')
roast.append('The only positive thing about you is your HIV status.')
roast.append('Is that your face? Or did your neck just throw up?')
roast.append('Two wrongs don\'t make a right, take your parents as an example,')
roast.append('Please, I could remove % of your \'beauty\' with a tissue.')
roast.append('Why don\'t you slip into something more comfortable? Like a coma.')
roast.append('The only thing that goes erect when I\'m near you is my middle finger.')
roast.append('Can I borrow your face? My arse is on holiday.')
roast.append('All the branches fell off your family tree when you were born.')
roast.append('You\'re like STDs, nobody wants you, everyone hates you and it proves your parents should have used protection.')
roast.append('If I wanted to kill myself, I could just climb up to your ego and jump down to your IQ level.')
roast.append('Your asinine simian countenance alludes that your fetid stench has annulled the anthropoid ape species diversity.')
roast.append('You\'re so fat that you had to be baptized in Sea World.')
roast.append('You\'re so fake that Barbie is jealous.')
roast.append('Your mom just called me, and she asked, that on your way home, you pick up a loaf of bread, bag of milk and some condoms, so she doesn\'t make the same mistake twice.')
roast.append('Who do you think is the best comedy team? I think it\'s your parents....they made the biggest joke!')
roast.append('You are so fat that I bet your pants size is \'Bitch, lose some weight.\'')
roast.append('If I were your mirror I would die by suicide.')
roast.append('Your teeth are beautiful. Do they come in white?')
roast.append('I would love to see things from your point of view but I can’t get my head that far up my ass.')
roast.append('If I had a penny for every brain cell you have I\'d have nothing.')
roast.append('Hi! I\'m a human being. What are you?')
roast.append('I would slap you but that would be animal abuse.')
roast.append('If your brain was donated to science, science would return it.')
roast.append('Why don\'t you shut up and give that hole in your face a chance to heal?')
roast.append('You are the world’s largest dick. Note that I did not use the word HAS.')
roast.append('Sad to see that the money that goes into the Syrian relief effort can\'t be used to pay for your facial reconstruction surgery. I guess it\'s a goat\'s life for you then.')
roast.append('Even when you apply some heavy filters, you still look like shit.')
roast.append('I would show you what you really look like, but I don’t think it is decent to pull down your pants and show your ass in public.')
roast.append('Is your ass jealous of the amount of shit that just came out of your mouth?')
roast.append('It\'s better to let someone think you are an idiot than to open your mouth and prove it.')
roast.append('If laughter is the best medicine, your face must be curing the world.')
roast.append('If ignorance is bliss, you must be the happiest person on earth.')
roast.append('I wasn\'t born with enough middle fingers to let you know how I feel about you.')
roast.append('What language are you speaking? Cause it sounds like bullshit.')
roast.append('You\'re the reason the gene pool needs a lifeguard.')
roast.append('Roses are red, violets are blue, God made me pretty, what happened to you?')
roast.append('I\'d give you a nasty look but you\'ve already got one.')
roast.append('If you\'re going to be two-faced, at least make one of them pretty.')
roast.append('Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.')
roast.append('Why is it acceptable for you to be an idiot but not for me to point it out?')
roast.append('Someday you\'ll go far... and I hope you stay there.')
roast.append('Stupidity\'s not a crime, so you\'re free to go.')
roast.append('You\'re not stupid you just have bad luck when thinking.')
roast.append('The zoo called. They\'re wondering how you got out of your cage.')
roast.append('Even Jesus would friendzone you if you asked for his love.')
roast.append('I was hoping for a battle of wits but you appear to be unarmed.')
roast.append('Aww, it\'s so cute when you try to talk about things you don\'t understand.')
roast.append('When you were born, the doctor came out to the waiting room and said to your dad, \'I\'m very sorry. We did everything we could. But he pulled through.\'')
roast.append('I thought of you today. It reminded me to take the garbage out.')
roast.append('I may love to shop but I\'m not buying your bull.')
roast.append('I\'d slap you but I don\'t want to make your face look any better.')
roast.append('Calling you an idiot would be an insult to all stupid people.')
roast.append('What are you going to do for a face when the baboon wants his butt back?')
roast.append('If you\'re going to be a smartass, first you have to be smart. Otherwise you\'re just an ass.')
roast.append('You\'ve got less meat in your pants than there is in a vegetarian restaurant.')
roast.append('I\'m not saying that I hate you, but I\'d unplug your life support machine to charge my mobile.')
roast.append('You look like a before picture.')
roast.append('I\'m jealous of all the people that haven\'t met you.')
roast.append('If you were on fire and I had water, I\'d drink it.')
roast.append('If you spoke your mind, you\'d be speechless.')
roast.append('I bet that if I give a penny for your thoughts, I’d get change.')
roast.append('You are worse than pineapples on pizza.')
roast.append('You and your brain are a worse combination than Crocs and socks.')
roast.append('I know  fat people in this compound and you are  of them')
roast.append('Your ego compensates for your lack of intellect.')
roast.append('Your parents should\'ve named you miracle after what happened with the broken condom and surviving both abortions.')
roast.append('If you were burning and I had a bucket full of water, I would go water the flowers and then throw the bucket at your ugly ass.')
roast.append('The only way you’ll ever get laid is if you crawl up a chicken’s ass and wait.')
roast.append('Keep rolling your eyes, maybe you\'ll find a brain back there.')
roast.append('Maybe if you ate some of that make up you could be pretty on the inside.')
roast.append('Fake hair, fake nails, fake smile. Are you sure you weren\'t made in China?')
roast.append('I\'m glad to see you\'re not letting your education get in the way of your ignorance.')
roast.append('Mirrors can\'t talk, and lucky for you they can\'t laugh either.')
roast.append('I\'d say you\'re funny, but looks aren\'t everything.')
roast.append('I bet your brain feels good as new, seeing that you\'ve never used it.')
roast.append('You look like Hitler’s wet dream.')
roast.append('I should not attack you on your looks but trust me, there is plenty of subject matter right there.')
roast.append('When I first saw you, I gagged.')
roast.append('Your facial hair makes you look like a prepubescent member of ISIS.')
roast.append('Your face is about as cringy as a Dove commercial.')
roast.append('If I was your shit, you’d get diarrhoea. Get it? ‘Cause even shit would want to get away from you as fast as possible.')
roast.append('The closest a girl will ever get to you is when your mom serves food to you from 6 feet away.')
roast.append('I pity your ancestors.')
roast.append('This is the best you can get?')
roast.append('I am ashamed to be categorized as the same species as you.')
roast.append('I feel sullied just standing next to you.')
roast.append('It feels disgusting breathing the same air you breathe.')
roast.append('You are a piece of shit, and I do not mean metaphorically.')
roast.append('My politeness is preventing me from completely eviscerating you.')
roast.append('I feel for you. Unfortunately, the feeling is nausea.')
roast.append('I think its mating season at the zoo so go back to the orangutans and get married.')
roast.append('twatface')
roast.append('You walk behind your boss reaching through his legs and supporting his testicles.')
roast.append('Your head shape looks like a broken condom.')
roast.append('Out of 100,000 sperm, you were the fastest?')
roast.append('Are you always an idiot or just when I\'m around?')
roast.append('You got fired from the M&M factory for throwing all the Ws.')
roast.append('Your mom made Chuck Norris have a heart attack.')
roast.append('Go away I was looking at something better than you.')
roast.append('Close your mouth! Crap is coming out of it.')

def roaster(i):
    rand = randint(1,2)
    if (rand == 1):
        return data['insult']
    else:
        return roast[i]

def roasterjson():
    rand = randint(0,116)
    roastString = roast[rand]

    returnJSON["roast"] = roastString
    jsonString = json.dumps(returnJSON, indent=4)
    return jsonString
    
