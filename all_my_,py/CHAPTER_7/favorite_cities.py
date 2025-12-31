# THIS IS ABOUT LEARING THE __init__ FUNKTION


class Student:
    def __init__(self, name, year, gpa, enrolled):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(year, int):
            raise TypeError("year must be an integer")

        if not isinstance(gpa, (int, float)):
            raise TypeError("gpa must be a number (int or float)")

        if not isinstance(enrolled, bool):
            raise TypeError("enrolled must be a boolean (True or False)")

        self.name = name
        self.year = year
        self.gpa = float(gpa)
        self.enrolled = enrolled


daniel = Student("Daniel Li", 10, 4.0, True)


JOH = Student('joh',11,2.9,True)


print(vars(JOH))



class city:
    def __init__(self, name, country, population, landmarks):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(country, str):
            raise TypeError("country must be an integer")

        if not isinstance (population, (int, float)):
            raise TypeError("population must be a number (int or float)")

        if not isinstance(landmarks, list) or not all(isinstance(item, str) for item in landmarks):
             raise TypeError("landmarks must be a list of strings")


        self.name = name
        self.country = country
        self.population = round(population,2)
        self.landmarks = landmarks          
    
    
HOME_TOWN = city('londen','bg',2.33,['buckinghempales','londen bridge '])  
NEW_YOURK = city('New yourk','USA',8.47,['tatue of Liberty','Empire State Building'])

print(vars(NEW_YOURK))
print(vars(HOME_TOWN))