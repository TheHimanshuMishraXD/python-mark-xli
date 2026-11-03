# so here we are learning about the shutil module in Python. The shutil module provides a number of high-level operations on files and collections of files. 
# It is especially useful for copying and archiving files and directories.
import shutil
shutil.copy("test.py" , "tupple.py")

# Isme:
# Code	Meaning
# shutil.copy()	File copy karne ka function
# "test.py"	Source file, jisko copy karna hai
# "tupple.py"	Destination file, jisme copy banegi


# agar hame 1 pure folder ko copy karna hai to hum shutil.copytree() ka use krege q ki shutil.copy file ke liye use hota h

shutil.copytree("test" , "test2")



# .move use file ko move karne ke liye hota hai. Agar hame file ko ek jagah se dusri jagah move karna hai to hum shutil.move() ka use krege.
shutil.move("tutorial/file.file" , "file.file")


#  isme scene ye hai ki ki agar tutorial folder ke andar file.file hai to usko move karne ke baad tutorial folder khali ho jayega. Agar hame tutorial folder ko bhi move karna hai to hum shutil.move() ka use krege.




# so lets agar hame kisi folder ko delete karna hai to hum shutil.rmtree() ka use krege. Ye function folder ke andar ke sare files aur folders ko delete kar deta hai.
shutil.rmtree("test2") #here the test 2 is folder



and agar hame kisi file ko delete karna hai to hum os.remove() ka use krege. Ye function file ko delete kar deta hai.
