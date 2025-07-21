class ott_subs:
    def __init__(self,subs_id,plan,total_pay):
        self.id=subs_id
        self.plan=plan
        self.total=total_pay

    def subscribe(self):
        print(f"Subscribe with {self.id}id successfully to {self.plan}")

    def unsubscribe(self):
        print(f"Unsubscribe with {self.id}id successfully to {self.plan}")

class premium_subs(ott_subs):    #child class
    def __init__(self,subs_id,plan,total_pay,screen):
        super().__init__(subs_id,plan,total_pay)        #inheritance of ott_subs
        self.max_screen=screen

    def max_no_screen(self,screen):
        print(f"Max no screen successfully to {self.max_screen}")


s=int(input("Enter sub_id"))
p=int(input("Enter plan"))
t=int(input("Enter total pay"))
sc=int(input("Enter screen"))
a=ott_subs(s,p,t)
a.subscribe()
b=premium_subs(s,p,t,sc)
b.max_no_screen(sc)