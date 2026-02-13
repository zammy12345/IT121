while True:
    pas = input("Enter Pasword: ")
    
    let = any(char.isalpha() for char in pas)
    num = any(char.isdigit() for char in pas)
    
    if let and num:
        print("Accept")
        break;
    else:
        print("Denied")