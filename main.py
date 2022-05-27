class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
    #Define the attributes for this class
        self.Name= name
        self.Age= age
        self.Tracks = []
        self.Tracks.append(tracks)
        self.Score= score
    #Define methods  for the the classes    
    def change_name(self, new_name):
        self.Name= new_name

    def change_age(self, new_age):
        self.Age= new_age

    def add_track(self, new_track):
        self.Tracks.append(new_track)

    def get_score(self):
        return self.Score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob)
print(Bob.Name)
print(Bob.Age)
print(Bob.Tracks)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob)
print(Bob.Name)
print(Bob.Age)
print(Bob.Tracks)

      
