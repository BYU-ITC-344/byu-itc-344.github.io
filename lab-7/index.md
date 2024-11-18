---
title: Lab 7 - Operating System Defense
---
# Lab 7 - Operating System Defense

## Introduction

Welcome to operating systems hardening. This lab consists of a single virtual machine that you will be in charge of defending and hardening against external and internal security risks and attacks. For the duration of this lab, you will be responsible for a Ubuntu machine and its security. There will be a scoring engine and feedback that you can check, and it will give you feedback as you progress. Read over the instructions for the lab and virtual machine carefully, and good luck.

![](./meme.jpeg)

## Unique Identifier

In the `/opt` directory of each virtual machine, there is an id.txt file that is already populated. Do not alter the id; the scoring engine will stop giving you points.

## Scoring

Scoring will update approximately every minute. You can find your score and a points breakdown at `172.16.16.2`. You can login with your user id and the scoreboard password you received in an email. 


There are multiple ways to achieve some of the objectives, and we may not have been able to account for them all, so if you believe your solution to a problem should have given you points, try another method, and then if that still doesn't work reach out to a TA. It may also be that you fix or harden something for which no points are awarded.

There will be a total of 460 points, but to get full points for the lab, you will only need 350. Anything over that will significantly improve your learning but will not give you more points toward your grade.

## Connecting to the machine

You can connect to the VM via SSH. If you lock yourself out and require the TA to let you back into the VM, there will be a 10-point penalty each time it needs to be done. You should change your user's password after logging in but do not forget it. If the TA has to reset your password, that will also incur a 10-point penalty every time.

## Scenario

You have been hired as a new security consultant at the local government office in Pawnee, Indiana. You have been informed by your new boss Ron that your predecessor spent all of his time "working from home" at the local park doing nothing but recreational activities. Your first job is to assess the office's main computer. There have been several tickets raised about their systems acting weird. Your job will be to investigate, fix any problems you find, and report back to Ron. There have been many complaints, mainly about the inability to list out files correctly.

You can work on this project by yourself or in a group of 2 to 3 people. Do not collaborate outside your group. Tell TAs who you are working with.

## Report

> Notice: Your reports must be your own work! There is no collaboration on the reports.

As part of the assignment, you will write a report on any modifications and remediation you have performed on the office systems. The report will include 2 parts. The report should be uploaded to Learning Suite as a PDF. No other file format will be accepted!

The report should be logical, flow well and have good spelling, grammar, and punctuation.

### Part 1
Part one will be in the form of a memo to your new boss Ron, and should detail the following:

1. List who you worked with ( if you did the lab solo indicate that )
1. What did you find
1. What did you do to fix it
1. Suggestions for new policies and practices to safeguard their computer systems


The memo should be 1 to 2 pages. Your boss is also not a tech guy at all, and the terminology used needs to be understood by a non-technical audience. 

### Part 2
Part two will be a technical report that should detail:

1. What you found
1. What did you do to fix it

The technical report should be 2-4 pages. 

## Templates
The report templates can be found here.
* [Click here to download the write up template in MS Word .docx format](Lab-7-Technical-Report.docx){: download}
* <a href="Lab-7-Report-Template.md" download>Click here to download the write up template in MarkDown format</a>.

## Rules

1. Any attempt to manipulate the scoring machine will be considered cheating and result in an automatic failure of the assignment
1. This assignment is graded on an individual basis; however, you may collaborate in a group of 2 to 3 people to help bounce ideas off each other. Do not share details of the lab outside your group. 
1. Inform TAs who you are working with. No daisy chaining of groups!
1. The assignment is an open note and open internet in read-only mode. You cannot post questions to any forum or website for help, but you can use anything publicly available on the internet. Messaging or conferring with anyone is also not allowed.
1. You are not allowed to attempt to access other students' VMs or the scoring engine. Doing so will be considered cheating and result in failing the assignment.
1. Do not remove the ssh key for the `blackteam` account or change the password. Doing so will lock you out of the scoring engine, resulting in no more points. 
1. Do not disable, delete or modify scripts or services labeled with `blackteam`.
1. Do not remove any authorized users or their home directories. Doing so will cause you to lose points. 
1. Do not modify the unique id found in the `id.txt` file
1. You are not permitted to perform major version upgrades on the virtual machines but updating or upgrading packages is allowed. 
1. You are not allowed to block the IP address of the attack machine(s).
1. Do not change the IP address of your VM.
1. You can reboot your VM at any time, but if you shutdown the VM, you will have no way to power it back on without TA intervention
1. At the end of the lab, your VM must be functioning; you cannot leave it in a bricked state and call it good. This system is a simulation of a live production system and should remain up.

##  Guidelines
1. Authorized administrator passwords are correct when the lab starts, but this is not guaranteed to remain the case.
1. You can check your current score by going to `172.16.16.2` and using your unique id contained in the lab email to log in.
1. If your VM becomes corrupted beyond use or can no longer be salvaged at any point, it can be reset by the TA to its original state. Doing so will reset your points to 0, and you will not be given more time on the assignment. Resets will only be performed during regular business hours. Do not message the TAs before 9:00 am or after 5:00 pm. The first reset will not have a penalty, but any after that will incur a 10-point penalty per reset.
1. Make sure to read the documentation that details what services should be running, who the valid users and administrators are, any company requirements for that VM, and what software packages are allowed or prohibited. 
1. The lab's overall goal is to find and fix as many security, configuration, or policy issues as possible. However, you may make a change that could fix a problem that is not scored or do it in a way not recognized by the scoring engine.
1. Some things to look out for include removing users, password policies, unauthorized scripts or shells, non-work related materials, prohibited software, etc. 
1. 48 hours after the lab has started, the red team will go from passive to active, so make sure you start on the lab or early
1. There is a total of 670 Points available, but only 350 are needed to get full points on the lab. Additional points will not change your grade or count as extra credit.

## Grading 

[ ] 350 Points - Finding and fixing problems with the VM  
[ ] 150 Points - Written Report  

[ ] Total 500 Points  