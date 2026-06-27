# Goal 
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

# Commands used 
>  cat /etc/bandit_pass/bandit14
> 
> echo "password" | nc localhost 30000

# Problems faced
getting the password of this level as we logged into this using a private ssh key