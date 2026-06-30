# Goal 
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

# Commands Used
>ls -la
>
>./suconnect
>
>echo "4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA" | nc -l -p 2220 & sleep 1 && ./suconnect 2220
>
>echo "4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA" | nc -l -p 45678 & sleep 1 && ./suconnect 2220
>
>echo "4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA" | nc -l -p 45678 & sleep 1 && ./suconnect 45678

# Poblems faced 
./suconnect should connect to the same port as nc -p