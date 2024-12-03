'''
Created on 12/04/2024
@author:   Alan Atrach, Ian Chao, Ruhi Ajinkya
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Group Project
'''


import os

EXTRA_CREDIT = False

def read_preferences(file):
    '''
    Ruhi Ajinkya
    Open file and read user preferences 
    '''
    dic = {}
    with open(file, "r") as file:
        for line in file:
            [username, singers] = line.strip().split(":")
            singersList = singers.strip().split(",")
            dic[username.rstrip()] = singersList
    return dic

def enter_preferences():
    '''
    Ruhi Ajinkya
    Open file to prompt the user for their preferences, and then write user preferences
    '''
    singerList = []
    while(True):
        singer = input("Enter an artist that you like (Enter to finish):\n")
        if singer == "":
            break
        else:
            singer = singer.title()
            singerList.append(singer)
    singerList.sort()
    return singerList


def showMenu():
    '''
    Ruhi Ajinkya
    Menu to show user what options they have
    '''
    #TODO maybe put delete and show on menu?
    print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")
    if EXTRA_CREDIT:
        print("d - Delete preference\ns - Show preferences")
    response = input()
    return response
    
def getRecommendations(currentUser, dict):
    '''
    Ian Chao
    Given the current user and the dictionary containing all user info, finds the most similar user and prints a list of unique artists.
    '''
    if currentUser not in dict:
        print("No recommendations available at this time.")
    currentUserPref = dict[currentUser]
    matches = 0
    uniques = []
    for user in dict.keys():
        if user == currentUser or user[-1] == "$":
            continue
        artists = dict[user]
        numMatches = 0
        currentUniques = []
        for artist in artists:
            if artist in currentUserPref:
                numMatches += 1
            else:
                currentUniques.append(artist)
        if numMatches > matches and len(currentUniques) > 0:
            matches = numMatches
            uniques = currentUniques
    if uniques == []:
        print("No recommendations available at this time.")
    uniques.sort()
    for artist in uniques:
        print(artist)
           
def showPopularArtists(dict):
    '''
    Ian Chao
    Given the dictionary containing all user info, finds the top 3 most popular artists.
    '''
    artistCounts = {}
    for user in dict.keys():
        if user[-1] == "$":
            continue
        artists = dict[user]
        for artist in artists:
            if artist in artistCounts:
                artistCounts[artist] += 1
            else:
                artistCounts[artist] = 1
    mostPopular = []
    for artist in artistCounts.keys():
        if len(mostPopular) == 3:
            break
        most = artist
        count = artistCounts[artist]
        for otherArtist in artistCounts.keys():
            if otherArtist == artist:
                continue
            if artistCounts[otherArtist] > count:
                most = otherArtist
                count = artistCounts[otherArtist]
        if most in mostPopular:
            continue
        else:
            mostPopular.append(most)
    for artist in mostPopular:
        print(artist)

def popular_score(dict):
    '''
    Alan Atrach
    Given the dictionary containing all user info, prints the highest number of likes of an artist
    '''
    artistLikes = {}
    count = 0
    for user in dict:
        if user[-1] == "$":
            continue
        for artist in dict[user]:
            if artist in artistLikes:
                artistLikes[artist] += 1
            else:
                artistLikes[artist] = 1
    for artist in artistLikes:
        likes = artistLikes[artist]
        if artistLikes[artist] > count:
            count = likes
    if count == 0:
        print("Sorry, no user found.")
    else:
        print(count)
    
    
def most_likes(dict):
    '''
    Alan Atrach
    Given the dictionary containing all user info, finds the person who likes the most people
    '''
    userList = []
    likes = 0
    for user in dict:
        if user[-1] == "$":
            continue
        amount = len(dict[user])
        if amount > likes:
            likes = amount
            userList.clear()
            userList.append(user)
        elif amount == likes:
            userList.append(user)
    if likes == 0:
        print("Sorry, no user found.")
    else:
        for user in userList:
            # print(user + "\n") # can't have newline for one person
            print(user)
            
def delete(currentUser, dict):
    '''
    Alan Atrach
    delets a specified artist from the user's preferences
    '''
    artists = dict[currentUser]
    while len(artists) != 0:
        print("Type the number correlated to the artist to delete:\n")
        for i in range (0, len(artists)):
            print(f"{i + 1}. {artists[i]}")
        response = input()
        if response == "":
            return
        elif not response.isdigit() or int(response) > len(artists) or int(response) < 1:
            print("invalid input, try again or press enter to end")
        else:
            artists.pop(int(response) - 1)
            print(f"artist {response} has been removed")
    print("No artists in user preference")

def showPreferences(currentUser, dict):
    '''
    Ian Chao
    Prints the current user's preferences
    '''
    preferences = dict[currentUser]
    for artist in preferences:
        print(artist)
        
    
    
    

def save(data, file):
    '''
    Ruhi Ajinkya
    Uses data that the user inputs to add to the text file
    '''
    sortedData = list(data.keys())
    sortedData.sort()
    
    with open(file, "w") as file:
        for user in sortedData:
            file.write(user + ":"+",".join(data[user]) + "\n")
            
#TODO: delete these when done, i found it useful to have them here so you guys can use it if yall want

#THIS IS FOR TESTING PURPOSES
dict = {
    "Anne Adamant": ["50 Cent", "Eminem", "Lil Wayne", "Snoop Dog"],
    "Bacon Bryant$": ["Britney Spears", "Gotye", "Kesha", "TMBG"],
    "Caesar Zeppeli": ["Fun.", "Gotye", "Sara Bareilles"],
    "Hidden Powers": ["Baby Metal", "FLOW", "Spyair", "Vipera", "something"],
    "Sappho of Lesbos": ["Anna Kendrick", "Kerkylas Of Andros", "Sara Bareilles"],
    "Steph Oro": ["Fun.", "Gotye", "Sara Bareilles"]
}

dict2 = {}

dict3 = {"Steph Oro": ["Fun.", "Gotye", "TMBG"]}

# popular_score(dict2)

def main():
    '''
    main function, utilizes all methods
    '''
    filename = "musicrecplus.txt"
    if not os.path.exists(filename):
        file = open(filename, "w")
    
    data = read_preferences(filename)

    username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    # Check if the user is in the file, if not ask them to enter preferences
    if not username in data:
        data[username] = enter_preferences()

    option = showMenu()
    #TODO: put appropriate methods here
    while option != "q":
        # print(data)
        if option == "e":
            data[username] = enter_preferences()
        elif option == "r":
            getRecommendations(username, data)
        elif option == "p":
            showPopularArtists(data)
        elif option == "h":
            popular_score(data)
        elif option == "m":
            most_likes(data)
        elif option == "d" and EXTRA_CREDIT:
            delete(username, data)
        elif option == "s" and EXTRA_CREDIT:
            showPreferences(username, data)
        
        
        option = showMenu()
    
    
    
    save(data, filename)

main()

