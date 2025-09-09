#  Lab 5 - Signature-Based Malware Detection and Removal

## **Overview**

Malware poses a serious risk to both individuals and organizations. Preventing malware infections is crucial to maintaining confidentiality, integrity, and availability. Some major impacts of malware include:

* **Data Theft**: Stolen credentials, credit cards, or private data can be used for identity theft and fraud.
* **System Performance**: Malware slows down systems, crashes programs, and reduces productivity.
* **Network Security**: Malware spreads laterally, potentially compromising an entire network.
* **Financial Loss**: Business operations may be disrupted, or ransomware may demand payment.
* **Reputation Damage**: Customers may lose trust in an organization that suffers a malware incident.

In enterprise environments, modern defenses rely on **Endpoint Detection and Response (EDR)** solutions like Microsoft Defender, CrowdStrike Falcon, or SentinelOne Singularity. These tools detect suspicious **behavior** instead of just static signatures.

Before EDR, most people relied on **signature-based detection** (traditional antivirus). AV compared running programs to a database of known malicious file hashes. If a match was found, the program was terminated. While still useful, this method struggles against **polymorphic malware**.

To better understand why modern defenses are stronger, review David Bianco’s **Pyramid of Pain**, which shows how hard it is for attackers to adapt when defenders move from signatures to behaviors.

![](https://www.attackiq.com/wp-content/uploads/2019/06/blog-pyramid-pain-01-1024x576.jpg)


## Instructions

You will access a **Linux VM via SSH** and must write a simple **custom antivirus script** to detect and remove malware using **signature-based detection**.

### Key Tasks

1. **Find malware files**: Compare file hashes against a provided list of MD5 hashes.
1. **Remove malware files**: Delete them from the system.
1. **Repair services**: If malware disrupts your system (e.g., Apache server), restore it.
1. **Automate detection**: Your script must run continuously and pass **12 consecutive scoring checks**.

### System Behavior

* The **scoring engine** checks your VM every 5 minutes.
* To pass:
  * No malicious files should exist.
  * Your Apache web server should return the correct webpage with a **200 status code**.
* Malware will only appear in the following directories:

```
/etc
/home
/var
/dev
/bin
/usr
```

## **Rules**

* You may use **sudo**, but you **cannot switch to root** or another account.
* **Do not interfere with the `blackteam` account** (e.g., don’t delete, change password, kill scripts, modify SSH keys, etc.).
* Do not modify firewall or SSH configs.
* Do not turn off your VM (you won’t be able to turn it back on).
* You must write your **own script**. Existing antivirus software is not permitted.
* Modifying binary files is not allowed.

Violating these rules = **0 on the lab**.

## Hash Values

Your script must scan for these known malware hashes:

1. `4bc8448b818a983db84f44a4fafd60c4`
2. `8e5d5629672fcf8664bc28f42f79453f`
3. `d35482baeab98cd49621866021e9e6fa`
4. `5d80aaea305d1cb46b2e987270a3aa95`

> Hackers may alter or create new files to bypass detection. Be prepared to restore services even if malware isn’t hash-matched.


## Apache Website Requirements

Your system runs an Apache web server serving `/var/www/html/index.php`.

It must always:

* Be accessible on **port 80**.
* Return a **200 OK status code**.
* Contain the following content:

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

## Scoreboard

Accessible at `172.16.1.2`. It displays:

1. **User ID** – your unique number (emailed to you).
1. **VM Scoring** – green arrow if your VM is being scored, red if unreachable.
1. **Service Active** – green arrow if Apache is running correctly.
1. **Malware Detected** – green arrow if no malware is found, red if malware exists.
1. **Malware Count** – number of malicious files detected.
1. **Consecutive Checks Passed** – must reach **12** for full credit.


### Write up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- **Answers to all questions**
- **Copy of your script**
- **Screenshot of the scorboard**

#### Templates

- <a href="lab-5-writeup-template.docx" download>Download the MS Word Write-Up Template (.docx)</a>
- <a href="lab-5-writeup-template.md" download>Download the Markdown Write-Up Template (.md)</a>


## Requirements and Points

### Grading Breakdown (100 Points Total)

| **Task**               | **Deliverable**                                                                        | **Points** |
| ---------------------- | -------------------------------------------------------------------------------------- | ---------- |
| **Custom Script**      | Working script that finds/removes malware based on hash values and repairs any damage. | **25**     |
| **Scoreboard Success** | Pass **12 consecutive checks** on the scoreboard.                                      | **50**     |
| **Technical Write-Up** | Completed template with answers + screenshots.                                         | **25**     |

### Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.
