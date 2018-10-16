def make_album(singer_name,album_name,number=''):
    pt={'singer':singer_name,'album':album_name}
    if number:
        pt['number']=number
    return pt

while True:
    singername=input('singer_name:')
    if singername=='q':
        break
    albumname=input('album_name:')
    if albumname=='q':
        break
    ptt=make_album(singername,albumname)
    print(ptt)



