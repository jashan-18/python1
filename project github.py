# to declare a class employee which contains 2 methods: get_detail, forget the name ,employee_id,salary of employee and another method is print details
class employee:
    def get_details(self,n,i,s):
        self.name=n
        self.id=i
        self.salary=s
    def print_details(self):
        return self.name+' '+self.id+' '+self.salary
e1=employee()
e1.get_details('Mohit','01','1234546543')
e2=employee()
e2.get_details('Rohit','02','9876543')
print(e1.print_details())
print(e2.print_details())
