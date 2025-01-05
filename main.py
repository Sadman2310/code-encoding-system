s=input("Enter something to decode : ")
n=len(s)
if(n<3):
     new_string=s[1::-1]
     print("The decoded word is: ",new_string)
else:
   new_string=s[3:]
   ans_str=new_string[:len(new_string)-3]
   first=ans_str[:len(ans_str)-1]
   k=ans_str[len(ans_str)-1]
   ans=k+first
   print("The decoded word is: ",ans)