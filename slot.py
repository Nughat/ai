import random

#runs with python3, not python, because of the use of random.choices 

stats = [] #list to store the number of plays until broke

def slot(): #function to record the number of plays
    coins = 10 #start with 10 coins
    symbols = ['A','B','C','D'] #list of symbols in slot machine
    sample = [] #list to generate the symbols that come up for 3 independent wheels
    num_plays = 0 #variable that keeps track of the plays before going broke

    while (coins >= 2): #while buy in can still be afforded
        sample = random.choices(symbols, k = 3) #run the slot machine and generate a sample
        coins = coins-2 #the cost of cranking the machine is 2 coins
        coins = check_sample(sample,coins) #call function to check if the sample is a win and if so, update the current coins value
        num_plays = num_plays + 1 #increment as the loop continues in order to keep track of how many plays have been made
         
    return num_plays #return the total number of times played before going broke

def check_sample(samplelist,coin): #function to check if the sample is a win and if so, add to the current coins value
    if (samplelist == ['A','A','A']): #A/A/A pays 2 * twenty times = 40
        coin = 40+coin #add 40 to the current coins value
    if (samplelist == ['B','B','B']): #B/B/B pays 2 * fifteen times = 30
        coin = 30+coin #add 30 to the current coins value
    if (samplelist == ['C','C','C']): #C/C/C pays 2 * five times = 10
        coin = 10+coin #add 10 to the current coins value
    if (samplelist[0] == 'D'): #D//
        if(samplelist[1] == 'D'): #D/D/
            if samplelist[2] == 'D': #D/D/D pays 2 * three times = 6
                coin = 6+coin #add 6 to the current coins value
            elif samplelist[2] != 'D': #D/D/? pays 2 twice = 4
                coin = 4+coin #add 4 to the current coins value
        elif(samplelist[1] != 'D'): #D/?/? pays 2 
            coin = 2+coin #add 2 to the current coins value
    return coin #return updated coins value
2
for i in range(1000): #run the whole game 1000 times
    stats.append(slot()) #each time record the number of plays in stats
stats.sort() #sort stats to find median and mean

median = (stats[490]+stats[500])/2 #calculate the median using the 499th and 500th element of stats
mean = sum(stats)/1000 #calculate the mean by summing all of stats's values and dividing by 1000
print("mean: ", mean, "median: ", median) 
#example output: mean:  113.841 median:  8.0

#The median is the more consistent measure central tendency. It is almost always 8, and at times when it is not, it 
#is 7.5 or 7. During testing, all elements of stats were printed out, and every time there was a similar number of 5s, 7s, and 8s, among 
#other numbers that were less than 10. At the other end of the list, higher numbers showed more variation, with some numbers reaching 
#the thousands. Because numbers in the lower/mid area are consistent, the median is also consistent. On the other hand, the mean 
#is more varied as it usually ranges from 80-150. This likely has to do with the fact that it 
#accounts for the outliers more than the median does, and is influenced more by the less frequent values that land in the 
#thousands and above. It is concerning that the median is so much lower than the mean for most runs. When analyzing stats, 
#it appears that the median is the better measure because a large chunk of the values are below 100, the majority
#even below 10, whereas a small chunk at the bottom is above 100. 