all_people = []


class Person:
    def __init__(self, name, birth_year, gender,
                 father=None, mother=None): 
        [self.name, self.birth_year, self.gender, self.father,  
         self.mother] = [name, birth_year, gender, father, mother]
        all_people.append(self)


    def get_siblings(self, gender):
        siblings = set()
        for person in all_people:
            if person is self.father or person is self.mother:
                for person2 in all_people:
                    if (person2.father is person or
                        person2.mother is person):
                        if person2.gender == gender:
                            siblings.add(person2)
        if self in siblings:
            siblings.remove(self)
        return list(siblings)

           
    def get_brothers(self): 
        return self.get_siblings("M")

                        
    def get_sisters(self):
        return self.get_siblings("F")

        
    def children(self, gender="both"):
        children = set()
        if gender == "both":
            if self.gender == "M":
                for person in all_people:
                    if person.father is self:
                        children.add(person)
            if self.gender == "F":
                for person in all_people:
                    if person.mother is self:
                        children.add(person)
        else:
            if self.gender == "M":
                for person in all_people:
                    if (person.father is self and
                        person.gender == gender):
                        children.add(person)
            if self.gender == "F":
                for person in all_people:
                    if (person.mother is self and
                        person.gender == gender):
                        children.add(person)
        return list(children)
    
        
    def is_direct_successor(self, person):
        if self.gender == "M":
            if person.father is self:
                return True
        elif self.gender == "F":
            if person.mother is self:
                return True
        if person.gender == 'M':
            if self.father is person:
                return True
        elif person.gender == 'F':
            if self.mother is person:
                return True
        return False
    
    
    def __str__(self):
        if self.mother is not None and self.father is not None:
            return "{0}, {1}, {2}, father: {3},mother: {4} \n".format(self.name,
                self.birth_year,
                self.gender,
                self.father.name,
                self.mother.name )
        else:
            return "{0}, {1}, {2} \n".format(self.name,
                                             self.birth_year,
                                             self.gender)


    def has_children(self, child):
        if child.father is self:
            return True
        return False
