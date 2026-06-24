# Goal 
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

# Commands used
>echo "password" | openssl s_client -connect localhost:30001 -quiet 

# Problems faced
like last level nc wont work directly so need to connect using openssl
