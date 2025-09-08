---
title: Lab3 Backups and Integrity Checking
---

# Lab 3 - Backups and Integrity Checking
 
## Introduction
 
Backups are essential to data management and can be critical in preventing data loss, whether due to a hardware failure, accidental deletion, or a malicious attack. Backing up your data ensures that you can restore your important files and data in case of such events, minimizing the impact of any data loss or breaches.  
 
Without backups, data loss can have serious consequences, especially in a business or organizational context where critical data and information may be lost, resulting in financial losses, legal liabilities, and reputational damage.  

In addition to providing a safety net in case of data loss, backups also play a central role in **disaster recovery and continuity planning**. In the event of a disaster such as a fire, flood, ransomware attack, or another large-scale disruption, having backups can help organizations quickly restore their operations and minimize the impact of the disaster.  


## Instructions

### Step 1: Choose a Backup Solution
Many backup solutions are available. Below are several examples. Choose one that best meets the needs of this lab and implement it.  

> **Note:** Some of these may not be fully suitable for the lab environment; it is your responsibility to research and determine which solution works best.

- **Duplicati:** Free and open-source backup software (Windows, Linux, macOS). Supports many storage providers (local, FTP/SFTP, Amazon S3, Google Drive, etc.). Offers encryption and deduplication.  
- **Bacula:** Enterprise-level network backup solution with scheduling, encryption, and client-server architecture. Supports Windows, Linux, and Unix-like systems.  
- **Amanda:** Open-source backup solution supporting full, incremental, and differential backups with a client-server architecture. Works across multiple OS platforms.  
- **rsync:** A file synchronization tool often used for incremental backups. Works across Linux and Windows (via cwRsync or DeltaCopy). Lightweight but highly efficient.  
- **Clonezilla:** Disk imaging and cloning tool, suitable for full system or partition backups. Restores systems to exact previous states.  

When selecting a solution, consider **encryption, storage location, restore reliability, and scalability**.  


### Step 2: Perform Backups
- Select **1 Linux VM** and **1 Windows VM** as your backup clients.  
- Designate a **separate VM as your backup server**.  
  - Do **not** make your backup server one of the clients, or you may create an infinite backup loop.  

Think about the **type of backup** you perform:  
- **Full Backup:** Copies everything (useful as a baseline, but storage-heavy).  
- **Incremental Backup:** Copies only changes since the last backup (efficient, but requires a full chain to restore).  
- **Differential Backup:** Copies changes since the last full backup (middle ground).  

### Step 3: Fight the Troll
In this stage, you will connect to a new VM (using a different VPN than before) and attempt to preserve its integrity despite active interference by a “troll” adversary.  

The troll tampers with critical system files, allowing illegitimate users access. Your mission is to **restore integrity and frustrate the troll** by continually reverting his changes.  

##### Tasks:
1. **Remove malicious accounts:**  
   - Delete all users **without underscores** in their usernames.  
   - Do **not** delete:  
     - Users with underscores  
     - `blueteam`, `blackteam`, or system accounts  
   - Deleting the wrong accounts could brick your VM.  

1. **Restore home directories:**  
   - Illegitimate users’ files must be removed.  
   - Legitimate user files that the troll tampers with must be restored from backups.  
   - Use the provided <a href="Files part 1.zip" download>Files Part 1.zip</a> and <a href="Files part 2.zip" download>Files Part 2.zip</a>  archive to restore original contents under `/home`.  

1. **Integrity checks:**  
   - The system will be scored every **2-5 seconds**.  
   - You must pass **200 integrity checks** total not cumulative.  
   - Monitor progress at <a href='http://172.16.2.2' target="_blank">http://172.16.2.2</a>. (You will need to be connected to the VPN to access the dashboard)

   The scoreboard displays:  
   - **VM Score:** Green = VM is responding; Red = scoring engine can’t connect.  
   - **Users:** Green = no malicious users; Red = at least one remains.  
   - **File Integrity:** Green = all files match hashes; Red = at least one file corrupted.  
   - **Checks Passed:** Counter toward 200 successful checks.  
   - **Correct Files:** Must remain at **64** legitimate files.  

> ⚠️ **Restrictions:** You may not alter firewall settings, SSH configuration, or the `Blackteam` account.  

Your persistence is key—keep restoring from backups until the troll gives up.  

### Step 4: Write-Up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- **Answers to all questions**
- **Screenshots for each of the following:**
    1. Screenshots proving successful backups for both machines.
    1. Screenshot of the backup configuration  
    1. Screenshot of the scoreboard showing **200 checks completed**.  
- **Any commands or scripts you used.**  

#### Templates

- <a href="lab-3-writeup-template.docx" download>Download the MS Word Write-Up Template (.docx)</a>
- <a href="lab-3-writeup-template.mdp" download>Download the Markdown Write-Up Template (.md)</a>


### Requirements and Points

### Grading Breakdown (100 Points Total)

| **Task**                                               | **Points** |
|--------------------------------------------------------|--------|
| Backed up **1 Windows VM**                             | 10     |
| Backed up **1 Linux VM**                               | 10     |
| Designated **1 VM as backup server**                   | 10     |
| Completed **200 integrity checks** against troll VM    | 40     |
| Completed **Write-Up** with explanations + screenshots | 30     |


### Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.