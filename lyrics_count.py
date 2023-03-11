
song_lyrics = "Somebody said they saw you The person you were kissing wasn't me And I would never ask you, I just kept it to myself \
I don't wanna know, if you're playing me Keep it on the low Cause my heart can't take it anymore And if you creeping, please don't let it show Oh baby, I don't wanna know\
I think about it when I hold you When looking in your eyes, I can't believe And I don't need to know the truth But baby keep it to yourself \
I don't wanna know, if you're playing me Keep it on the low Cause my heart can't take it anymore And if you creeping, please don't let it show Oh baby, I don't wanna know\
Did he touch you better than me  Did he watch you fall asleep Did you show him all those things that you used to do to me If you're better off that way Baby all that I can say If you're gonna do your thing, then don't come back to me\
21 \
Had me crushing, I was cuffing like the precinct\
How you go from housewife to a sneaky link\
Got you ridin round in all types of benz's and rovers\
Girl you used to ride in a rinky dink\
I'm the one put you in Eliante \
Fashion Nova model, I put you on the runway \
You was rocking coach bags, got you chanaynay\
Side bitch in frisco, I call her my bae bae \
I got a girl but I still feel alone\
If you playing me that mean my home aint home\
Having nightmares of going through your phone \
Can't even record you got me out my zone\
I don't wanna know, if you're playing me\
Keep it on the low\
Cause my heart can't take it anymore\
And if you creeping, please don't let it show\
Oh baby\
I don't wanna know, if you're playing me\
Keep it on the low\
Cause my heart can't take it anymore\
And if you creeping, please don't let it show\
Oh baby I don't wanna know\
If you creeping just don't let me find out \
Get a hotel never bring him to the house \
If you're better off that way (better off that way)\
Baby all that I can say \
If you're gonna do your thing, then don't come back to me"


split_lyrics = song_lyrics.split(' ')
#print(split_lyrics)
#['Somebody', 'said', 'they', 'saw', 'you', 'The', 'person', 'you', 'were', 'kissing', "wasn't", 'me', 'And', 'I', 'would', 'never', 'ask', 'you,', 'I', 'just', 'kept', 'it', 'to', 'myself', 'I', "don't", 'wanna', 'know,', 'if', "you're", 'playing', 'me', 'Keep', 'it', 'on', 'the', 'low', 'Cause', 'my', 'heart', "can't", 'take', 'it', 'anymore', 'And', 'if', 'you', 'creeping,', 'please', "don't", 'let', 'it', 'show', 'Oh', 'baby,', 'I', "don't", 'wanna', 'knowI', 'think', 'about', 'it', 'when', 'I', 'hold', 'you', 'When', 'looking', 'in', 'your', 'eyes,', 'I', "can't", 'believe', 'And', 'I', "don't", 'need', 'to', 'know', 'the', 'truth', 'But', 'baby', 'keep', 'it', 'to', 'yourself', 'I', "don't", 'wanna', 'know,', 'if', "you're", 'playing', 'me', 'Keep', 'it', 'on', 'the', 'low', 'Cause', 'my', 'heart', "can't", 'take', 'it', 'anymore', 'And', 'if', 'you', 'creeping,', 'please', "don't", 'let', 'it', 'show', 'Oh', 'baby,', 'I', "don't", 'wanna', 'knowDid', 'he', 'touch', 'you', 'better', 'than', 'me', '', 'Did', 'he', 'watch', 'you', 'fall', 'asleep', 'Did', 'you', 'show', 'him', 'all', 'those', 'things', 'that', 'you', 'used', 'to', 'do', 'to', 'me', 'If', "you're", 'better', 'off', 'that', 'way', 'Baby', 'all', 'that', 'I', 'can', 'say', 'If', "you're", 'gonna', 'do', 'your', 'thing,', 'then', "don't", 'come', 'back', 'to', 'me21', 'Had', 'me', 'crushing,', 'I', 'was', 'cuffing', 'like', 'the', 'precinctHow', 'you', 'go', 'from', 'housewife', 'to', 'a', 'sneaky', 'linkGot', 'you', 'ridin', 'round', 'in', 'all', 'types', 'of', "benz's", 'and', 'roversGirl', 'you', 'used', 'to', 'ride', 'in', 'a', 'rinky', "dinkI'm", 'the', 'one', 'put', 'you', 'in', 'Eliante', 'Fashion', 'Nova', 'model,', 'I', 'put', 'you', 'on', 'the', 'runway', 'You', 'was', 'rocking', 'coach', 'bags,', 'got', 'you', 'chanaynaySide', 'bitch', 'in', 'frisco,', 'I', 'call', 'her', 'my', 'bae', 'bae', 'I', 'got', 'a', 'girl', 'but', 'I', 'still', 'feel', 'aloneIf', 'you', 'playing', 'me', 'that', 'mean', 'my', 'home', 'aint', 'homeHaving', 'nightmares', 'of', 'going', 'through', 'your', 'phone', "Can't", 'even', 'record', 'you', 'got', 'me', 'out', 'my', 'zoneI', "don't", 'wanna', 'know,', 'if', "you're", 'playing', 'meKeep', 'it', 'on', 'the', 'lowCause', 'my', 'heart', "can't", 'take', 'it', 'anymoreAnd', 'if', 'you', 'creeping,', 'please', "don't", 'let', 'it', 'showOh', 'babyI', "don't", 'wanna', 'know,', 'if', "you're", 'playing', 'meKeep', 'it', 'on', 'the', 'lowCause', 'my', 'heart', "can't", 'take', 'it', 'anymoreAnd', 'if', 'you', 'creeping,', 'please', "don't", 'let', 'it', 'showOh', 'baby', 'I', "don't", 'wanna', 'knowIf', 'you', 'creeping', 'just', "don't", 'let', 'me', 'find', 'out', 'Get', 'a', 'hotel', 'never', 'bring', 'him', 'to', 'the', 'house', 'If', "you're", 'better', 'off', 'that', 'way', '(better', 'off', 'that', 'way)Baby', 'all', 'that', 'I', 'can', 'say', 'If', "you're", 'gonna', 'do', 'your', 'thing,', 'then', "don't", 'come', 'back', 'to', 'me']


