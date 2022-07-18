
class ListTesting:

    def callToLearinList(self,testL , whatToInsert , pos):
        print(testL)

        # To Print Length of a list ...

       # print(len(testL))


        # Access List Items ...

        #print(testL[3])
       # print(testL[-2])
       # print(testL[2:5])
        testL.insert(pos,whatToInsert)
        print(testL)

        for z in testL:
            print(z)

        testL.append(whatToInsert)    
        print(testL)





obj =  ListTesting() 

obj.callToLearinList(["BA" , "Dev" , "QA" , "Prod" ,"Debug" , "Discussion" , "Escalation"] , "phonecall" , 6)


