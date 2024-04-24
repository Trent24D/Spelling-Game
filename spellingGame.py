import random, os
from gtts import gTTS
from playsound import playsound
words = ['abhorrent', 'abrasive', 'absolute', 'academic', 'aching', 'acidic', 'acrobatic', 'admirable', 'admired', 'adolescent', 'adorable', 'adventurous', 'affectionate', 'aggravating', 'aggressive', 'agile', 'agitated', 'agonizing', 'alarmed', 'alarmingly large', 'alarmingly small', 'alert', 'alien', 'all-knowing', 'altruistic', 'amazing', 'amber', 'ambitious', 'American', 'amphibious', 'amusing', 'anchored', 'ancient', 'angelic', 'angry', 'anguished', 'animated', 'antique', 'anxious', 'apprehensive', 'arctic', 'Aristotelian', 'aromatic', 'artistic', 'ashamed', 'astonishing', 'athletic', 'attentive', 'attractive', 'auburn', 'austere', 'Australian', 'authentic', 'avariciousaverage', 'awesome', 'awfulawkward', 'babybabyishbackward', 'badbasic', 'beautifulBelgian', 'beloved', 'bewitched', 'big-hearted', 'big', 'biodegradable', 'bite-sized', 'bitter', 'black-and-white', 'black', 'bland', 'blank-faced', 'blank', 'blaring', 'bleeding', 'blind', 'blissful', 'blue', 'blundering', 'blushing', 'bogus', 'boiling', 'bold', 'bony', 'boorish', 'boring', 'bossy', 'bouncy', 'bountiful', 'bowed', 'brave', 'Brazillian', 'breakable', 'bright', 'brilliant', 'British', 'broken', 'bronze', 'brown', 'bruised', 'bubbly', 'buggy', 'bulky', 'bumbling', 'bumpy', 'burdensome', 'burly', 'buzzing', 'calm', 'Canadian', 'canine', 'carefree', 'careful', 'careless', 'caring', 'cautious', 'charming', 'charred', 'cheap', 'cheerful', 'cheery', 'Chinese', 'chubby', 'circular', 'classic', 'clear', 'clever', 'close', 'closed', 'clouded', 'clueless', 'clumsy', 'coarse', 'cold', 'colorful', 'colorless', 'colossal', 'comedic', 'comfortable', 'compassionate', 'complex', 'concerned', 'concerning', 'concrete', 'condemned', 'confused', 'conventional', 'cooked', 'cool', 'cooperative', 'coordinated', 'corny', 'corrupt', 'costly', 'courageous', 'courteous', 'crafty', 'crazy', 'creamy', 'creative', 'creative', 'creepy', 'criminal', 'cringe-worthy', 'crisp', 'critical', 'crooked', 'cruel', 'crummy', 'crushing', 'cuddly', 'cultivated', 'cultured', 'cumbersome', 'curly', 'curvy', 'cute', 'cyan', 'cybernetic', 'damaged', 'dangerous', 'dapper', 'daring', 'dark', 'darling', 'dazzling', 'dead', 'deadly', 'deaf', 'deafening', 'decisive', 'deep', 'defenseless', 'defensive', 'defiant', 'deficient', 'delectable', 'delicious', 'delightful', 'delirious', 'demanding', 'dense', 'dependable', 'dependent', 'derivative', 'descriptive', 'deserted', 'detailed', 'determined', 'devoted', 'different', 'difficult', 'digital', 'diligent', 'dim', 'dimpled', 'dimwitted', 'dirty', 'disastrous', 'discrete', 'disfigured', 'disguised', 'disgusting', 'dishonest', 'disloyal', 'distorted', 'dizzy', 'dopey', 'doting', 'doublecrossing', 'drab', 'drafty', 'dramatic', 'dreary', 'droopy', 'dry', 'dual-wielding', 'dull', 'dumb', 'dunderheaded', 'dutiful', 'eager', 'early-rising', 'earnest', 'easily-exhausted', 'easily-startled', 'easygoing', 'ecstatic', 'edible', 'eerie', 'Egyptian', 'elaborately dressed', 'elastic', 'elated', 'elderly', 'electric', 'elegant', "elementary school's", 'elliptical', 'embarrassed', 'embellished', 'eminent', 'emotional', 'emotionless', 'empirical', 'empty-headed', 'empty', 'enchanted', 'enchanting', 'energetic', 'English', 'enlightened', 'enormous', 'enraged', 'envious', 'ethereal', 'ethical', 'euphoric', 'evergreen', 'everlasting', 'evil', 'exalted', 'excellent', 'excitable', 'excited', 'exciting', 'exhausted', 'exhaustingly energetic', 'exotic', 'expensive', 'experienced', 'expert', 'extra-large', 'extra-small', 'extroverted', 'fabulous', 'failing', 'faint', 'fair', 'faithful', 'fake', 'false', 'familiar', 'famous', 'fancy', 'fantastic', 'fast', 'fat', 'fatal', 'fatherly', 'fatherly', 'favorable', 'favorite', 'fearful', 'fearless', 'feisty', 'feline', 'feminine', 'fickle', 'fiendish', 'fighting', 'filthy', 'fine', 'finished', 'Finnish', 'firm', 'fitting', 'fixed', 'flaky', 'flamboyant', 'flaming', 'flashy', 'flat', 'flawed', 'flawless', 'flickering', 'flimsy', 'flippant', 'floating', 'flowery', 'fluffy', 'fluid', 'flustered', 'flying', 'focused', 'foolhardy', 'foolish', 'forceful', 'forked', 'formal', 'forsaken', 'fragile', 'fragrant', 'frail', 'frayed', 'French', 'fresh', 'friendly', 'frightened', 'frightening', 'frigid', 'frilly', 'frivolous', 'frizzy', 'frosty', 'frozen', 'frugal', 'fruitful', 'full-grown', 'fully-functional', 'fumbling', 'fuming', 'fundamentalist', 'funny', 'fussy', 'fuzzy', 'gargantuan', 'gaseous', 'generous', 'gentle', 'genuine', 'German', 'ghostly', 'giant', 'giddy', 'gifted', 'gigantic', 'gilded', 'girly', 'giving', 'glamorous', 'glaring', 'glass', 'glassy-eyed', 'gleaming', 'gleeful', 'glistening', 'glittering', 'glittery', 'glossy', 'glum', 'gold', 'golden', 'good-natured', 'gorgeous', 'graceful', 'gracious', 'grateful', 'grave', 'gray', 'grayscale', 'great', 'greedy', 'Greek', 'green', 'gregarious', 'grizzled', 'gross', 'grotesque', 'grouchy', 'growing', 'growling', 'grubby', 'gruesome', 'grumbling', 'grumpy', 'guilty-looking', 'guilty', 'gullible', 'gummy', 'gun-toting', 'hairy', 'hand-drawn', 'hand-painted', 'handmade', 'handsome', 'handy', 'happy-go-lucky', 'happy', 'hard-to-find', 'hard', 'harmful', 'harmless', 'harmonious', 'harsh', 'hasty', 'hateful', 'haunting', 'healthy', 'heavenly', 'heavy', 'hefty', 'helpful', 'helpless', 'hidden', 'hideous', 'high-level', 'hilarious', 'historically accurate', 'hoarse', 'hollow', 'homely', 'hopeful', 'horrible', 'hospitable', 'hot', 'huge', 'humble', 'humiliating', 'humming', 'humongous', 'Hungarian', 'hungry', 'hurtful', 'husky', 'icky', 'icy', 'ideal', 'idealistic', 'idiotic', 'idle', 'idolized', 'ignorant', 'ill-fated', 'ill-informed', 'ill', 'illegal', 'illiterate', 'illustrious', 'imaginary', 'imaginative', 'imbecillic', 'immaculate', 'immaterial', 'immense', 'impartial', 'impassioned', 'impeccably-dressed', 'imperfect', 'imperturbable', 'impish', 'impolite', 'important', 'impossible', 'impractical', 'impressionable', 'impressive', 'improbable', 'impure', 'Incan', 'incomparable', 'incompatible', 'incomplete', 'inconsequential', 'incredible', 'indelible', 'Indian', 'indolent', 'indomible', 'inexperienced', 'infamous', 'infantile', 'infatuated', 'inferior', 'infinite number of', 'informal', 'ingenious', 'innocent', 'insecure', 'insidious', 'insignificant', 'insistent', 'instructive', 'intelligent', 'interesting', 'international', 'intrepid', 'intrusive', 'ironclad', 'irresponsible', 'irritating', 'Italian', 'itchy', 'jaded', 'jagged', 'Japanese', 'jaunty', 'jealous', 'jeering', 'jingling', 'jittery', 'jolly', 'jovial', 'joyful', 'joyous', 'jubilant', 'judicious', 'juicy', 'jumbo', 'jumping', 'jumpy', 'juvenile', 'kaleidoscopic', 'keen-eyed', 'Kenyan', 'kind', 'kindhearted', 'klutzy', 'knobby', 'knotted', 'knowledgeable', 'kooky', 'kosher', 'lame', 'lanky', 'large', 'lawful', 'lazy', 'leafy', 'lean, mean fighting', 'lean', 'legalistic', 'lighthearted', 'lightweight', 'likable', 'limp', 'limping', 'liquid', 'listless', 'little', 'lively', 'livid', 'living', 'loathsome', 'lone', 'lonely', 'lonesome', 'long-winded', 'long', 'loose', 'lopsided', 'lost', 'loud', 'lovable', 'lovely', 'loving', 'lowbrow', 'loyal', 'lucky', 'lumbering', 'luminous', 'lumpy', 'lustrous', 'luxurious', 'lying', 'lyrical', 'mad', 'made-up', 'magenta', 'magnificent', 'majestic', 'major', 'mammoth', 'manly', 'married', 'marvelous', 'masculine', 'massive', 'mature', 'Mayan', 'meager', 'mean', 'meaty', 'medical', 'meek', 'mellow', 'melodic', 'memorable', 'menacing', 'merry', 'messy', 'metallic', 'mindless', 'miniature', 'mink-like', 'minty', 'miserable', 'miserly', 'misguided', 'misty', 'modern', 'modernized', 'modest', 'moist', 'monstrous', 'morally-driven', 'moronic', 'mortified', 'motherly', 'motionless', 'muddy', 'muffled', 'multicolored', 'mundane', 'mushy', 'musty', 'muted', 'mysterious', 'naiive', 'narrow-minded', 'nasty', 'Native American', 'natural', 'naughty', 'nautical', 'nearsighted', 'needy', 'negative', 'neglected', 'negligible', 'neighboring', 'nervous', 'new', 'nice', 'nifty', 'nimble', 'nocturnal', 'noisy', 'non-functioning', 'nonstop', 'noteworthy', 'novel-writing', 'noxious', 'numb', 'nutritious', 'nutty', 'obedient', 'obese', 'objectively good', 'oblong', 'obsessive', 'obvious', 'odd', 'oddball', 'odious', 'offbeat', 'offensive', 'oily', 'old-fashioned', 'old', 'open-minded', 'optimistic', 'orange', 'origami', 'ornate', 'ornery', 'outgoing', 'outlandish', 'outrageous', 'outstanding', 'oval', 'over-aware', 'over-dramatic', 'overactive', 'overburdened', 'overcooked', 'overjoyed', 'overly-attached', 'overly-emotional', 'painted', 'palatable', 'pale', 'paltry', 'passionate', 'pastel', 'peaceful', 'peppery', 'perfect', 'perfumed', 'perky', 'pesky', 'pessimistic', 'petty', 'phony', 'photorealistic', 'pink', 'pitiful', 'pixellated', 'plastic', 'playful', 'pleasant', 'pleased', 'pleasing', 'plump', 'plush', 'pointed', 'pointless', 'pointy', 'Polish', 'polished', 'polite', 'political', 'polka-dotted', 'poor', 'poorly-animated', 'poorly-drawn', 'popular', 'portly', 'positive', 'powerful', 'powerless', 'practical', 'precious', 'prestigious', 'pretty', 'previously unknown', 'pricey', 'prickly', 'pristine', 'private', 'prize', 'productive', 'profitable', 'proper', 'proud', 'prudent', 'puce', 'pumpernickel', 'punctual', 'pungent', 'puny', 'pure', 'purple', 'pushy', 'putrid', 'puzzled', 'puzzling', 'qualified', 'quarrelsome', 'queasy', 'querulous', 'questionable', 'quick-witted', 'quick', 'quiet', 'quintessential', 'quirky', 'quizzical', 'radiant', 'ragged', 'rare', 'rash', 'raw', 'realistic', 'reasonable', 'reckless', 'rectangular', 'red', 'reflective', 'regal', 'reliable', 'remorseful', 'repentant', 'repulsive', 'respectful', 'responsible', 'revolving', 'rewarding', 'rich', 'righteous', 'rigid', 'ringed', 'ripe', 'roasted', 'robust', 'rosy', 'rotating', 'rotten', 'rotund', 'rough', 'round', 'rowdy', 'royal', 'rubbery', 'ruddy', 'rude', 'runny', 'rural', 'rusty', 'sacred', 'sad', 'safety-minded', 'salty', 'sane', 'sarcastic', 'sardonic', 'satirical', 'satisfied', 'satisfying', 'scaly', 'scared', 'scary', 'scented', 'scholarly', 'scientific', 'scornful', 'scratchy', 'scrawny', 'secondary', 'secretive', 'sedentary', 'self-assured', 'self-assured', 'self-reliant', 'selfish', 'sentimental', 'separatist', 'serious', 'serpentine', 'severe', 'shadowy', 'shallow', 'shameful', 'shameless', 'sharp', 'shiny', 'shocked', 'shocking', 'shoddy', 'short-term', 'short', 'showy', 'shrill', 'shy', 'sick', 'silent', 'silky', 'silly', 'silver', 'simple-minded', 'simplistic', 'sinful', 'single', 'sizzling', 'skeletal', 'skinny', 'sleepy', 'slim', 'slimy', 'slow', 'slushy', 'small', 'smart', 'smooth', 'smug', 'snappy', 'snarling', 'sneaky', 'sniveling', 'sociable', 'soft', 'soggy', 'solid', 'somber', 'sophisticated', 'sore', 'sorrowful', 'soulful', 'soupy', 'sour', 'Spanish', 'sparkling', 'specific', 'spectacular', 'speedy', 'spherical', 'spicy', 'spiffy', 'spirited', 'spiteful', 'splendid', 'spotted', 'spry', 'square', 'squeaky', 'squiggly', 'stale', 'starchy', 'starry', 'stationary', 'steel', 'sticky', 'stiff', 'stimulating', 'stingy', 'stormy', 'strange', 'strict', 'strident', 'striking', 'striped', 'strong', 'studious', 'stunning', 'stupendous', 'stupid', 'sturdy', 'stylish', 'subdued', 'submissive', 'sugary', 'superb', 'superficial', 'superior', 'supernatural', 'supportive', 'sure-footed', 'surprised', 'suspicious', 'svelte', 'sweaty', 'sweet', 'swift', 'sympathetic', 'talkative', 'tall', 'tame', 'tan', 'tangible', 'tart', 'tasty', 'tattered', 'taut', 'technically functional', 'technologically advanced', 'tender', 'tense', 'tepid', 'terrible', 'terrific', 'testy', 'thankful', 'theatrical', 'thick', 'thin', 'thirsty', 'thorny', 'thorough', 'thoughtful', 'threadbare', 'thrifty', 'thunderous', 'tidy', 'tight-fitting', 'tight', 'timely', 'tingling', 'tinted', 'tiny', 'tired', 'torn', 'tough', 'tragic', 'trained', 'traumatic', 'tremendous', 'triangular', 'tricky', 'trifling', 'trim', 'trivial', 'troubled', 'true', 'trusting', 'trustworthy', 'trusty', 'truthful', 'tubby', 'turbulent', 'twitching', 'twitchy', 'Ugandan', 'ugly', 'ultimate', 'unacceptable', 'unaware', 'unbreakable', 'uncomfortable', 'uncommon', 'unconscious', 'understated', 'uneducated', 'unequaled', 'uneven', 'unfinished', 'unfit', 'unfolded', 'unfortunate', 'unhappy', 'unhealthy', 'uniformed', 'unimportant', 'unique', 'united', 'unkempt', 'unknown', 'unlawful', 'unlined', 'unlucky', 'unnatural', 'unnecessary', 'unpleasant', 'unrealistic', 'unripe', 'unruly', 'unselfish', 'unsightly', 'unstable', 'unsteady', 'unsung', 'untidy', 'untimely', 'untried', 'untrue', 'unused', 'unusual', 'unwelcome', 'unwieldy', 'unwilling', 'unwitting', 'unwritten', 'upbeat', 'upright', 'upset', 'usable', 'used', 'useful', 'useless', 'utilized', 'utter', 'vacant', 'vague', 'vain', 'valid', 'valuable', 'vapid', 'velvety', 'venerated', 'vengeful', 'vicious', 'victorious', 'vigilant', 'vigorous', 'villainous', 'violent', 'violet', 'virtual', 'virtuous', 'visible', 'vivacious', 'voluminous', 'wan', 'warlike', 'warm', 'warmhearted', 'warped', 'wary', 'wasteful', 'watchful', 'waterlogged', 'watery', 'wavy', 'weak', 'wealthy', 'weary', 'webbed', 'wee', 'weekly', 'weepy', 'weighty', 'weird', 'welcome', 'well-animated', 'well-documented', 'well-drawn', 'well-educated', 'well-groomed', 'well-informed', 'well-known', 'well-off', 'well-to-do', 'wet', 'whimsical', 'whispering', 'white', 'whole', 'wicked', 'wide-eyed', 'wide', 'wiggly', 'wild', 'wilted', 'winged', 'wiry', 'wise', 'witty', 'woeful', 'wonderful', 'wooden', 'woozy', 'wordy', 'worldly', 'worried', 'worrisome', 'worthless', 'worthwhile', 'worthy', 'wrathful', 'wretched', 'writhing', 'wry', 'yawning', 'yellow', 'yellowing', 'young', 'youthful', 'yummy', 'zany', 'zealous', 'zesty', 'zigzag', 'zigzagging']
running = True
language = "en"
score = 0
while running == True:
    word = random.choice(words)
    word = word.lower()
    obj = gTTS(text = word, lang = language, slow = False)
    obj.save(word+".mp3")
    get = ""
    while get == "" or get == None or get == '':
        os.system("clear")
        playsound(word+".mp3")
        get = input("How do you spell that word? ")
    if get == word:
        score += 1
    elif get == "exit":
        break
    else:
        score = score
    os.remove(word+".mp3")
print("You got: " + str(score) + " points")