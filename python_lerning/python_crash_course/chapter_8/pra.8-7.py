#pra.8-7
'''def make_album(singer_name,album_name):
    #info about an album
    info = {'Singer_name':singer_name,'Album_name':album_name}
    return info

album = make_album('Taylor Swift','Fearless')
print(album)

album = make_album('Burno Mars','Leave the door open')
print(album)

album = make_album('Bob Dylon','Tempest')
print(album)'''


#album with chooseable index of songs number
def make_album(singer_name,album_name,songs_num = None):
    #info about an album
    info = {'Singer_name':singer_name,'Album_name':album_name}
    if songs_num:
        info['Songs_number'] = songs_num
    return info

album = make_album('Taylor Swift','Fearless')
print(album)

album = make_album('Burno Mars','Leave the door open',1)
print(album)


