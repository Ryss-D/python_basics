##approach #1 with simple decorator syntax
user = {"usernmae":"jose", "access_level":"guest"}

def get_admin_password():
    return "1234"

#decorator allowus to modify functuions behjavior

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func
    return secure_function

#this is the simple decorator
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

##approach #2 with @("at") syntax

import functools

user = {"usernmae":"jose", "access_level":"guest"}

def make_secure(func):
    ##we have to add this decorator, because without it
    ## the function referenced will be secure_function instead of
    ## get_admin__password (testeable if we print get_admin_password.__name__)
    ##with this decorator we express thaat this is just a wareppes o decorator
    @functools.wraps(func)
    def secure_function():
        ##if functions must receive argument
        ##btw ** unpack dictionaryes 
        ##we just unse secure_fucntion(*args, **kwargs) to receive unlimited arguments and keyword arguments
        if user["access_level"] == "admin":
            return func
    return secure_function

## if we put the at syntax an point to a decorator
##before a fucntion definition it will avoid the function 
##to be created it self and will pass it to the decorator
@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())

##id function give us the addess in memory for a objectr