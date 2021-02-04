def alphabetSoup(m, s):
   #We remove the spaces
   m_user = m.replace(" ","")
   # We iterate on the text
   for k in m_user:
       if k in s:
           #each time we find a letter on the soup, we delete it
           s = s.replace(k,"", 1)
       else:
            print("You can not write the message")
            return False
   print("You can write the message")
   return True

#These are the inputs for the code
user_input = input("Enter a message you want to write: ")
soup_input = input("letters found in your soup ")

result = alphabetSoup(user_input,soup_input)

