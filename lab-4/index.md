# Lab 4 – Password Recovery

## Overview

People like Bob, Alice, and Eve forget their passwords — it happens all the time. Most websites and services have a **password reset mechanism**, but operating systems can be trickier. Fortunately, there are still ways to reset or recover access. In this lab, you will use the **magic of cybersecurity** to get into two virtual machines (VMs) and practice password recovery techniques.

This lab will give you hands-on experience with:

* Accessing locked systems.
* Extracting password hashes.
* Cracking passwords with custom wordlists and rainbow tables.
* Documenting your process and results like a professional.

You may collaborate with classmates while breaking into the VMs, but **you are not allowed to share or discuss the actual hashes** with one another. The TAs will assist with technical issues (e.g., VM startup problems) but will **not provide walkthroughs** of breaking into the VMs. They may, however, point you toward resources if you get stuck.

## Instructions

### Step 1 – Breaking In: VMs

Two VMs will be uploaded to your Proxmox instance:

* **Linux VM**
* **Windows 10 VM**

Your first task is to **break into each VM**.

* **Linux VM**

  * You must recover the password hash for the account called `bob`.
  * **Do NOT reset `bob`’s password.** If you reset it, you will not be able to complete the cracking requirement.
  * You will, however, need to demonstrate that you can **reset the password for a different user account** (to show you can regain access through privilege escalation, the root account can be used for this).

* **Windows VM**

  * Your task is to **break into the VM** and gain access.
  * For the password cracking portion, a **Windows password hash** will be provided separately. This hash does **not** correspond to any user in the Windows VM.
  * We provide the hash because extracting Windows password hashes requires specialized tools not included in this lab.


### Step 2 – Cracking Passwords

Once you have access, your next task is to **crack the passwords**.

* **Linux Password Cracking**

  * Extract the `bob` account’s password hash from `/etc/shadow`.
  * The company enforces a **very weak password format**:

    ```
    <three lowercase letters>-<three numbers>
    ```

    Examples: `aaa-000`, `abc-123`, `zzz-999`.
  * Generate a **custom wordlist** containing all possible passwords in this format.
  * Use a cracking tool (e.g., **John the Ripper** or **Hashcat**) with your wordlist to recover `bob`’s password.

* **Windows Password Cracking**

  * You will be given a **pre-extracted Windows password hash**.
  * Use **Ophcrack** with rainbow tables to crack the password.
  * Take a screenshot of the cracked password in Ophcrack.

### Step 3 – Write-Up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- **Answers to all questions**
- **Screenshots for each of the following:**
    1. Proof of breaking into both VMs.
    1. Screenshot of password hash extraction for bob.
    1. Screenshot of your custom wordlist (sample output).
    1. Cracking results for Linux (bob’s password).
    1. Cracking results for Windows (rainbow table + recovered password).
    1. Resetting a different Linux account’s password.
- **Any commands or scripts you used.**  

#### Templates

* <a href="lab-4-writeup-template.docx" download>Download the MS Word Write-Up Template (.docx)</a>
* <a href="lab-4-writeup-template.md" download>Download the Markdown Write-Up Template (.md)</a>


### Requirements and Points

### Grading Breakdown (100 Points Total)


| **Task**                      | **Deliverable**                                                                                                         | **Points** |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------- |
| **Windows VM Access**         | Demonstrate that you can log in or bypass login on the Windows VM. Include a screenshot.                                | **25**     |
| **Linux VM Access**           | Gain access and show that you can reset the password for an account other than `bob`. Include a screenshot.             | **20**     |
| **Linux Password Cracking**   | Extract the hash for `bob` and crack it using a custom wordlist. Show screenshots of the process and result.            | **25**     |
| **Windows Password Cracking** | Crack the given Windows password hash using Ophcrack with rainbow tables. Provide a screenshot of the cracked password. | **10**     |
| **Technical Write-Up**        | Submit the provided write-up file as a PDF. Must include answers to all questions + required screenshots.               | **20**     |

### Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.