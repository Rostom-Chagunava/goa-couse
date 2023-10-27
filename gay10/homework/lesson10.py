# 1 davaleba  დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
# რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 1 ქულა და გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),
# import random
# list_member_of_squad = ["gigi gabitaze","gio chirgaze","merab cicxvaia","rostom chagunava"]
# score_of_gigi = 0
# score_of_gio = 0
# score_of_merab = 0
# score_of_rostom = 0
# for i in range (len(list_member_of_squad)):
#     lacky_member = random.choice(list_member_of_squad)
#     print(lacky_member)
#     answer=input("did the students answer correctly: ")
#     list_member_of_squad.remove(lacky_member)
#     if answer == "yes":
#         if lacky_member == list_member_of_squad [0]:
#             score_of_gigi+=10
#             print(score_of_gigi)
#         elif lacky_member == list_member_of_squad [1]:
#             score_of_gio+=10
#             print(score_of_gio)    
#         elif lacky_member == list_member_of_squad [2]:
#             score_of_merab+=10
#             print(score_of_merab) 
#         elif lacky_member == list_member_of_squad [3]:
#             score_of_rostom+=10
#             print(score_of_rostom)
#     elif answer == "no" :
#         if  lacky_member == list_member_of_squad [0]:
#             score_of_gigi-=5
#             print(score_of_gigi)
#         elif lacky_member == list_member_of_squad [1]:
#             score_of_gio-=5
#             print(score_of_gio)    
#         elif lacky_member == list_member_of_squad [2]:
#             score_of_merab-=5
#             print(score_of_merab) 
#         elif lacky_member == list_member_of_squad [3]:
#             score_of_rostom-=5
#             print(score_of_rostom)          
#     else :
#         print ("something wrong") 








# import random
# list_member_of_squad = ["gigi gabitaze","gio chirgaze","merab cicxvaia","rostom chagunava"]
# score_of_gigi = 0
# score_of_gio = 0
# score_of_merab = 0
# score_of_rostom = 0




# for i in range(len(list_member_of_squad)):
#     lucky_member = random.choice(list_member_of_squad)
#     print(lucky_member)
#     answer = input("Did the student answer correctly (yes/no): ")
#     list_member_of_squad.remove(lucky_member)

#     if answer == "yes":
#         if lucky_member == "gigi gabitaze":
#             score_of_gigi += 10
#             print("Gigi's score:", score_of_gigi)
#         elif lucky_member == "gio chirgaze":
#             score_of_gio += 10
#             print("Gio's score:", score_of_gio)
#         elif lucky_member == "merab cicxvaia":
#             score_of_merab += 10
#             print("Merab's score:", score_of_merab)
#         elif lucky_member == "rostom chagunava":
#             score_of_rostom += 10
#             print("Rostom's score:", score_of_rostom)
#     elif answer == "no":
#         if lucky_member == "gigi gabitaze":
#             score_of_gigi -= 5
#             print("Gigi's score:", score_of_gigi)
#         elif lucky_member == "gio chirgaze":
#             score_of_gio -= 5
#             print("Gio's score:", score_of_gio)
#         elif lucky_member == "merab cicxvaia":
#             score_of_merab -= 5
#             print("Merab's score:", score_of_merab)
#         elif lucky_member == "rostom chagunava":
#             score_of_rostom -= 5
#             print("Rostom's score:", score_of_rostom)
#     else:
#         print("Something wrong")





#  2 davaleba 
# import random
# num=[2,1,5,3,4,6,3,4,7,3,4,7]
# alpb=["ა","გ","ქ","წ","ე","კ","ჯ","ა","ს","კ,","ჯ","ქ","წ","ე"]
# symbol=["!","#","#","%","(",")","^"]
# print(random.choice(num),random.choice(num),random.choice(alpb),random.choice(alpb),random.choice(symbol),random.choice(symbol),random.choice(symbol),random.choice(symbol))

# 3 davalena turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი 

# import random
# from turtle import *
# speed(10)
# width(5)
# for i in range(5000):
#     forward(random.randint(1,100))
#     color("purple")
#     left(random.randint(1,100))
#     color("red")
#     forward(random.randint(1,100))
#     right(random.randint(1,100))
#     color("pink")
#     forward(random.randint(1,100))
#     left(random.randint(1,100))
#     color("green")


    