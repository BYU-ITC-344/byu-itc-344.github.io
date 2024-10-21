---
title: Lab4 Password Recovery
---
# Lab 4 - Password Recovery

## Overview

People like Bob, Alice, and Eve forget their passwords, it happens all the time. Most websites and services have a way for you to reset your password should you forget it. However, operating systems are a little trickier but there are ways to change the password and let yourself back in. Use the magic of cybersecurity and get into the VMs.

You may collaborate with one another while breaking into the VMs, but you are not allowed to discuss the hashes with one another. The TAs will assist with any technical issues. TA's will not give walkthroughs of breaking into the VMs but will help you find resources if you are struggling.

<div style="page-break-after: always"></div>

## Instructions
2 VMs will be uploaded to your ProxMox instance. One for Linux and another for Windows 10. Your task will be to break into each VM using whatever tools or methods you deem appropriate. ***Warning*** If you do plan on downloading hacking or malicious tools make sure to do it off the BYU network.

Additionally, you will break into a physical Mac device. On Mac there will be an account called 'flag' and on the Linux VM there will be an account called 'bob'. You will need to recover the hashes for these accounts and then crack the passwords. For the Windows VM, you will only need to break in. A Windows password hash will be given to you separately. The Windows hash does not relate to any user from the Windows VM. We have provided a hash for you because extracting Windows hashes is difficult without special tools.  

>Note: Please look at the write-up while doing the lab so you know what deliverables are required.


### Step 1 - Breaking In - VMs

Once you find the VMs on your instance, your task will be to break into them. For the Linux VM do ***NOT*** reset the password for the 'bob' account. Do ***NOT*** reset the password for the account called `bob` You will need to obtain `bob`'s password hash and break it.

### Step 2 - Breaking In - Mac

Since we can't install a Mac VM on anything other than Mac hardware, we have obtained 4 Macs that can be used for this assignment.

1. Break into an iMac
1. Set a new password for an account other than `flag`

If you break the Mac operating system or hardware in any way you will lose the 30 points associated with the Mac portion of this lab. 

If you change the flag password it will be considered cheating and you will receive a 0 on this lab.

### Step 3 - Cracking Passwords

You will need to extract the password hashes from a Linux operating system and another from the Mac. The Windows hash will be given to you. Your task will be to find what the passwords are. 

You will use three different approaches to cracking a password. For the Linux password, you will use a custom-made wordlist using data about the format of the password, for the Windows 10 password you will use a rainbow table, and for the Mac a list of common passwords. 

The company the Linux password belongs to specifies the format of their employee's passwords to the extreme and instead of making it more secure it has done the opposite. 

Create a password list of all combinations that match this pattern. Three letters followed by a `-` then three numbers. The first password in the sequence would be `aaa-000` and the last would be `zzz-999`.

To crack the Windows password you will use rainbow tables using the program `Ophcrack`.

Cracking the Mac password will require a common wordlist. 

### Step 4 - Write Up

Answer the questions in the `Write up` file and include the needed screenshots
* [Click here to download the write up template in MS Word .docx format](Lab-4-writeup-template.docx){: download}
* <a href="Lab-4-writeup-template.md" download>Click here to download the write up template in MarkDown format</a>.

<div style="page-break-after: always"></div>

## Requirements
**Please** check the writeup for specifics you need to submit. <br>
[ ] 15 Points - Get into the Windows VM and reset the password for an account other than the flag account  
[ ] 15 Points - Get into the Linux VM and reset the password for an account other than the bob account  
[ ] 15 Points - Get into the Mac and reset the password for an account other than the flag account  
[ ] 15 Points - Crack the Linux password  
[ ] 15 Points - Crack the Windows password  
[ ] 15 Points - Crack Mac password  
[ ] 10 Points - Write up  

## Submission

Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite.