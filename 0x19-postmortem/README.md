# 0x19-postmortem

![I WILL FIND YOU AND I WILL FIX YOU](https://miro.medium.com/max/1400/0*kHoWD7gJ0PC9GmBK.jpg)

## Issue Summary

**Duration:** The outage occurred from 10:00 AM to 2:00 PM on 2023-05-15 (UTC).
**Impact:** The web application experienced complete unavailability, affecting 100% of the users.
**Root Cause:** The outage was caused by a misconfigured load balancer that led to a traffic overload on the database server.

## Timeline

10:00 AM: The issue was detected when monitoring alerts indicated a sudden spike in server response time.
10:15 AM: Engineers noticed the unresponsiveness of the web application and initiated an investigation.
10:30 AM: Initial assumption pointed to a potential database overload, triggering a thorough examination of the database server.
11:00 AM: Misleadingly, the investigation focused on a potential DDoS attack due to the unexpected traffic surge.
11:30 AM: The incident was escalated to the infrastructure team and senior database administrators.
12:00 PM: After extensive analysis, it was confirmed that the misconfigured load balancer caused the traffic overload on the database server.
2:00 PM: The incident was resolved by reconfiguring the load balancer to distribute traffic evenly and implementing additional monitoring for traffic spikes.

## Root Cause and Resolution

**Root Cause:** The misconfigured load balancer was directing all incoming traffic to a single database server, causing an overload and subsequent unavailability.
**Resolution:** The issue was fixed by reconfiguring the load balancer to distribute traffic across multiple database servers and implementing stricter traffic management policies.

## Corrective and Preventative Measures

**Improvements/Fixes**: Implement automated checks for load balancer configurations, enhance monitoring for traffic distribution, conduct regular load testing to simulate traffic surges.
**Tasks**:
  Patch load balancer configuration script to include automated checks for traffic distribution.
  Add real-time monitoring for load balancer performance and traffic distribution.
  Conduct load testing scenarios to simulate traffic spikes and validate system resilience.

This postmortem outlines an outage that occurred due to a misconfigured load balancer, resulting in a complete service unavailability. The incident was detected through monitoring alerts, leading to a thorough investigation that initially pursued misleading paths. The root cause was identified as the misconfigured load balancer, causing a traffic overload on the database server. The issue was resolved by reconfiguring the load balancer and implementing additional monitoring. To prevent similar incidents, corrective measures include automated checks, enhanced monitoring, and regular load testing. Specific tasks such as patching the load balancer configuration and conducting load testing were outlined to address the issue effectively.
