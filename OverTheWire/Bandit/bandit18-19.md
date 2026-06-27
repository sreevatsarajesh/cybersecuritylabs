# Goal 
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

# Commands Used 
> ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"

# Problems Faced
It logs you out immediately 
You can send the commands to run inside the ssh without logging in using " ".