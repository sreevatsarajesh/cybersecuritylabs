# Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

# Commands Used
>crontab
>
>crontab -l
>
>ls -la /etc/cron.d/
>
> cat /etc/cron.d/cronjob_bandit22
>
>cat /usr/bin/cronjob_bandit22.sh
>
>cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

# Problems Faced
running crontabl -l or trying to edit the crontab is not allowed, but cron.d can be seen using ls -la