# Goal 
A program is running automatically at regular intervals from cron, the time-based job scheduler. -Look in /etc/cron.d/ for the configuration and see what command is being executed.

# Commands Used
  >ls -la /etc/cron.d/
  >
  >cat /etc/cron.d/cronjob_bandit23
  >
  >cat /usr/bin/cronjob_bandit23.sh
  >
  >myname=bandit22 
  >
  >mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
  >
  >echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
  >
  >cat /tmp/8169b67bd894ddbb4412f91573b38db3
  >
  >myname=bandit23 
  >
  >mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
  >
  >echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
  >
  >cat  /tmp/8ca319486bfbbc3663ea0fbe81326349

# Problems Faced
Should run it in bandit21 not 22