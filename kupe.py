def find_number_of_kupe(user_data):
    if user_data <= 0 or user_data >= 24:
        return 'Input correct № of place!'
    return f"Your's kupe № {((int(user_data)-1)//4)+1 if user_data >= 5 else 1}, please, take your seat!"
user_data = int(input('Input your ticket number: '))
print(find_number_of_kupe(user_data))
