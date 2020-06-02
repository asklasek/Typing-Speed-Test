''' v.1.0: App created to display a passage from a famous book, have a user type the passage as fast and accurate as they can,
           determine the speed and accuracy of the user, and display the results to the user.
           \Future versions to incorporate a 95% accuracy requirement, leaderboard, saved user files, and multiple uses per run of the app. '''

import time
import sys
import random
import difflib


def main():
    
    # Print opening visuals.
    opening()
    
    # Create a User object.
    user=User(challengePassage())
    
    # Display passage to the user that will be typed.
    print()
    print(user.getChallenge())
    print("\n\n")
    
    # Countdown to start; loop with sleep crashes in windows so had to write it out.  :(
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    # The user inputs the shown passage.
    print("Go!\n\nInput: ", end="")
    user.setStartTime(time.time())  # record start time.
    entry = input()
    while len(entry) < 10: # If entry is less than 1 second, calc exceptions occur.
        print("\nInput: ", end="")
        entry = input()

    # user input, end time, and time taken are set in User object.
    user.setInput(entry)
    user.setEndTime(time.time())
    user.setTime()
    
    # Calculations are performed and added to User object.
    errorCalc(user)
    user.setWPM()
    
    # Display results to user.
    print(user)
    input("\n\nPress 'Enter' to quit")
    sys.exit()

''' Class to hold the user;s information throughout the apps lifecycle ''' 
class User:

    def __init__(self, challenge):
        self.errors__ = 0
        self.input__ = ""
        self.startTime__ = 0
        self.endTime__ = 0
        self.time__ = 0
        self.wpm__ = 0
        self.percCorrect__ = 0
        self.challenge__ = challenge
        self.wordCount__ = len(self.challenge__.split())
        
    # Getters
    def getErrors(self): return self.errors__
    def getInput(self): return self.input__
    def getTime(self): return self.time__
    def getWPM(self): return self.wpm__
    def getPercCorrect(self): return self.percCorrect__
    def getWordCount(self): return self.wordCount__
    def getChallenge(self): return self.challenge__

    # Setters
    def setErrors(self, x): self.errors__ = x
    def setInput(self, s): self.input__ = s.rstrip()
    def setStartTime(self, x): self.startTime__ = x
    def setEndTime(self, x): self.endTime__ = x
    def setPercCorrect(self, x): self.percCorrect__ =  x
    def setWordCount(self, x): self.wordCount__ = x
    def setChallenge(self, s): self.challenge__ = s

    # Setters that calculate
    def setTime(self): self.time__ = int(self.endTime__ - self.startTime__)
    def setWPM(self): self.wpm__ = int(self.wordCount__ * (60 / self.time__))

    # Incriment error count
    def addErrors(self, x): self.errors__ += x

    # Returns vital info from User
    def __str__(self):
        return "\n\t*************\n\t***RESULTS***\n\t*************\n\nTime: " \
               + str(self.time__) + " sec\nWPM: "+ str(self.wpm__) \
               + "\nErrors: " + str(self.errors__) + "\nPercent Match: " + str(self.percCorrect__) + "%"

''' Displays a fancy ASCII visual about the app's purpose and what to do. '''
def opening():
    top = "***Discover how fast you can type!***"
    starRow = ""
    for x in range(len(top)):
        starRow += "*"

    print("\n\t" + starRow + "\n\t" + top + "\n\t" + starRow + "\n\nAfter the countdown, type the displayed sentence.")
    time.sleep(5)

''' Takes a user object and determines the errors between the user input and original passage
    by utilizing difflib sequence matcher.'''
def errorCalc(user):
    # Calculate percent match between the input string and test string.
    s = difflib.SequenceMatcher(None, user.getChallenge(), user.getInput(), False)
    user.setPercCorrect(int(s.ratio()*100))

    # Calculate number of errors between the input string and test string.
    # "-" signifies missing char, "+" signifies added char.
    d = difflib.Differ()
    # list of strings with len=3. 1st index is " ", "+", or "-", 2nd index is " ", 3rd index is char"
    result = list(d.compare(user.getChallenge(), user.getInput()))

    for x in range(len(result)):
        try:
            # if wrong char, system will give - and +; this if ensures it isn't counted twice.
            if result[x][0] == "-" and result[x+1][0] != "+":
                user.addErrors(1)
            # always counts +
            if result[x][0] == "+":
                user.addErrors(1)
        except IndexError: # Most likely not required, but in case a scenario was forgotten and an exception occurs.
            user.addErrors(1)

    # Code to print where errors occured in user input (if ever needed/wanted).
    '''for item in result:
        if item == '   ':     # make space into 1 space instead of 3
            print(' ', end='')
        else:                 # print char
            print(item.lstrip(), end='')
            if item[-1] == ".":    # newline for end of a sentence
                print()'''

# Random passage is returned from a list of famous literature passages.
def challengePassage():
    passageList = ["In the late summer of that year we lived in a house in a village that looked across the river and the plain to the mountains. In the bed of the river there were pebbles and boulders, dry and white in the sun, \
and the water was clear and swiftly moving and blue in the channels. Troops went by the house and down the road and the dust they raised powdered the leaves of the trees. The trunks of the trees too were dusty and the leaves fell \
early that year and we saw the troops marching along the road and the dust rising and leaves, stirred by the breeze, falling and the soldiers marching and afterward the road bare and white except for the leaves.",
                   "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the \
season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way — in short, the period \
was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.",
                   "Dark spruce forest frowned on either side of the frozen waterway. The trees had been stripped by a recent wind of their white covering of frost, and they seemed to lean toward each other, black and ominous, in \
the fading light. A vast silence reigned over the land. The land itself was a desolation, lifeless, without movement, so lone and cold that the spirit of it was not even that of sadness. There was a hint in it of laughter, but of a \
laughter more terrible than any sadness — a laughter that was mirthless as the smile of the Sphinx, a laughter cold as the frost and partaking of the grimness of infallibility. It was the masterful and incommunicable wisdom of \
eternity laughing at the futility of life and the effort of life. It was the Wild, the savage, frozen-hearted Northland Wild.",
                   "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things \
which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly - Tom's Aunt Polly, she is - and Mary, and the \
Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
                   "I will be very careful the next time I fall in love, she told herself. Also, she had made a promise to herself that she intended on keeping. She was never going to go out with another writer: no matter how \
charming, sensitive, inventive or fun they could be. They weren’t worth it in the long run. They were emotionally too expensive and the upkeep was complicated. They were like having a vacuum cleaner around the house that broke all \
the time and only Einstein could fix it. She wanted her next lover to be a broom."
                   "This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. \
It’s like a stuck record. The ear demands some variety. Now listen. I vary the sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of \
medium length. And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, \
the crash of the cymbals–sounds that say listen to this, it is important.",
                   "Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every \
funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off—then, I \
account it high time to get to sea as soon as I can."]
    random.shuffle(passageList)
    return passageList.pop()

''' Start app '''
if __name__ == "__main__":
    main()
