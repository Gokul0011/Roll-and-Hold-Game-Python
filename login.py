import logging
def register():


    username = input('Enter the user name:').lower()
    password = str(input('Enter the password:'))
    confirm_password = str(input('Confirm password:'))
    if password == confirm_password:
        
            # password = password
        print('Congratulations! you have successfully registered. ')
    else:
        print('password and confirm password is not matching')
        register()
        
        
register()


    