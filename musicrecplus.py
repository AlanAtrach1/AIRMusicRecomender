def read_preferences(filename):
    dic = {}
    with open(filename, 'r') as file:
        for line in file:
            [username, singers] = line.strip().split(":")
            singersList = singers.strip.split(",")
            dic[username.rstrip()] = singersList
    return dic

def write_preferences(filename):
    
    with open(filename, 'w') as file:
        for line in file:
            username = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
            singersList = input("Enter an artist that you like (Enter to finish) ")
            file.write(username + ":" + singersList)
    filename.close()

def showMenu():
    print("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np= Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit")