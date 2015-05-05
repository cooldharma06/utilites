
'''
Function to  find and replace the string in the files
this is one have to run under the current or nearby folder for better performance.
Input : Input to find
        input to replace

Output: It will search and it will replace the string in the maximum location
'''

import os

list=[]

find = raw_input('Enter the input to find..')
replace = raw_input('Enter the input to replace...')

#command = 'grep -r -I "'+find+'" | awk -F : "{print $1}" >found12.txt'
command = 'grep -r -I "'+find+'" | awk -F : '+'\'{print $1}\''+' > found.txt' 

print 'command is ..',command
os.system(command)
#os.system('grep -r -I "10.0.2.15" | awk -F : '{print $1}' > fount.txt')

# for opening the file list 
found = open('found.txt','r')
filelist = found.readlines()
for n,i in enumerate(filelist):
    file_ = os.path.basename(i).rstrip()

    file_list = 'file2.txt'

## For doing find and replace in the files

    tmp = open(file_,'r+')
    contents = tmp.readlines()

    for n,i in enumerate(contents):
        if find in i:
            #print contents[n]
            contents[n]=contents[n].replace(find,replace)


    #print contents
    tmp.close()

    tmp= open(file_,'w')
    tmp.writelines(contents)
    tmp.close()

found.close()
####  have to remove the found.txt  file
