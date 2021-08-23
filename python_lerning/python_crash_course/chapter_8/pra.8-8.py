#pra.8-8
def make_album(singer_name,album_name):
    #info about an album
    
    
    info = {'Singer_name':singer_name,'Album_name':album_name}
   
    return info

while True:
    print("\nPlease tell me some info about the album:")
    print("(Enter 'q' at any time to quit)")
    singer = input("Singer's name:")
    if singer == 'q':
        break
    album = input("Album's name:")
    if album == 'q':
        break

    infos = make_album(singer,album)

    print(infos)
