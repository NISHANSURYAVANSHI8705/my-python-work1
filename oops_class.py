#OOP's --->class object


# class Even_odd:
#     def get_num(self,n):
#         self.n=n
#     def cal(self):
#         if self.n % 2==0:
#             print("EVEN") 
#         else:
#             print("odd") 
# E1=Even_odd()
# E1.get_num(6)
# E1.cal()



class Student:
    def get_details(self,n,a,E):
        self.n=n
        self.a=a
        self.E=E
    def show_details(self):
        print("NAME OF STUDENT IS:",self.n)
        print("AGE OF STUDENT IS:",self.a)
        print("AGE OF ENROLLEMENT:",self.E)    
S1=Student()
S1.get_details("nishan","18","2000")        
S1.show_details()