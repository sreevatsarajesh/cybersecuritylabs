# Goal 
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time

# Commands Used
>for i in $(seq -w 0000 9999); do
>
>   echo "<hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv> $i"
>
>done | nc localhost 30002
>
>for i in $(seq -w 0000 9999); do
>   echo "<bandit24_password> $i"
>done | nc localhost 30002

# Problems faced
I added <> as a part of password 