Number_of_items_bought=int(input("Number of items bought:"))
money_paid=int(input("money paid:"))
average=Number_of_items_bought+money_paid/2
if average >9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif average <5:
    print("გილოცავ გაექეცი მატრიცას")    
elif average>=5 < 9:
    print("YOU ARE MID") 
elif average <10 >0:
    print("there is somthing wrong with you")   

your_salary=int(input("Enter your salary:"))
if your_salary >10000:
    print(" გოა-ში სწავლობდი? ")
elif your_salary>= 1000 <10000:
    print("you mid") 
elif your_salary<1000:
    print("შემოსულიყავი გოაში, მატრიცელო")     


         