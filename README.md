# Juke-box
A very very basic music-player.

This is a small attempt made to understand the working of a music-player application.
**Work under progress**

It is slightly different than our standard music players in such a way that this does not play songs from the stored songs, instead it plays the youtube video of it's respective song name.

The program asks for 3 choices :
1. Display list of songs.
2. Add new song.
3. Quit the application.

The first option displays the list of the songs as follows :


#%%

Choose one of the following options

s)Show
n)New
q)Quit
Choice: s
Name                              Link
1  Ae dil hai mushkil    https://youtu.be/vUCM_0evdQY
2  Agar tum saath ho     https://youtu.be/6SGRn9OHtFY
3  Bolna                 https://youtu.be/GYFDRoJtfGM
4  Buddhu sa mann        https://youtu.be/i0AUEswUayo
5  Bulleya               https://youtu.be/wTgrZE9RWNY
6  Shape of you          https://youtu.be/JGwWNGJdvx8
Do you wanna play the song y/n?
#%%


If you press 'n', the program will comtinue to ask to choose from the options.

If you want to play any of the songs from the list, just press 'y' and it will play the youtube video in your default browser.
After pressing 'y', the index number of the song from the given list has to be entered by the user. Once the index number has been entered, the desired song will be played in the browser in a new tab.

#%%
Do you wanna play the song y/n?
y
Which song do you wanna play ? 
Enter index number: 6
#%%

Voila!! it works.

On choosing the second option, we can add any song we want.
On selecting this option, the program will ask to enter the name of the song and its youtube link.
(I know this is tedious, but I haven't made a web crawler or an audio site like Saavn)


#%%
Choose one of the following options
   s)Show
   n)New
   q)Quit
Choice: n
Enter the data for a new song:
Enter name: We dont talk anymore
Enter youtube link: https://youtu.be/3AtDnEC4zak
Choose one of the following options
   s)Show
   n)New
   q)Quit
Choice: s
     Name                              Link
  1  Ae dil hai mushkil    https://youtu.be/vUCM_0evdQY
  2  Agar tum saath ho     https://youtu.be/6SGRn9OHtFY
  3  Bolna                 https://youtu.be/GYFDRoJtfGM
  4  Buddhu sa mann        https://youtu.be/i0AUEswUayo
  5  Bulleya               https://youtu.be/wTgrZE9RWNY
  6  Shape of you          https://youtu.be/JGwWNGJdvx8
  7  We dont talk anymore  https://youtu.be/3AtDnEC4zak
#%%

And don't forget to quit the application or the song added won't be added in the list.
All the songs added are stored in a CSV file which are stored and retrieved in a sorted order.

The third option to choose is to quit.
But hey, when you listen to songs, do you ever wish to ??

