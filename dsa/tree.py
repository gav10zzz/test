class tree:
   def __init__(self,data):
      self.data=data
      self.children=[]
      self.parent=None

   def add_child(self,child):
      child.parent=self
      self.children.append(child)

   def starttree(self):
      human=tree("Human")
      male=tree("Male")
      female=tree("Female")
      human.add_child(male)
      human.add_child(female)

      father=tree("Father")
      brother=tree("Brother")

      mother=tree("Mother")
      sister=tree("Sister")

      male.add_child(father)
      male.add_child(brother)
      female.add_child(mother)
      female.add_child(sister)


if __name__=="main":
   obj=starttree()


   
      

