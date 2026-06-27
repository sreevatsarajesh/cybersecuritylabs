# Goal 
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

# Commands Used
> ls -l
> 
> ./bandit20-do
>
> ./bandit20-do whoami
>
> ./bandit20-do cat /etc/bandit_pass/bandit20

# Problems Faced 
Used ./bandit20-do whoami cat /etc/bandit_pass/bandit20
and ran into errors , fixed when whoami was removed
