#!/usr/bin/python3.6
import os
count = 0

file_name = os.getcwd()
with open(file_name+'/'+'Job_list.txt','r') as f:
        for line in f:
            count +=1
            
def main():
    Strings="Search Job"
    Job_Des="Details"
    Apply="Applied"
    List=["1.Search Job", "2.Details","3.Applied"]
    for i in List:
        print(i);
    Options=input("Enter the Job Opening 'Yes' or 'No': ")
    if Options=='Yes':
        print('List of job openings');
        file_name = os.getcwd();
        file = open(file_name + '/' + 'Job_list.txt', "r");  
        for line in file:
            coun = 0
            i=0
            fields=line.split(",")
            coun=len(fields)
            for i in range(coun-1):
                print(fields[i]);
        ID=input("Enter you matching Opening Jobs ID: ")
        List = []
        for directories in os.listdir(os.getcwd()):
            List.append(directories);
#        print(List)
        res = [i for i in List if ID in i]
        ID_Not=len(res)
        if ID_Not>0:
            file = open(file_name + '/' +res[0], "r");                
            for line in file:
                print(line);
            Apply=input("Intersted Enter 'Apply' Key: ");
            if str(Apply)=='Apply':
               print("Thanks For Submitting!!!!")
            else:
               print("Not Applied")
        else:
             print("Your Entered Invalid Job ID");
    else:
        print("Your Exit")

if __name__ == "__main__":
    main();
 
