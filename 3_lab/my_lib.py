print("Це виведеться при запуску на пряму та при здійснення імпорту бібліотеки!")
# Тут ми тільки ініціалізуємо нашу бібіліотеку без виконання коду.
class AnimeClabLib:
   unic_favorite_anime = set()
   
   def __init__(self, name:str, surname:str, favorite_anime:set, favorite_characters:dict=None) -> None:
      # Це просто прінт щоб ми знали що викликався нас конструктор
      print(f"Ура в нас є новий учасник: {name} {surname}!")
      self.name = name # кожне поле обєкта називається атрибутом
      self.surname = surname
      self.favorite_anime = favorite_anime
      self.favorite_characters = favorite_characters
      self.rank = None
      self.user = self.define_user(name, surname)
      AnimeClabLib.unic_favorite_anime = AnimeClabLib.unic_favorite_anime.union(favorite_anime) if favorite_anime != None else AnimeClabLib.unic_favorite_anime

   
   @property
   def full_name(self):
      # тут також можуть бути якісь команди
      return f"{self.name} {self.surname}"

   @property
   def anime_amount(self):
      return len(self.favorite_anime)
   
   @property
   def rank_beginner(self):
      return "Початківець анімешник"

   @property
   def rank_pro(self):
      return "Анімешник задрот"
   
   def add_new_favorite_anime(self, title:str):
      print(f"{self.name} має нове улюблене аніме: {title}")
      self.favorite_anime.add(title)
      AnimeClabLib.unic_favorite_anime.add(title)
   
   def remove_favorite_anime(self, title:str):
      print(f"Чомусь {self.name}у більше не пободається аніме: {title}")
      self.favorite_anime.remove(title)

   def count_favorite_animes(self):
      return len(self.favorite_anime)
   
   @staticmethod
   def invite_frient(name:str):
      print(f"Запрошую {name} до нас у клуб. Ми ділимось враженнями про найкращі аніме!")

   @staticmethod
   def define_user(name:str, surname:str):
      return f"{name} на прізвисько {surname}"
   
   @classmethod
   def new_participant(cls, name:str, surname:str):
      return cls(name, surname, favorite_anime=None)


if __name__ == "__main__":
    # тут повинен бути код роботи з нашою бібліотекою
    print("Файл бібліотеки був викликаний напряму!")
    # тут навіть можна створювати обєкти та працювати з ними
    bb = AnimeClabLib("Богдан", "Bobas", set(["Сходження в тіні",]), {"Людина Бензопила": "Пауер"})
    print(f"Був створений новий обєкт: {bb.name} який любить наступні аніме: {bb.favorite_anime}")