unique_words = set(split_lyrics)
#print(unique_words)
#{'', 'like', 'say', 'way)Baby', "can't", 'him', 'need', 'off', 'call', 'asleep', 'just', "Can't", 'babyI', 'bags,', 'it', 'coach', 'hotel', 'feel', 'yourself', "dinkI'm", 'better', 'Cause', 'still', 'ride', 'knowI', 'then', 'round', 'take', 'about', 'keep', 'Had', 'roversGirl', 'used', 'truth', 'believe', 'fall', 'please', 'kissing', 'find', 'your', 'rinky', 'me', 'baby,', 'model,', 'know', 'let', 'saw', 'through', 'touch', 'knowDid', 'lowCause', 'you,', 'of', 'they', 'think', 'when', 'that', 'chanaynaySide', 'home', 'homeHaving', 'you', 'was', 'do', 'And', 'cuffing', 'mean', 'baby', 'heart', 'Nova', 'girl', 'Somebody', 'would', 'said', 'if', 'playing', 'The', 'her', 'even', 'showOh', 'bring', 'precinctHow', "you're", 'out', 'thing,', 'on', 'wanna', 'than', 'those', 'looking', 'frisco,', 'hold', 'Baby', 'the', 'phone', 'one', 'sneaky', 'Oh', "benz's", 'record', 'knowIf', 'gonna', 'from', 'bitch', "wasn't", 'But', 'can', 'going', 'low', 'bae', 'put', 'creeping', 'Fashion', 'I', 'housewife', 'things', 'back', 'go', 'If', 'and', 'zoneI', 'but', "don't", 'Eliante', 'runway', 'ask', 'Did', 'watch', '(better', 'aloneIf', 'crushing,', 'way', 'were', 'You', 'he', 'a', 'myself', 'Keep', 'rocking', 'anymoreAnd', 'in', 'to', 'aint', 'know,', 'When', 'anymore', 'me21', 'Get', 'my', 'house', 'person', 'ridin', 'creeping,', 'linkGot', 'nightmares', 'never', 'kept', 'types', 'all', 'meKeep', 'eyes,', 'got', 'show', 'come'}


print("Number of words in the whole lyrics: ")
print(len(split_lyrics)) # number of words in the whole lyrics
print("Number of unique words: ")
print(len(unique_words)) # number of unique words