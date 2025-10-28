# Homework 6 – Windows Event Logging & Security Monitoring

## Learning Outcomes

By completing this assignment, you will:

- Understand how **Windows security subsystems** generate and record events.
- Configure and test **auditing policies** for authentication, privilege use, and PowerShell execution.
- Gain experience using **Event Viewer** to identify suspicious activity.
- Develop skills in writing concise, technical documentation of monitoring and analysis.


## Assignment Overview

Windows Event IDs are unique numerical codes used by the Windows operating system to identify and categorize specific system, security, and application events recorded in the Event Viewer. Each Event ID represents a particular type of activity—such as a user login, process creation, policy change, or system error. By monitoring these IDs, administrators and security professionals can trace user actions, detect anomalies, and investigate potential security incidents. Understanding common Event IDs, particularly those related to authentication, privilege use, and process tracking, is essential for effective auditing, forensic analysis, and maintaining system integrity.

Windows maintains a detailed record of system activity through **event logs**, which are vital for both troubleshooting and **security monitoring**. In this assignment, you will:

1. Configure **audit policies** for authentication, PowerShell activity, and privilege use.
1. Trigger test events (e.g., failed logins, privilege escalation attempts, and PowerShell script execution).
1. Use **Event Viewer** to analyze the logged events and map them to relevant **operating system subsystems** (such as logon, access control, and process creation).
1. Document your findings with **screenshots and explanations**.


## Assignment Instructions

### Step 1: Configure Auditing

1. Open **Local Security Policy** (`secpol.msc`) on your Windows 11 VM.
1. Navigate to *Advanced Audit Policy Configuration → System Audit Policies - Local Group Policy*

1. **Logon/Logoff → Audit Logon**

  - **Enable:** Success and Failure
  - **Purpose:** This policy tracks all attempts to log on or log off the system—whether interactive (via console or RDP), network-based, or service logons.
  - **Why it matters:**
    - **Success events** show legitimate user activity (e.g., user logins, scheduled tasks running under service accounts).
    - **Failure events** can indicate brute-force attempts, misconfigured services, or potential unauthorized access attempts.

1. **Detailed Tracking → Audit Process Creation**

  - **Enable:** Success and Failure
  - **Purpose:** This policy logs every time a process is created or started, providing visibility into what commands or executables are being launched.
  - **Why it matters:**

    - Helps identify malicious scripts, command-line tools, or suspicious executables being run by attackers or compromised accounts.
    - Enables correlation between logon events and subsequent process activity.
  

1. **Privilege Use → Audit Sensitive Privilege Use**

  - **Enable:** Success and Failure
  - **Purpose:** This policy tracks attempts to use sensitive Windows privileges (e.g., **SeDebugPrivilege**, **SeBackupPrivilege**, **SeShutdownPrivilege**).
  - **Why it matters:**

    - Detects misuse of elevated privileges or privilege escalation attempts.
    - Identifies when administrators or malware attempt to perform powerful operations like loading drivers, modifying security tokens, or accessing protected processes.

1. Take a screenshot showing all the settings you configured above.

### Step 2: Trigger Events

Perform controlled actions to generate test logs:

  - **Failed Login Attempts**

    - Log out and attempt to log in with incorrect credentials 2–3 times.

  - **Successful Logon**

    - Log in with your correct account.

  - **Privilege Escalation Attempt**

    - Attempt to run a program as Administrator from a standard user account.

  - **PowerShell Activity**

    - Open PowerShell and run:

    ```powershell
    Get-Process
    ```
    - Run a command that interacts with the file system.

* **Process Creation**

  * Launch a standard application (e.g., Notepad or Calculator).

### Step 3: Analyze in Event Viewer


1. Open **Event Viewer** (`eventvwr.msc`).
1. Navigate to:

  - `Windows Logs → Security` for authentication and privilege events.

  - `Applications and Services Logs → Microsoft → Windows → PowerShell → Operational` for PowerShell events.
1. Identify specific **Event IDs** for the events you triggered in Step 2. 


### Step 4: Write Technical Report

Write a **2-page technical report** (\~500–750 words) that includes:

1. **Introduction** – Importance of event logging in Windows security.
1. **Configuration Summary** – What policies you enabled and why.
1. **Event Analysis** – Screenshots and explanations of:
  - **Failed Login Attempt**
  - **Successful Logon**
  - **Privilege Escalation Attempt**
  - **PowerShell Activity**
  - **Process Creation**
1. **Conclusion** – How event logging helps with security monitoring and incident response.


## Deliverables

| **Task**                        | **Deliverable**                                                                   | **Points** |
| ------------------------------- | --------------------------------------------------------------------------------- | ---------- |
| Configure auditing policies     | Screenshots of policy settings enabled                                            | 20        |
| Trigger and capture test events | Evidence of failed logins, PowerShell use, privilege escalation, process creation | 20         |
| Event analysis                  | Screenshots of 5+ relevant events with explanations                               | 30         |
| Technical report                | 2 pages, professional format, clear writing                                       | 30         |



## Submission Requirements

* Submit a **single PDF** containing:
  * Screenshots of auditing configuration and event logs.
  * 2-page technical report.

* Upload to **Learning Suite**. Other formats will not be accepted.
