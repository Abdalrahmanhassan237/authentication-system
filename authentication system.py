def psw():
    password =input("enter your password  :")
    password2 = input("confirm password :")
    if password != password2 :
        print("password not match ,try again")
        psw()


  
       
choice = input("To login enter [1]. If you want to register enter [2] : ")
if choice == "2":
     def register():
        import re
        d= open("data.txt","r")
        first_name =input("enter your first name :")
        last_name =input("enter your last name :")
        password =input("enter your password  :")
        password2 = input("confirm password :")
        if password != password2 :
            print("password not match ,try again")
            psw()
        elif len(password) <= 6:
            print("password too short,try again")
            psw()
        def check_email():
            e_mail = input("enter your email :")
            global y
            y = re.search( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',e_mail)
        if y:
            print("e-mail is ok")
        else :
            print("e-mail is not valid")
            check_email()
        def mobile_number_check():
            mobile =input("enter your phone number  :")
            x = re.search("^01[0125][0-9]{8}$", mobile)
        if x:
           print("number is ok")
        else :
           print("number is not valid")
           mobile_number_check()
        d= open("data.txt","a")
        d.write("name = "+first_name+" "+last_name+"\n"+"password ="+password+"\n"+"e_mail = "+e_mail+"\n"+"phone number= " +mobile+"\n")
        d.close
        print("success")
           
     register()
elif choice == "1":
     
     def login():
          d = open("data.txt","r")
          name =input("enter your name :")
          password =input("enter your password :")
          check = d.read()
          if name in check :
              print("user name is  found ")
              if password  in check :
                  print("password is ok \n success login")
          else :
             print("faild login ,try again")
             login()
     login()     
else : 
    print("please enter [1] or [2]")
