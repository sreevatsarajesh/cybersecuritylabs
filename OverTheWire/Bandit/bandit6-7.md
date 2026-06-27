# Goal 
to find the password somewhere in the server where used by -owner bandi7 and group bandid6

# commands used
>find ./ type f -user bandit7 -group bandit6 -size 33c
>
>find / type f -user bandit7 -group bandit6 -size 33c 
>
>find / type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
>cat filename

# Problems faced 
first used find ./ type f -user bandit7 -group bandit6 -size 33c

then removed . and ran into a flood of errors 

hence find / type f -user bandit7 -group bandit6 -size 33c 2>/dev/null

then pathway of the password file will come through, and then cat the path 
