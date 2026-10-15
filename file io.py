# agar hame kisi file ko open krke usko read krna hoto ham phle ik file 
# banayege jisme data text ke taur par hoga and then usko f ya kisi bhi variable se assign krege after this isme ham f = open('my file.txt , 'r') f.read()
# f = open('my file.txt' , 'r')
# # f = open('my file.txt' , 'r')   #agar ham yaha bina r mode ke kare tb bhi chlega  q ki r mod fefault hota hai
# text = f.read()

# print(text)
# f.close()

#for write inside the file
# f = open('my file2.txt' , 'w')
# text = f.write('Helllo ! himanshu')

# f.close()







# # #agar hame without  close statement ka use kre file likhni hai  to ham with statement ka use krege
# # with open('my file.txt' ,  'a'):
# #     f.write("hey im inside with") 






# #agar hamne binary file read krni ho to ham rb use kreege comma ke baad



# # agar hame kisi file me naye text rewrite krne ho to ham use krege

# # f = open("my file2.txt" , 'w')
# # text = f.write("mera name haidon or mai hu nayab rakhwala madhyapradesh ka")
# # f.close()

# # agar mujhe append krna hai file me to mai use kruga 'a'

# # f = open('my file2.txt' , 'a')
# # text = f.write("mera name hai baagad billaaa aur me naachta hu khullam khulla")
# # f.close()

# # with open('my file2.txt' , 'a') as f:
# #     f.write("hey my name is himanshu")




# # f = open('intro.txt' , 'w')
# # test = f.write("my name is himanshu\n")
# # f.close()
# a  = input("enter your string:    ")
# f = open('intro.txt' ,'a')
# test = f.write(a)





# # f = open('intro.txt' , 'r')
# # test = f.read()
# # print(test)




# # Problem Statement 2: Daily Learning Log

# # Python program likho jo learning.txt file me tumhari aaj ki learning save kare.

# # User se aaj seekha hua topic input lo aur file me likho.
# # User se ek aur topic input lo aur use file me nayi line par add karo. Pehla topic delete nahi hona chahiye.
# # File ka poora content read karke print karo.

# # Example input:

# # First topic: File handling
# # Second topic: Append mode

# # Expected output:

# # File handling
# # Append mode






a  = input("enter your string:    ")

f = open('intro.txt' ,'a')

test = f.write(a)

#kaise kaam aayega ye Bhai, real project me file I/O ka kaam data ko program band hone ke baad bhi save rakhna hai. 
# Abhi tumhara f.write(a) exactly wahi kar raha hai: user ka input intro.txt me save ho jaata hai. Program dobara chalaoge, to purana text file me milega.