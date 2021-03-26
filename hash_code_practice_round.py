import numpy

def fileinput(filen):
    with open(f"./inputs/{filen}") as file:
        data = file.read().splitlines()
    file.close()

    fline = data[0].strip()
    fline = fline.split(' ')
    pi_avail = int(fline[0])
    ppt = fline[1:] #No. of Person per Team

    print("\nNo. of Pizza Available : ",pi_avail)
    for i in range(3): 
        ppt[i] = int(ppt[i])
        print("No. of ",i+2,"- Person Teams : ",ppt[i])

    pi_type = {} #Pizza Catalogue
    nip = {} #No. of Ingredient per Pizza
    i=0
    for line in data[1:]:
        pi_type[str(i)] = line
        nip[str(i)] = int(line.split(' ')[0])
        i+=1
    
    #print("\nPizza types : ")
    #print(pi_type)
    level = {}
    ingredient = {} #Count of each Ingredient
    for pt in pi_type.values():
        for i in pt.split(' ')[1:]:
            ingredient[i] = int(ingredient.get(i,0))+1 
    
    for ind,pt in pi_type.items():
        l=1
        for i in pt.split(' ')[1:]:
            l = l*(ingredient.get(i)/pi_avail)
        level[ind] = l
    
    #print(level)
    s = sorted(level.items(),key=lambda x:x[1])
    i=0
    new={}
    for ind,pt in pi_type.items():
        new[s[i][0]] = pi_type.get(s[i][0])
        i+=1
    #print(new)
    pi_type = new
    #print(pi_type)
    #print("\nNo. of ingredient per pizza : ",nip)
    #print("\nCount of each ingredient : ",ingredient)
    
    return(pi_avail,ppt,pi_type,ingredient,nip)

def distribution(piav,team,type,ing,noip,filen):
    piavc = piav #variable storing total no. of pizza available
    pi_twolist = {} #list of pizzas for 2-team
    pi_threelist = {} #list of pizzas for 3-team
    pi_fourlist = {} #list of pizzas for 4-team
    j=0 #increment variable used as key to get pizzas
    total_dev = 0 #no. of team getting pizzas
    list_keys= list(type.keys())
    f = open(f"./outputs/submission_{filen}","w")
    f.write(str(total_dev)+'\n')

    def pi4():
        nonlocal j,f,piavc,piav,pi_twolist,pi_threelist,pi_fourlist,total_dev
        if piav >= 4:
            i = 0
            while (i<team[2] and piav>=4):
                pi_fourlist[str(i)] = [type.get(str(list_keys[j])),type.get(str(list_keys[j+1])),type.get(str(list_keys[j+2])),type.get(str(list_keys[j+3]))]
                f.write(str(4)+" "+str(list_keys[j])+" "+str(list_keys[j+1])+" "+str(list_keys[j+2])+" "+str(list_keys[j+3])+"\n")    
                piav -= 4
                i += 1
                j+=4
            total_dev+=i
            
    def pi3():
        nonlocal j,f,piavc,piav,pi_twolist,pi_threelist,pi_fourlist,total_dev
        if piav>=3:
            i=0
            while (i<team[1] and piav>=3):
                pi_threelist[str(i)] = [type.get(str(list_keys[j])),type.get(str(list_keys[j+1])),type.get(str(list_keys[j+2]))]
                f.write(str(3)+" "+str(list_keys[j])+" "+str(list_keys[j+1])+" "+str(list_keys[j+2])+"\n")    
                piav-=3
                i+=1
                j+=3
            total_dev+=i

    def pi2():
        nonlocal j,f,piavc,piav,pi_twolist,pi_threelist,pi_fourlist,total_dev
        if piav>=2:
            i=0
            while (i<team[0] and piav>=2):
                pi_twolist[str(j)] = [type.get(str(list_keys[j])),type.get(str(list_keys[j+1]))]
                f.write(str(2)+" "+str(list_keys[j])+" "+str(list_keys[j+1])+"\n")    
                piav-=2
                i+=1
                j+=2
            total_dev+=i

    pi2()
    pi3()
    pi4()

    f.close()

    fi = open(f"./outputs/submission_{filen}","r")
    lines = fi.readlines()
    lines[0] = str(total_dev)+"\n"
    fi.close()
    fi = open(f"./outputs/submission_{filen}","w")
    fi.write("".join(str(l) for l in lines))
    fi.close()
    '''
    if (len(pi_twolist)!=0):
        print("\nA 2 Person Team will receive ",len(pi_twolist)," pizzas")
        #print(pi_twolist)
        tig_2 = 0 #variable for storing total no. of ingredient for 2-team
        uig2=[] #variable for storing unique no. of ingredient for 2-team
        for key,val in pi_twolist.items(): 
            tig_2 += noip.get(key)
            val=[x for v in val for x in v.split(" ")[1:]]
            uig2.append(val)
            
        uig2=list(numpy.concatenate(uig2).flat)
        uig2=len(numpy.unique(uig2))
        print("Total Ingredient of 2-Person Team: ",tig_2)
        print("Unique Ingredient of 2-Person Team:",uig2)

   
    if len(pi_threelist)!=0:
        print("\nA 3 Person Team will receive ",len(pi_threelist)," pizzas")
        #print(pi_threelist)
        tig_3 = 0 #variable for storing total no. of ingredient for 3-team
        uig3=[] #variable for storing unique no. of ingredient for 3-team
        for key,val in pi_threelist.items():
            tig_3 += noip.get(key)
            val=[x for v in val for x in v.split(" ")[1:]]
            uig3.append(val)

        uig3=list(numpy.concatenate(uig3).flat)
        uig3=len(numpy.unique(uig3))
        print("Total Ingredient of 3-Person Team: ",tig_3)
        print("Unique Ingredient of 3-Person Team:",uig3)
       
    if len(pi_fourlist)!=0:
        print("\nA 4 Person Team will receive ",len(pi_fourlist)," pizzas")
        #print(pi_fourlist)
        tig_4 = 0 #variable for storing total no. of ingredient for 4-team
        uig4=[] #variable for storing unique no. of ingredient for 4-team
        for key,val in pi_fourlist.items():
            tig_4 += noip.get(key)
            val=[x for v in val for x in v.split(" ")[1:]]
            uig4.append(val)
            
        uig4=list(numpy.concatenate(uig4).flat)
        uig4=len(numpy.unique(uig4))
        print("Total Ingredient of 4-Person Team: ",tig_4)
        print("Unique Ingredient of 4-Person Team:",uig4)
    '''

    return
    
if __name__ == '__main__':
    filenames = ["a_example","b_little_bit_of_everything.in","c_many_ingredients.in","d_many_pizzas.in","e_many_teams.in"]
    #filenames = ["a_example"] 
    for filen in filenames:
        inputlist = fileinput(filen)
        distribution(inputlist[0],inputlist[1],inputlist[2],inputlist[3],inputlist[4],filen)