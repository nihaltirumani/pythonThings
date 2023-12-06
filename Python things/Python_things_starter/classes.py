class person:
    def __init__(self, name, age, occupation, person_id) :
        self.name = name
        self.age = age
        self.occupation = occupation
        self.person_id = person_id
    
    def show(self):
        return self.name, self.age, self.person_id
    
    def introduction_person(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old. My occupation is {self.occupation} My ID is {self.person_id}.")

    def get_more_info(self, hobbies, fav_food, fav_sport):
        self.hobbies = hobbies
        self.fav_food = fav_food
        self.fav_sport = fav_sport

    def show_more_info(self):
        return self.hobbies, self.fav_food, self.fav_sport
    
    def more_info(self):
        if hasattr(self, 'hobbies') and hasattr(self, 'fav_food') and hasattr(self, 'fav_sport'):
            print(f"My hobby is {self.hobbies}. My favourite food is {self.fav_food} and favourite sport is {self.fav_sport}.")
        else:
            print(f"No more information about {self.name}.")

person1 = person("Nihal", 11, 1025)
person2 = person("Varun", 11, 1079)
person1.introduction_person()
person2.introduction_person()
person1.get_more_info("playing key board", "pizza", "Basketball")
person1.more_info()
person2.more_info()