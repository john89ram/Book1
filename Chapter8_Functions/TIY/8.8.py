# User Album - Extend the lab in 8.7 and create a while loop to allow users to create 
    # their own album. Store that information and when completed they can return and 
    # print the dictionaries information. 

def make_album(artist_name, album_title):
    """This is a simple function to create a dictionary with album information."""
    album_info = { 'artist name': artist_name, 'album title': album_title}
    return album_info

while True:
    print(f"\nPlease enter the album information you would like to create.")
    print(f"(enter 'q' at any time to quit)")
    art_name = input("Artist Name: ")
    if art_name == 'q':
        break
    alb_name = input("Album Name: ")
    if alb_name == 'q':
        break

    user_album = make_album(art_name, alb_name)
    print(f"\n{user_album}")
    print("\nWould you like to create another album?")
    print("Press 'y' for yes and 'q' to quit.")
    another_album = input('y/q: ')
    if another_album == 'y':
        continue
    if another_album == 'q':
        break