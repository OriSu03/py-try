def make_album(singer_name,album_name,number=''):
    pt={'singer':singer_name,'album':album_name}
    if number:
        pt['number']=number
    return pt

ptt=make_album('lee','ailee')
print(ptt)
