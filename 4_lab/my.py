from jikanpy import Jikan
jikan = Jikan()

j = jikan.anime(54595, extension='episodes')
print(j)
for episode in j["data"]: 
    print(f"Епізод {episode['title']} має оцінку {episode['score']}")