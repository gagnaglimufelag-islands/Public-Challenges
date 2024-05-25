# Zero Day Zorro
**Category:** for

**Author:** hjalti

**Files:**
- access.log
- exploit.py

We have recently experienced a security breach on our website, and we urgently need your help. Our site, which utilizes a SQLite database, was compromised by a hacker.

Based on the findings of the experts we consulted, the hacker used a tool called SQLMap to identify a vulnerability, although it appears that this tool was not used for the actual exploitation.

Through analysis of our logs and user agent data, the experts attributed the attack to a notorious hacker known as @Zer0DayZorro. They discovered a forum post where he boasted about the attack and shared the exploit he used to gain access to our data.

Using this exploit, the hacker stole the admin password stored in our database and subsequently shut down all our systems. The logs show that the exploit was the last activity on the server. The attack occurred in the middle of the night, a time when we typically do not expect genuine traffic, indicating that the only requests to the server were from the attacker.

We are in a difficult position: to inform our loyal customers about the breach, we need to access our Facebook account. Unfortunately, the Facebook account shares the same password as the compromised admin account, and no one can remember it.

To assist you in your investigation, we are providing the exploit discovered on the forum and the logs retrieved from the server. Unfortunately, these logs are mostly just HTTP access logs and do not provide much detailed information. The developers accidentally left the SQL query profiler running, which could have given some insight into the exploit. However, due to GDPR regulations, the profiler was not logging the actual queries themselves. We apologize for the extra noise in the logs.

Can you help us recover the password?
