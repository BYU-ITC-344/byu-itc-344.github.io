---
title: Lab3 Backups and Integrity Checking
---
# Lab 3 - Backups and Integrity Checking
 
## Overview
 
Backups are essential to data management and can be critical in preventing data loss, whether due to a hardware failure, accidental deletion, or a malicious attack. Backing up your data ensures that you can restore your important files and data in case of such events, minimizing the impact of any data loss or breaches.  
 
Without backups, data loss can have serious consequences, especially in a business or organizational context where critical data and information may be lost, resulting in financial losses, legal liabilities, and reputational damage.  

In addition to providing a safety net in case of data loss, backups can also help in disaster recovery and continuity planning. In the event of a disaster such as a fire, flood, or another natural disaster, having backups can help organizations quickly restore their operations and minimize the impact of the disaster. 
 
<div style="page-break-after: always"></div>

## Instructions

### Step 1: Chose A Solution
 
Many backup solutions are available to use. Some of which are listed below, choose one that would best meet the needs of this lab and implement it.
 
Note: Some of these will not be suitable for the lab they are just examples. It will be up to you to find and implement a suitable solution.

**Duplicati:** Duplicati is a free and open-source backup software that works on Windows, Linux, and macOS. It supports various storage providers such as local storage, FTP, SFTP, Amazon S3, Google Drive, and more. It offers encryption and deduplication features to optimize backup storage.  

 
**Bacula:** Bacula is a network backup solution that supports Windows, Linux, and other Unix-like systems. It provides features like backup scheduling, data encryption, client-server architecture, and flexible storage options. Bacula is designed for enterprise-level backup needs.  
 

**Amanda:** Amanda (Advanced Maryland Automatic Network Disk Archiver) is an open-source backup solution that works on Windows, Linux, and Unix-like systems. It supports various backup methods like full, incremental, and differential backups. Amanda also offers a client-server architecture and supports tape storage.  
 

**rsync:** While not a dedicated backup solution, rsync is a powerful file synchronization tool that can be used for backup purposes. It works on both Windows (using tools like cwRsync or DeltaCopy) and Linux. Rsync efficiently copies and synchronizes files between different locations and supports features like incremental backups and compression.  
 

**Clonezilla:** Clonezilla is an open-source disk imaging and cloning tool that can be used for both backup and recovery purposes. It works on Windows and Linux and supports various file systems. Clonezilla can create full disk or partition backups and allows you to restore them when needed.  
 
### Step 2: Backup time
 
Choose 1 Linux and 1 Windows VM to back up and 1 VM that will become the backup server. Do not make your backup server a client or you will create an infinite backup loop.  

 
Make sure to consider the different options and types of backups and why you might use one over the other in different cases.   
 
### Step 3: Fight the troll

In this step, you'll be given credentials for a new VM. You’ll also need to connect using a different VPN than the one you’ve used previously.

Your mission is to deal with a mischievous troll who’s tampered with key system files, allowing himself and his friends access to your machine. Your goal is to maintain the integrity of the system, removing illegitimate users and restoring legitimate files. You will have to revert the troll's manipulation of:
- /etc/shadow
- /etc/passwd
- /etc/group

Additionally, you will remove files of illegitimate users and restore from backups legitimate files the troll edits or removes from /home. All the original home directory files can be found in the `files.zip`. 

**Important:**  
- Do **NOT** delete the `shadow`, `passwd`, or `group` files—removing these will brick your VM.
- You should only have to edit the `shadow`, `passwd`, and `group` files once.
- You do not have edit the `shadow`, `passwd`, and `group` files directly!
- Only remove users without a underscore in their username. Users with underscores, as well as the `blueteam`, `blackteam`, and system users, should **not** be deleted, as this could also break your VM.

The troll is quick, so you’ll need to check file integrity regularly. While you can’t stop the troll from remaining in your system, you *can* prevent him from making permanent changes to your files by restoring from backups.

You are **not permitted** to alter the firewall, SSH settings, or the `Blackteam` account. Keep restoring your backups to frustrate the troll. Eventually, he’ll give up when he realizes his changes aren’t sticking!

To complete the lab, you'll need to pass 200 integrity checks. These checks occur every 2 to 5 seconds. You can monitor your progress at `172.16.2.2`, where the scoreboard will display 5 columns:

- **VM Score**: A green-up arrow indicates that the scoring engine successfully scored your VM. A red down arrow means the engine was unable to score your machine.
- **Users**: A red down arrow appears if any malicious users remain on the system. Once all malicious users are removed, it will switch to a green-up arrow.
- **File Integrity**: If any files fail to match their original hash, a red down arrow will be displayed. When all files match their original hashes, the arrow will turn green.
- **Checks Passed**: Displays the number of checks that have been passed, with a maximum count of 200.
- **Correct Files**: Displays the number of files that have not been corrupted. show be at 64
 
### Step 3: Write up
 
Answer the questions in the `Write up` file and include any other necessary screenshots or code to prove that you have met the pass-off requirements.  
* [Click here to download the write up template in MS Word .docx format](Lab-3-writeup-template.docx){: download}
* <a href="Lab-3-writeup-template.md" download>Click here to download the write up template in MarkDown format</a>.
 
## Requirements
 
[ ] 20 Points - 1 Windows VMs have been backed up  
[ ] 20 Points - 1 Linux VMs have been backed up   
[ ] 10 Points - 1 VM has been designated the backup server  
[ ] 30 Points - 200 Checks have been completed  
[ ] 20 Points - Write up   
 
## Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been satisfied. Upload the PDF to Learning Suite. Any other file format will not be accepted.