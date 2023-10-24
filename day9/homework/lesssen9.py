


# 1 ანრი  ზუბაშცილი [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]


# min() ფუნქციის გამოყენების გარეშე
# list=[ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
# for i in list:
#     if i-1 <= 0 or i-2 <= 0:
#         print(i)
# 2  ლუკა სირაძე  input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები
# wort=input("your wort:")
# sum_vocal=0
# for element in wort:
#     for char in element:
#         if char == "a" :
#             sum_vocal+=1
#         elif char == "i":
#             sum_vocal+=1
#         elif char == "o":
#             sum_vocal+=1
#         elif char == "e":
#             sum_vocal+=1 
#         elif char == "u":
#             sum_vocal+=1      
# print("the vocai im wort:",sum_vocal)    





#3  რატი მურღულია მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,და შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა რომელ სახელში 
# name1=input("your name:")
# name2=input("your name:")
# a1=0
# a2=0
# for i in name1:
#     if i == "a":
#         a1+=1
#     else : 
#         a1+=0   
# for y in name2:
#     if y == "a":
#         a2+=1
#     else:
#         a2+=0

# if a1 > a2:
#     print(name1)
# else:
#     print(name2)    
# 
#4  ლუკა კეჭეხმაძე  ნივთმა დაიკლო ფასში 10% ით,საიდანაც გამყიდველმა აიღო 8% მოგება, რამდენ % იან მოგებას აიღებდა ის ფასის დაკლებამდე?ჩაწერეთ ეს ყველა მონაცემი პითონში და დაათვლევინეთ მას. )))

# original_price=int(input("original_price:"))
# Reduced_price=original_price-(original_price*0.1)
# total_win_after_price_reduced=Reduced_price*0.08
# print("reduced price ",Reduced_price)
# print("total win after price reduced ",total_win_after_price_reduced)
# total_win_beffor_price_reduced=original_price*total_win_after_price_reduced/Reduced_price
# print("total win beffor price reduced ",total_win_beffor_price_reduced)
# Answer=8 - (8*0.1)
# print("Answer",Answer)


# 5  გური ჯიშკარიანი შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. დავპრინტოთ დაწყვილებულად 
# name_boy=["dato","giorgi","tsotne","onise"]
# name_girl=["natia","nino","mariami","qristine"]
# print(name_boy[1]  +" "+  name_girl[0])
# print(name_girl[1],name_boy[2])
# print(name_boy[0],name_girl[3])
# print(name_boy[3],name_girl[2])

# 6 გიორგი ჩხეტიანი შექმენით ლისტი სადაც სტრინგის სახით ჩაწერთ სამ ელემენტს (სამივე განსხვავებული ზომის ), გამოთვალეთ ელემენტების სიმბოლოების რაოდენობა და რომელიც საშუალო იქნება ის დაპრინტეთ
# list=["bavshvi","axalgazrda","moxuci"]
# print(len(list[0]))
# print(len(list[1]))
# print(len(list[2]))
# if (len(list[0])-len(list[1]) > 0 and len(list[2]) - len(list[0]) > 0)  or (len(list[0]) - len(list[2]) > 0 and len(list[1]) - len(list[0]) > 0) :
#     print(list[0])
# elif  (len(list[1])-len(list[0]) > 0 and len(list[2]) - len(list[1]) > 0)  or (len(list[1]) - len(list[2]) > 0 and len(list[0]) - len(list[1]) > 0) :
#     print(list[1]) 
# elif  (len(list[2])-len(list[0]) > 0 and len(list[1]) - len(list[2]) > 0)  or (len(list[2]) - len(list[1]) > 0 and len(list[0]) - len(list[2]) > 0) :
#     print(list[2])     
# else:
#     print("something wrong")

# 7  ცოტნე სართანია მოკლედ ჩემი მოფიქრებული დავალაება:  შექმენით 10 მათემატიკური შეკითხვა მომხმარებლისთვის მაგალითად( 67-43=?,  86+23=?  5*18=?  და ასეშემდეგ  .......  რომ პასუხები იყოს რიცხვები)  შემდეგ გააკეთეთ ისე რომ ყოველი მცდარი ან  სწორი პასუხის შემდეგ პასუხის ქვემოთ ეწერებოდეს სწორია ან არასწორია ხოლო ტესტის დასრულების შემდეგ თუ 10 ივე  კითხვის პასუხი იქნება ჭეშმარიტი დაიპრინტოს: "შენ აშკარად GOA ში სწავლობდი ჩემო ძმაო".   ხოლო თუ ამ 10 პასუხიდან 1 მაინც იქნება მცდარი დაიპრინტოს ..."კიდევს სცადეთ ან შემოგვიერთდი GOA ში, GOA ელს ეს არეკადრება"
# totale_True=0
# question_1=2*5 
# answer_1=int(input("answer_1:(2*5) "))
# if question_1 == answer_1:
#     print("True")
#     totale_True+=1
# elif question_1 != answer_1:
#     print("False")    
# question_2=3*5
# answer_2=int(input("answer_2:(3*5)"))
# if question_2 == answer_2:
#     print("True")
#     totale_True+=1
# elif question_2 != answer_2:
#     print("False")    
# question_3=25+6
# answer_3=int(input("answer_3:(25+6)"))
# if question_3 == answer_3:
#     print("True")
#     totale_True+=1
# elif question_3 != answer_3:
#     print("False")   
# question_4=45-6
# answer_4=int(input("answer_4:(45-6)"))
# if question_4 == answer_4:
#     print("True")
#     totale_True+=1
# elif question_4 != answer_4:
#     print("False")   
# question_5=30/3
# answer_5=int(input("answer_5:(30/3)"))
# if question_5 == answer_5:
#     print("True")
#     totale_True+=1
# elif question_5 != answer_5:
#     print("False")  
# if totale_True == 5 :  
#     print("შენ აშკარად GOA ში სწავლობდი ჩემო ძმაო") 
# else: 
#     print("კიდევს სცადეთ ან შემოგვიერთდი GOA ში, GOA ელს ეს არეკადრება" )    
 
