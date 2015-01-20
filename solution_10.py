# Fuel efficiency of a multi-leg journey

def main():
    filename = input("Enter filename: ") 
    infile = open(filename,"r") 
    temp = infile.readline() 
    oStart = float(temp)
    oLast = oStart
    gLast = 0              
    legCount = 0
    legMPG = []  
    temp = infile.readline()   
         
    while temp !="":    
        oTotal,gTotal = temp.split()
        oTotal = float(oTotal)
        gTotal = float(gTotal)                           
        legMPG.append(round((oTotal-oLast)/(gTotal-gLast),1))
        oLast = oTotal
        gLast = gTotal 
        legCount = legCount+1
        temp = infile.readline()
    print("\nYour fuel efficiency is:")
             
    for i in range(legCount):
        print("Leg#{} has {} MPG.".format(i+1,legMPG[i]))           
    print("\nYour total MPG is",round((oTotal-oStart)/gTotal,2))
    infile.close()

main()
