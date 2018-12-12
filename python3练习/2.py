import os

filename1 = os.path.basename('/Users/momo/Desktop/lastvideo2')
filename2 = os.path.basename('/Users/momo/Desktop/last')

if filename1 != filename2:
   print(filename1,filename2)