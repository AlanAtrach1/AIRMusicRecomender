def read_preferences(filename):
    '''
    Ruhi Ajinkya
    Open file and read user preferences 
    '''
    dic = {}
    with open(filename, "r") as file:
        for line in file:
            [username, singers] = line.strip().split(":")
            singersList = singers.strip().split(",")
            dic[username.rstrip()] = singersList
    return dic

def write_preferences(filename):
    '''
    Ruhi Ajinkya
    Open file to prompt the user for their preferences, and then write user preferences
    '''
    with open(filename, "w") as file:
        for line in file:
            username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
            singersList = input("Enter an artist that you like (Enter to finish) ")
            file.write(username + ":" + singersList)
    filename.close()

def showMenu():
    '''
    Ruhi Ajinkya
    Menu to show user what options they have
    '''
    print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np -  Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")
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
        if user[len(user) - 1] == "$":
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
        if user[len(user) - 1] == "$":
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
            print(user + "\n")
         
            
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
    #TODO: implement proper text here
    
    # file = "musicrecplus.txt"
    # write_preferences(file)
    file = "musicrecplus_ex2_a.txt" #just testing out functionality, delete and replace with commented file for actual build
    data = read_preferences(file)
    option = showMenu()
    
    #TODO: put appropriate methods here
    while option != "q":
        if option == "e":
            pass
        elif option == "r":
            getRecommendations("Steph Oro", dict3)
        elif option == "p":
            showPopularArtists(dict3)
        elif option == "h":
            popular_score(data)
        elif option == "m":
            most_likes(data)
            
        option = showMenu()
    # TODO: save file after completion
main()