# 8  ნინო სოლომინია: შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.
# list=["გიორგი აბუდაძე","სალომე მილაძე","ტატო ჩოგოვაძე","გიგი გაგოტიძე","ილია ადამია"]
# count_a_b=0
# for i in list:
#     for char in i:
#         if char == "ი":
#             count_a_b+=1
#         elif char == "ა":
#             count_a_b+=1
#         else:
#             count_a_b+=0    
# print(count_a_b)


# 9 სალომე მილაძე :     შექმენით თქვენი ფილმების სია, რომელშიც ჩაწერთ უკვე ნანახ ფილმებს.
# მომხმარებელს(თქვენს პირობით მეგობარს) შემოატანინეთ მის მიერ რეკომენდირებული ფილმი. 
# თუ ფილმი დაემთხვევა თქვენს სიაში არსებულ ფილმს დაწერეთ “ძალიან მომეწონა ეს ფილმი ან არ მომეწონა ეს ფილმი” თუ არ გაქვს ნანახი “ჩავინიშნავ და აუცილებლად ვნახავ”
# list=["cisperi mtebi","sherekilebi","bechdebis brdsanebeli","interstelari"]
# name_of_Filme=input("შენი საყვარელი ფილმი:")
# for i in list:
#     if i in name_of_Filme:
#         if i in [list[0], list[1], list[2]]:
#             print("ძალიან მომეწონა ეს ფილმი")
#         else:
#             print("არ მომეწონა ეს ფილმი")
#         break
# else:
#     print("ჩავინიშნავ და აუცილებლად ვნახავ")



# 10 ნინი გოგლიჩაძე : შემოიტანეთ სამი რიცხვი და დაპრინტეთ გამოვა თუ არა ამ რიცხვების საშუალებით სამკუთხედი, თუ გამოვა გამოთვალეთ პერიმეტრი და დაპრინტეთ "ამ სამკუტხედის პერიმეტრია: XX" თუ არ გამოდის მაშინ დაპრინტეთ „მსგავსი სამკუთხედი არ არსებობს“
# namber1=int(input("namber1:"))
# namber2=int(input("namber2:"))
# namber3=int(input("namber3:"))
# if namber1 > 0 and namber2 >0 and namber3 >0 :
#     print("ამ სამკუტხედის პერიმეტრია:",namber1+namber2+namber3)
# else:
#     print("მსგავსი სამკუთხედი არ არსებობს")

# 11 (temo labadze) შექმენით სია სადაც შემოიტანთ რამდენმე რიცხვს 
#  მაგ:"24,50,25,90" და რომელიმე რიცხვი ჩაანაცვლეთ "69"_ით და გამოითვალეთ ამ რიცხვევის ჯამი
# list=[24,50,25,90]
# list.insert(2,69)
# print(list)
# sum=0
# for i in list:
#     sum+=i
# print(sum)


#12შემოიტანეთ აპლიკანტის: სიმაღლე (>= 1,6 და <=2,3) წონა (>=55 და <= 130) ასაკი (>=18 და <=27), თუ აპლიკანტის მონაცემები აკმაყოფილებს შესაბამის მთხოვნებს,მაშინ დაობეჭდოს " გილოცავთ!, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში" და თუ არ აკმაყოფილებს მაიშინ დაობეჭდოს "სამწუხაროდ თქვენი მონაცემები არ შესაბამება ჩვენს მოთხოვნებს"
# hight=int(input("hight:"))
# weight=int(input("weight:"))
# age=int(input("age:"))
# if  (hight >= 1.6 and hight <= 2.3) and ( weight >= 55  and weight <= 130) and ( age >= 18 and age <= 27):
#     print("გილოცავთ!, თქვენ ჩაირიცხეთ სავალდებულო სამხედრო სამსახურში")
# else:
#     print("სამწუხაროდ თქვენი მონაცემები არ შესაბამება ჩვენს მოთხოვნებს")



# 13 User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუნტებში...(თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, დაუპრინტეთ რამდენი ფუტია ის. 



   

    
# list=["x","a","y","b"]
# name_of_Filme=input("შენი საყვარელი ფილმი:")      

# for i in list:
#     if i == name_of_Filme[0] or name_of_Filme[1] or name_of_Filme[2]:
#         print("ძალიან მომეწონა ეს ფილმი")
#         break
#     elif i == name_of_Filme[3]:
#         print("არ მომეწონა ეს ფილმი")
#         break
#     else :
#         print("ჩავინიშნავ და აუცილებლად ვნახავ")
#         break


# for i in list:
#     if i in [name_of_Filme[0], name_of_Filme[1], name_of_Filme[2]]:
#         print("ძალიან მომეწონა ეს ფილმი")
#     elif i in [name_of_Filme[3]]:
#         print("არ მომეწონა ეს ფილმი")
#     else :
#         print("ჩავინიშნავ და აუცილებლად ვნახავ")

