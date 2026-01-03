class employee:
    def __init__(self,name,id):

        self.name=name
        self.id=id
    def __del__(self):
            print("the employee has been deleted destructor is called")

el=employee("ram",1)
print("the name is", e1.name)
print("the id is", e1.id)    
del e1
#print("the name is", e1.name)
#print("the id is", e1.id)