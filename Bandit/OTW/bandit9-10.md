# Goal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

# Commands Used
>cat data.txt | grep '='
>
>grep -a '==' data.txt
>
>strings data.txt | grep "="

# Problems faced 
after running cat, gave corrupted entries as file is binary
after running grep -a, corrupted entries again 
strings worked 