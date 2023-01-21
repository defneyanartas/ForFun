#!/usr/bin/env python3
"""
Script name: Secret Santa
Author: Defne YANARTAS 
Created: 2022-10-28

Usage: python 
   
Description: Program takes a list of participant names and assigns one person
            to another randomly.
Input: list of names
Output: text files named with participant name and containing the name that 
        the person is assigned to a get a gift for
Procedure:
    0. Import modeules and prep the participant lists.
    1. Use shuffle to reorganize the receivers list.
    2. Print the matches to outputfiles.
    
User defined function: None
Modules: random
              
Quality Control:
    - No QC because I am capable of making a list of names without messing it up... or am I? 
    
"""
#%% 0. Import modules, prepare the participant list
import random                                                                   #I will not set a seed so that people cant track who got their gift.
givers_list=["Jiheun","Huy", "Defne","Saghar","Joan","Markus","Iñaki", "Dominique", "Tamim", "Nikhilesh","Felicia","Axel","Laura","Eleni","Robin"]
receivers_list=["Jiheun","Huy", "Defne","Saghar","Joan","Markus","Iñaki", "Dominique", "Tamim", "Nikhilesh","Felicia","Axel","Laura","Eleni","Robin"]

#%% 1. Shuffle the list
while True:                                                                     #Make a while loop so that we keep going until the shuffling gets all the indices in two lists different from eachother, to avoid a person from getting a gift for themselves.
    for i in range(len(givers_list)):                                           #Iterate with indices in the givers list
        if givers_list[i]==receivers_list[i]:                                   #Compare the same index in both lists.
            random.shuffle(receivers_list)                                      #If at any point they are the same, we need to shuffe the whole list again.
            break                                                               #And we need to break so that we can start the iteration from the beginning.
    break                                                                       #If we dont find anythng the same during the for loop, while loop will reach the break.

#%% 2. Print the results
for i in range(len(givers_list)):                                               #We will iterate in the list again to create files.
    with open(f"{givers_list[i]}.txt", "w") as out:                             #For everyparticipant will have a text file with their on it.
        print(f"{givers_list[i]} gets a gift for {receivers_list[i]}\nPrice: rnorm(1,mean=50,sd=low) & Price<100\nIf you got Joan, dont get a chocolate\nHandmade gifts are the best\nClimate change shenanigans are real so second-hand gifts are highly appreciated\nBioinformatistmas day preliminary date: 2022-12-09 Friday, we can change if necessary\nLove y'all\n#pressrelease", file=out)#The file will contain the name of the person they will get the gift for.

