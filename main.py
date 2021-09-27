def define(word):
    if word == "cat":
        return "a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."
    elif word == "dog":
        return "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice."
    elif word == "cow":
        return "a fully grown female animal of a domesticated breed of ox, kept to produce milk or beef."
    elif word == "chicken":
        return "a domestic fowl kept for its eggs or meat, especially a young one."
    elif word == "wolf":
        return "a wild carnivorous mammal of the dog family, living and hunting in packs. It is native to both Eurasia and North America, but has been widely exterminated."
    elif word == "fox":
        return "a carnivorous mammal of the dog family with a pointed muzzle and bushy tail, proverbial for its cunning."
    elif word == "coyote":
        return "a wild dog that resembles the wolf, native to North America."
    elif word == "rabbit":
        return "a burrowing, gregarious, plant-eating mammal with long ears, long hind legs, and a short tail."
    elif word == "fish":
        return "a limbless cold-blooded vertebrate animal with gills and fins and living wholly in water."
    elif word == "grass":
        return "vegetation consisting of typically short plants with long, narrow leaves, growing wild or cultivated on lawns and pasture, and as a fodder crop"
    else:
        return "I do not know the definition of that word."

inputWord = str(input("What word would you like me to define? "))
print(define(inputWord.lower()))