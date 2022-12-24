import csv

listOfGrades=[]
listOfWeights=[]
sumOfGrades=0
sumOfWeights=0

with open("grades.csv","r") as file:
    csvreader=csv.reader(file, delimiter=';')
    for row in csvreader:
        print(row)
        listOfGrades.append(row[1])
        listOfWeights.append(row[2])

for i in range(0, len(listOfGrades)):
    grade=0
    sumOfWeights+=int(listOfWeights[i])
    if float(listOfGrades[i])==5:
        sumOfGrades+=5*int(listOfWeights[i])
    elif float(listOfGrades[i])==4.5:
        sumOfGrades+=4*int(listOfWeights[i])
    elif float(listOfGrades[i])==4:
        sumOfGrades+=3*int(listOfWeights[i])
    elif float(listOfGrades[i])==3.5:
        sumOfGrades+=2*int(listOfWeights[i])
    elif float(listOfGrades[i])==3:
        sumOfGrades+=1*int(listOfWeights[i])

print(sumOfGrades)
print(sumOfWeights)
print(sumOfGrades/sumOfWeights)
