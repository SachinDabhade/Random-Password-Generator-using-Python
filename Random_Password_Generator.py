# ************************* Strong Password ***************************
""" While making the password we have to make strong password """

# Importing Libraries
import string
import random
import pickle

if __name__ == '__main__':

    # Input the purpose of password
    purpose = input("Reason Behind your password: ")
    # Final Set useful for shuffle the password
    final_set = []
    set_1 = string.ascii_letters
    set_2 = string.digits
    set_3 = string.punctuation
    final_set.extend(set_1)
    final_set.extend(set_2)
    final_set.extend(set_3)
    random.shuffle(final_set)
    try:
        P_len = int(input("Enter your password length:"))
    except Exception as E:
        print("Please enter integers only...!")
        exit()
    Password = final_set[0:P_len]
    Pass_dict = {}
    Pass_dict[purpose] = ''.join(Password)

    # Hiding the file of password
    with open("Pass.pkl", "wb") as f:
        pickle.dump(Pass_dict, f)
    
    # Opening the hidden file
    with open("Pass.pkl", "rb") as f:
        a = pickle.load(f)
        print(a)
    
