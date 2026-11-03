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
