#in bash we only can create conditionals based on exit status $? thats a way to check the last process exit status

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

#The grep command is used to search text. It searches the given file for lines containing a match to the given strings or words. It is one of the most useful commands on Linux and Unix-like system. Let us see how to use grep on a Linux or Unix like system.

#the test command evaluate contions and then return a exit status code

if test -n "$PATH"; then echo "Your path is not empty";fi
#a alias to test is te []
if [ -n "$PATH" ]; then echo "Your path is not empty"; fi