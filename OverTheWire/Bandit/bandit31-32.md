# Goal
There is a git repository at ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo via the port 2220.
The password for the user bandit31-git is the same as for the user bandit31.

# Commands Used
```bash
cd repo
echo "May I come in?" > key.txt
cat key.txt
git add -f key.txt
git commit -m "Add key.txt"
git push origin master
```