def read_preferences(filename):
    '''
    whoever wrote this write your name
    '''
    dic = {}
    with open(filename, 'r') as file:
        for line in file:
            [username, singers] = line.strip().split(":")
            singersList = singers.strip().split(",")
            dic[username.rstrip()] = singersList
    return dic

def write_preferences(filename):
    '''
    whoever wrote this write your name
    '''
    with open(filename, 'w') as file:
        for line in file:
            username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
            singersList = input("Enter an artist that you like (Enter to finish) ")
            file.write(username + ":" + singersList)
    filename.close()

def showMenu():
    '''
    whoever wrote this write your name
    '''
    print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np -  Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")
    response = input()
    return response
    
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
    "Hidden Powers$": ["Baby Metal", "FLOW", "Spyair", "Vipera", "something"],
    "Sappho of Lesbos": ["Anna Kendrick", "Kerkylas Of Andros", "Sara Bareilles"],
    "Steph Oro": ["Fun.", "Gotye", "Sara Bareilles"]
}

dict2 = {}

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
            pass
        elif option == "p":
            pass
        elif option == "h":
            popular_score(data)
        elif option == "m":
            most_likes(data)
            
        option = showMenu()
    # TODO: save file after completion
main()

