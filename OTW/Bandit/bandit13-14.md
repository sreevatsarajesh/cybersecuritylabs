# Goal 
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. 

# Commands Used
> scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private .
>
> chmod 600 sshkey.private
>
> ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

# problems faced 
in scp -P, the P should be capital, faced problems after using "p" as it tried connecting to port 22

tried using chmod without logging out and using scp which gave me access errors