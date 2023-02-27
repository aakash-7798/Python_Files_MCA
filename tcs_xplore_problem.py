# / Testing Sample input to take data

total_bonus = 0
threshold = 0
rate_per_hour = 0


class Employee:
    def __init__(self,employee_name,designation,salary,overtime_contribution,overtime_status):
        self.ename = employee_name
        self.dsg = designation
        self.slry = salary
        self.otctb = overtime_contribution
        # print(threshold)
        self.otst = self.eligibility()
        if(self.otst is True):
            global total_bonus
            total_bonus += rate_per_hour*self.sum_hours()



    def sum_hours(self):
        summ = 0
        for i in self.otctb.values():
            summ+=i
        return summ

    def eligibility(self):
        return self.sum_hours()>threshold


emp_list = []
with open("tcs_xplore_sample_input2.txt","r") as f1:
    tc = int(f1.readline().strip())
    for i in range(tc):
        name = f1.readline().strip()
        dsg = f1.readline().strip()
        slry = int(f1.readline().strip())
        tt = int(f1.readline().strip())
        lst = []
        for j in range(tt*2):
            lst.append(f1.readline().strip())
        dt = {}
        for k in range(0,len(lst),2):
            dt[lst[k]] = int(lst[k+1])
        emp_list.append([name,dsg,slry,dt,False])

    threshold = int(f1.readline().strip())
    rate_per_hour = int(f1.readline().strip())

# print(threshold)
# print(rate_per_hour)

for i in emp_list:
    emp = Employee(*i)
    print(emp.ename,emp.otst)
print(total_bonus)


# print(emp_list)
# print(threshold)
# print(rate_per_hour)



