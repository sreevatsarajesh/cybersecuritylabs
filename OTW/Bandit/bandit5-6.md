# Goal
find password in the inhere directory where - it is in human readable format - 1033 bytes in size - not executable

# Commands
>ls
>
>find ./inhere -type f -size 1033c ! -executable -readable -exec file {} ; | grep ASCII;
>
>cat

# problems 
the find command was way too complicated and manually checking each of the directory is too tedius but once understood find command is easy