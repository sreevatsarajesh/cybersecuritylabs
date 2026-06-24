# Goal
find the password in a hexdump file which is repeatedly compressed

# Commands Used 
> xxd -r
>
> mv
> 
> gunzip
>
> bunzip
>
> tar -xf

# Problems faced 
Toughest one so far, had to repeatly check the file type and repeatedly decompress based on .gz or .bz2 or .tar

The main problem I faced was after each tar it created a new bin file and i had to ignore the previous file and work on the bin every single time, reached till databin8