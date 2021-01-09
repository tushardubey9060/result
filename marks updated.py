def main():
            x=input("student name:")
            a=float(input("marks in english:"))
            b=float(input("marks in hindi:"))
            c=float(input("marks in maths:"))
            d=float(input("marks in science:"))
            e=float(input("marks in sst:"))
            total= a+b+c+d+e
            if (a>b)and (a>c)and (a>d)and (a>e):
                                          print ("highest in english")
            elif (b>a)and b>c and b>d and b>e:
                                          print ("highest score in hindi")
            elif (c>a)and (c>b)and (c>d) and (c>e):
                                          print ("highest in maths")
            elif (d>a)and (d>b)and (d>c)and (d>e):
                                          print ("highest in science ")
            elif (e>a)and (e>b)and (e>c)and (e>d):
                                          print ("highest in sst")
            else :
                print ("invalid no.")

            percentage = (total /500) *100
            avg1=(total/5)

            if avg1>90:
                       print ("your grade is a")
            elif avg1>80:
                       print ("your grade is b")
            elif avg1 > 70:
                       print ("your grade is c")
            elif avg1 > 60:
                       print ("your grade is d")
            else:
                 print ("fail")

            print("total:",total )
            print("percentage:", percentage)
            print("average:", avg1 )

            restart=input("if u want to start again press y ")
            if restart=="y":
                main()
            else:
                exit()
                    
                            

                            
