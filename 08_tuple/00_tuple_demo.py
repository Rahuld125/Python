album = "Aashiqui 2", 2013, "Arijit Singh", (
    (1, "Tum hi ho"),
    (2, "Chahun Mai Ya Na"),
    (3, "Meri Aashiqui"),
    (4, "Aasan Nahin Yahaan"))

title, year, singer, songs = album
print("Title:", title)
print("Year:", year)
print("Singer:", singer)
for track in songs:
    songno, songname = track
    print("Song number:", songno, "Song name:", songname)
