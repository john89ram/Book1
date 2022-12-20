# Album - Write a function called make_album() that builds a dictionary with the
    # artist_name and the album_title. The function should be able to return the 
    # dictionary itself. Then make 3 different dictionaries with it and print them.

def make_album(artist_name, album_title):
    """This is a simple function to create a dictionary with album information."""
    album_info = { 'artist name': artist_name, 'album title': album_title}
    return album_info

num1_album = make_album('Drake & 21 Savage', 'Her Loss')
num2_album = make_album('Taylor Swift', 'Midnight')
num3_album = make_album('Lil Baby', "It's Only Me")

top_list = [num1_album, num2_album, num3_album]

for album in top_list:
    print(album)
