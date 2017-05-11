from pygame import mixer
#mixer.init()
#mixer.music.load('Path')
#mixer.music.play()
#mixer.music.stop()
import webbrowser
import csv
import os

songs = []
name_pos = 0
link_pos = 1
song_header = ['Name','Link']

#def delete_song():
#    print("Deleting")

def save_song_list():
    A = sorted(songs,key = lambda x:(x[0]))
    f = open("mysongs.csv",'w',newline='')
    for item in A:
        csv.writer(f).writerow(item)
    f.close()

def load_song_list():
    if os.access("mysongs.csv",os.F_OK):
        f = open("mysongs.csv")
        for row in csv.reader(f):
            songs.append(row)
        f.close()

def show_songs():
    show_song(song_header,"")
    index = 1
    for song in songs:
        show_song(song,index)
        index = index + 1
    print("Do you wanna play the song y/n?")
    ch = input()
    if ch == 'y':
        print("Which song do you wanna play ? ")
        ino = int(input("Enter index number: "))
        play_in_browser(ino)

def play_in_browser(ino):
    B = songs[ino-1]
    url = B[1]
    webbrowser.open_new(url)
    

def show_song(song,index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index,song[name_pos],song[link_pos]))


def create_song():
    print("Enter the data for a new song:")
    newname = input("Enter name: ")
    newsong_link = input("Enter youtube link: ")
    song = [newname,newsong_link]
    songs.append(song)
    
    
def menu_choice():
    print("Choose one of the following options")
    print("   s)Show")
    print("   n)New")
 #   print("   d)Delete")
    print("   q)Quit")
    choice = input("Choice: ")
    if choice.lower() in ['n','s','q']:
        return choice.lower()
    else:
        print(choice +"?" + "That is an invalid option!!!")
        return None

def main_loop():

    load_song_list()

    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print("Exiting..")
            break
        elif choice == 'n':
            create_song()
        elif choice == 'd':
            delete_song()
        elif choice == 's':
            show_songs()
        else:
            print("Invalid choice.")

    save_song_list()

if __name__ == '__main__':
    main_loop()


        
