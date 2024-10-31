---
Title: Lab 5 - Signature-Based Malware Detection and Removal
---

## Overview

Keeping malware off a system is crucial because malware can cause serious harm to both individuals and organizations. Some reasons why it is essential to keep malware off a system:

**Data Theft**: Malware can steal sensitive information, such as usernames, passwords, credit card numbers, and other personal data. This information can be used for identity theft, fraud, and other malicious activities.

**System Performance**: Malware can slow down a system's performance, causing programs to crash, web pages to load slowly, and other issues that can negatively impact productivity.

**Network Security**: Malware can also spread over a network from one computer to another, potentially infecting an entire organization's infrastructure.

**Financial Loss**: Malware can cause financial loss by disrupting business operations, stealing sensitive data, or extorting money from victims through ransomware attacks.

**Reputational Damage**: Malware attacks can damage an organization's reputation, leading to lost customers, decreased revenue, and other negative consequences.

<div style="page-break-after: always"></div>

In an enterprise environment, you would use an Endpoint Detection Response (EDR) solution to prevent malware infection. EDRs are amazingly capable programs that are able to identify a program as malicious based off its behavior, and EDR is able to stop its execution before it happens, all while feeding information back to a centralized console. The most capable solutions on the market include Microsoft Defender which comes with Windows, Crowdstrike Falcon, and SentinelOne Singularity.

Before the modern malware defense landscape became as sophisticated as today, most people relied on signature-based malware detection. An Anti-virus (AV) program would have a collection of hashes that match up to known malicious programs that it constantly compares any running programs against. If a program has a hash matching a malicious program, it would be killed by the AV program. Can you think of any ways to circumvent this kind of protection? Read [here](https://www.attackiq.com/glossary/pyramid-of-pain/) about the "Pyramid of Pain", a threat intelligence model created by [David J Bianco](https://x.com/DavidJBianco) to learn why EDRs are more useful than a simple AV. If you're interested in this and want to learn more, check out BYU CSA's Threat Intelligence emphasis meetings, once a month at 7PM in CTB385 on Tuesdays.

![Pyramid of Pain](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkiz9ryl7uWrYfI1ocHQaqAyXUiN2JTtCsIQ&s)

## Instructions

You will be given CLI access to a virtual machine via SSH, and your task will be to find and remove any file with a list of given MD5 hash values by creating a simple AV program that uses signature-based malware detection.

Your main objective will be to keep your system clean of malware and fix the damage that it does. You will be able to access a global board that shows your machine's malware status.

Every 5 minutes, your system will be checked for any files that match the malicious hash values. If any files are found on your system or the website is not working correctly, then you will fail that check. You must pass 12 consecutive checks to pass the lab. The malware will be limited to the following directories and subdirectories within the list:

```
/etc
/home
/var
/dev
/bin
/usr
```

You are **NOT** permitted to use any form of existing anti-malware or program. You must write and implement your own program to find and remove the malicious file when found.

You may use any programming language you want to although bash or python are recommended. Malicious files will be randomly placed in different locations within the system throughout the lab. The program you write must find and remove the file and fix any damage that malware may have caused. 

The system you have been given runs an Apache web server that runs a basic index page that must return a 200 status code and have the correct content to be considered working. You will also fail the status check if the code or content changes.

The malware will not do anything to affect your access to the machine permanently, but it may affect any running programs and services.

<div style="page-break-after: always"></div>

## Rules

You are confined to using the account you are given to log in. You may use `sudo`, but **you are not allowed to switch to the root user or any other user.**

**DO NOT** change the firewall or SSH configurations or access.


**DO NOT** do anything to alter or affect the `blackteam` account, which includes but is not limited to:
 - Changing the `blackteam` password
 - Removing the `blackteam` SSH key
 - Changing the `blackteam` account permissions
 - Killing any scripts that the `blackteam` is running
 - Deleting the `blackteam` account
 - Editing the contents of the `/home/blackteam` directory
 - Deleting the account `/home/blackteam` directory or any of its contents


 You must write your own custom script to find, remove, and fix the malware and any damage that it has caused. Using any existing antimalware programs is not permitted.

 Consciously violating the above rules will be considered cheating and you will receive a 0 on the lab.

 Do not turn off your VM, you will not be able to turn it back on again.

## Hash Values

These are the *known* hash values of malicious files.

1. `4bc8448b818a983db84f44a4fafd60c4`
2. `8e5d5629672fcf8664bc28f42f79453f`
3. `d35482baeab98cd49621866021e9e6fa`
4. `5d80aaea305d1cb46b2e987270a3aa95`

The hackers may also alter files to create files with hashes we are unaware of.


Answer the questions using the `Write Up` file provided and include all necessary screenshots. There should only be one screenshot for each title in the document. 

<div style="page-break-after: always"></div>

## Scoreboard

The scoreboard can be found at `172.16.1.2`. It has these 6 columns:
1. User ID
    - Unique number value that you will receive in an email
1. VM Scoring
    - A green-up arrow will be displayed if the scoring engine can score your VM. If it cannot be scored a red down arrow will be displayed.
1. Service Active
    - A green-up arrow will be displayed to indicate whether the Apache web server is working correctly. If it is not a red down arrow will be displayed.
1. Malware Detected
    - A green-down arrow will be displayed if there is no malware found on your VM. If there is even 1 malware file present a red up arrow will be displayed.
1. Malware Count
    - A numerical number showing how many malware files are present on your system.
1. Consecutive Checks Passed
    - A numerical number showing how many consecutive checks your VM has passed. This will stop increasing when it has reached 12.


## Web page

The website must be accessible on port 80, located in the file `/var/www/html/index.php`, and return a 200 status code.

```html
<!DOCTYPE html>

<html>
    <head>
        <title>Welcome to my malware free website</title>
    </head>
    
    <body>
        <h1>Hello, world!</h1>
        <p>Good thing the hackers can't change this!</p>
    </body>
</html>

```

<div style="page-break-after: always"></div>

## Write Up
Answer the questions in the write up template. Include the screenshots and the script you used to detect and remove malware.

{% comment %}
We use HTML here for the links because if you use MarkDown Jekyll converts a link to a .md file into a link to a rendered .html file.
{% endcomment %}
* <a href="Lab-5-Write-Up.docx" download>Click here to download the write up template in MS Word .docx format</a>
* <a href="Lab-5-Write-Up.md" download>Click here to download the write up template in MarkDown format</a>

## Requirements

[ ] 80 Points - 12 Consecutive checks have been passed using a custom-written automated script  
[ ] 20 Points - Write up

## Submission
Create a single PDF from one of the given `Write Up` templates that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. No other file format will be accepted.

* If you use the .docx template, edit your writeup in Microsoft Word or Google Docs and use the export to .PDF function.
* If you use the MarkDown template, the [Markdown PDF VS Code add-in](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) is among the best options. Regardless, make sure the method you use includes your images.