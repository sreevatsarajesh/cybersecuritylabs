# Goal 
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

# Commands Used 
>nmap -p 31000-32000 localhost
>
>for p in 31046 31518 31691 31790 31960; do
>
>   echo "Testing $p"
>
>   openssl s_client -connect localhost:$p < /dev/null 
>
>2>/dev/null | head
>
>done
>
>  echo "password" | openssl s_client -connect localhost:31790 -quiet

# Problems Faced
Got lost after the RSA Private Key

Tried logging into bandit17 through bandit16, need to logout, save the private key locally and then login into bandit17

