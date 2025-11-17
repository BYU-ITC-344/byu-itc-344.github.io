# Lab 7: Operating System Defense

## Acceptable Use Policy

Welcome to **CyberJousting**, an online cybersecurity range and training platform. To maintain a secure and productive environment, we have established this **Acceptable Use Policy (AUP)** to outline the expectations and responsibilities of all users. By accessing and using the CyberJousting network, you agree to adhere to the following terms and conditions:

- **No Expectation of Privacy**: There is no expectation of privacy while connecting to the CyberJousting network. Network traffic to and from competition resources may be monitored for security and compliance.  
- **No Illegal Activity**: Users are strictly prohibited from engaging in any illegal activities while connected to our network. Any detected illegal activity will be reported to the appropriate authorities.  
- **Scope of Activities**: Users are only allowed to perform activities that are within the defined scope of CyberJousting. Any out-of-scope activities will result in immediate blocking and banning from the platform.  
- **Authorized User Accounts**: Accounts are intended to be used solely by the authorized user. Unauthorized access or account sharing will result in suspension or banning.  
- **Ownership of Resources**: All internal CyberJousting resources, including infrastructure, code, and proprietary content, are the exclusive property of CyberJousting. These may not be copied, distributed, or used externally without explicit written permission.  
- **Respectful Behavior**: Discriminatory, rude, or disrespectful behavior towards other users, instructors, or staff is strictly prohibited. CyberJousting is committed to providing a respectful and inclusive environment.  
- **Non-Personal Entertainment Use**: The CyberJousting network may not be used for personal entertainment purposes. All activities must relate to training, learning, or authorized tasks.  

Failure to comply with this AUP may result in banning from the platform and potential legal consequences. CyberJousting reserves the right to update this policy at any time.


## Data Usage Disclaimer

At CyberJousting, your privacy and the responsible handling of your data is important to us. This Data Usage Disclaimer explains the types of data we collect and how it is used:

- **Scoring Data**: We collect data such as vulnerabilities discovered, vulnerabilities missed, time spent on labs, and reset requests.  
- **Anonymization**: All scoring data is anonymized within two weeks of the conclusion of each lab or competition.  
- **Retention**: Anonymized scoring data is retained as needed to improve our services.  
- **Account Security**: Accounts are intended for the assigned user only. Unauthorized use may result in suspension.  
- **Data Protection**: Data is stored securely, with access restricted to authorized personnel.  
- **Purpose**: Data is used to evaluate labs, make improvements, and refine training offerings.  
- **No Third-Party Sharing**: CyberJousting does not sell or share your data with third parties without your consent, unless required by law.  

By using the platform, you acknowledge and agree to this disclaimer.

## Rules

- Do not block port `2222` (used by the blackteam to score your machine).  
- Do not remove the Proxmox `qemu-guest-agent`.  
- Any attempt to manipulate or access the scoring machines is **cheating** and will be caught. Only access the scoring engine from your VPN, on ports `80` or `443`.  
- This is an **individual assignment**. Do not collaborate with other students. Direct all questions to the TAs.  
- Do not attempt to access other students’ VMs or the scoring engine.  
- Do not modify the **blackteam** account (e.g., password, SSH key, privileges). Doing so will lock you out and cost points.  
- Do not disable services/scripts owned by blackteam.  
- Do not remove authorized users or their home directories.  
- Do not perform major version upgrades on the VM.  
- Do not change your VM’s IP address.  
- You may reboot the VM, but shutting it down will prevent you from restarting it.  
- If your VM becomes corrupted or unsalvageable, a TA can reset it.  
  - First reset: no penalty.  
  - Each additional reset: **–10 points**.  
  - Resets only during normal hours (9:00 a.m. – 5:00 p.m.).  
- Your VM must be **powered on and scorable** when the lab ends.  
- Reporting legitimate bugs/vulnerabilities may earn **bonus points**, but this is not permission to pen test the infrastructure.
- The scoring engine runs from /opt/aeacus. All programs, services, and files located in—or related to—this directory are out of scope and must not be modified, deleted, or altered in any way.
- If an entire file is malicious, delete the file. If only a portion of the file is malicious, remove only the malicious portion while preserving the rest.


## Scenario

Welcome to **Veridian Solutions**!  

We are a cutting-edge technology company delivering innovative software solutions to businesses across multiple industries. With a skilled team and a passion for excellence, we aim to empower organizations with state-of-the-art tools that improve operations, productivity, and growth.  

As a **new Security Analyst**, you have been tasked with securing our main server to coordinate operations between our office and field operatives. The system may already be compromised. Your mission is to **identify, secure, and remove any malicious files or programs** before sensitive data is added to the server.  

## Getting Started

### SSH

You will connect to the VM using **SSH**. SSH securely allows you to access another machine’s command line.  

Run the following command from your terminal (CMD/PowerShell on Windows, or Terminal on macOS):  

```bash
ssh username@ipaddress
```

## System Requirements

### Users

User management is critical to security. Add, modify, or remove users as needed.

- Usernames: `firstnamelastname` (all lowercase).
- Password policy: at least **8 characters** with **1 uppercase** character.
- Use a strong hashing algorithm.
- The required group name is enclosed in the `()`

#### Authorized Administrators (sudo)

- Jason Smith – IT Manager
- John Baker – Network Administrator
- Nancy Davis – Data Analyst
- Albert Tay – Director of Fried Chicken
- blueteam – Security Analyst
- blackteam – IT Support

#### Leadership Group (leadership)

- Albert Tay – Director of Fried Chicken
- Ailbhe Feidlimid – CEO
- Sarah Jones – COO
- Ryan Williams – CMO
- Samantha Hill – CFO
- Kevin Nguyen – CTO
- Katie Wright – Director of Operations
- Emily Lee – Director of Marketing
- Alexander Wilson – Director of Sales

#### IT Group (IT)

- John Baker – Network Administrator
- Nancy Davis – Data Analyst
- Jason Smith – IT Manager
- blueteam – Security Analyst
- blackteam – IT Support
- blackteam2 – Backup IT Support

### Critical Services

If these services are down, you will lose points, until they are restored to the correct working condition.

- **SSH**

  - Only admin users may SSH into the system.
  - SSH must require **keys only**, no passwords.
  - Limit to **3 attempts** before lockout.
  - Limit total to **6 concurrent sessions**.

- **Apache2**

  - Must return **200 status code**.
  - Must serve the page with **no content errors**.

- **UFW (Firewall)**

  - Rules must align with allowed critical services.
  - Use only the standard protocols for the service


### Folder Permissions

In `/shared`, there are 3 subdirectories:

#### Board\_of\_Directors

- Owned by the **CEO** and **leadership group**.
- Full access for CEO and leadership only.
- Subdirectories owned by corresponding users (e.g., `CFO` owned by CFO).
- User has full access; others in group have read-only.
- Use underscores for multi-word names (e.g., `Director_of_Operations`).

#### IT

- Owned by **IT Manager** and **IT group**.
- Full access for owner and group.
- `network` subdir: owned by **Network Administrator** + IT group.

  * Owner: full access.
  * Others in IT group: read/write only.
  * No access for others.

#### General

- Accessible to **all system users**.
- Owned by **Network Administrator** and **general group**.


### Login Message

Upon login, the following message of the day should appear:

```
Welcome to the Veridian Solutions server!!
```

### Packages

- Ensure all packages are up to date and stay up to date.
- Install any missing **critical services**.


### Reports

You must submit a **memo-style report** addressed to the leadership group.

### The memo should include:

1. **Issues Discovered**

    - Provide a clear, high-level description of the problems identified during the assessment.
    - Avoid technical jargon—focus instead on business impact (e.g., “The company’s website was unavailable to customers,” or “A malicious file disrupted normal operations”).
    - Highlight the risks posed by the issues, such as downtime, data loss, or reputational harm.

1. **Resolution Summary**

    - Briefly explain how the issues were fixed in terms that emphasize outcomes rather than technical details.
    - For example, say “We restored the website to full functionality and ensured it returned correct responses” instead of describing exact commands or code.
    - Emphasize restored stability, security, and business continuity.

1. **Policy and Practice Recommendations**

    - Provide forward-looking suggestions on how the organization can strengthen defenses, reduce risks, and avoid similar issues in the future.
    - Recommendations might include employee training, stronger system monitoring, regular audits, or establishing clearer response procedures.
    - Frame recommendations as improvements to protect the business and its stakeholders.


### Formatting & Submission Requirements:

- Use a **memo format** (To, From, Date, Subject) at the top of the document.
- Write in **plain, non-technical language** that executives and non-technical leaders can easily understand.
- Ensure a **clear, logical flow** with polished grammar and professional tone.
- Keep the focus on **business impact, outcomes, and recommendations**—not technical processes.
- Submit the report as a **PDF only**.
- Length: **1–2 pages**, single-spaced, using **12 pt Times New Roman** font.


You must also submit a **technical report** addressed to the IT group.

### The technical report must include:

1. **Issues Discovered**

   * Provide a clear description of each technical issue found, including relevant details such as error messages, system misconfigurations, vulnerabilities, or malware symptoms.
   * Use technical terminology where appropriate so that IT staff can fully understand the scope and impact.

1. **Resolution Steps**

   * Explain, step by step, how each issue was remediated.
   * Include any commands, scripts, configuration changes, or patches that were applied.
   * If an issue could not be fully resolved, explain why and provide recommendations for future workarounds or escalations.

1. **Policy and Practice Recommendations**

   * Suggest improvements to existing IT practices that would prevent similar issues from recurring.
   * These may include changes to patch management, system monitoring, malware detection, user access controls, or incident response procedures.
   * Provide justification for each recommendation, citing best practices or security standards where possible.


### Formatting & Submission Requirements:

- Write in **technical language** that assumes the audience has IT knowledge (system administrators, security engineers, etc.).
- Organize content with **headings, bullet points, and/or numbered lists** for readability.
- Ensure a **logical flow** and maintain professional grammar and spelling.
- Submit the report as a **PDF only**.
- Length: **3+ pages**, single-spaced, using **12 pt Times New Roman** font.
- Appendices (optional): You may include additional evidence such as screenshots, log snippets, or configuration files if relevant, but the main body of the report should remain concise.


## Guidelines

- Authorized user passwords were correct at lab start but may change.
- Check your score in the **Details** tab.
- VM resets follow the reset policy (see **Rules**).
- Read VM requirements carefully—some threat hunting is expected.
- You may fix issues that are not scored. If points don’t update, wait 10 minutes, then contact a TA.
- Goal: **find and fix as many issues as possible** to maximize score.

## Grading Breakdown (700 Points Total)


| **Task**          | **Points** |
| ----------------- | ---------- |
| Defense Points    | 500        |
| Memo              | 100        |
| Technical Report  | 100        |             


### Grading Rubric – Executive Memo-Style Report (To Leadership)

| Category                              | Points | Criteria                                                                                                                                                                                                  |
| ------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Memo Format & Structure**           | 5      | Proper use of memo format with **To, From, Date, Subject**. Clear headings, logical flow, professional presentation.                                                                                      |
| **Issues Discovered**                 | 20     | High-level description of problems in **plain, non-technical language**. Emphasizes **business impact** (downtime, reputational risk, financial loss). Clearly identifies **risks posed**.                |
| **Resolution Summary**                | 20     | Clear, concise explanation of how issues were resolved **in terms of outcomes**, not technical steps. Emphasizes restored stability, continuity, and security.                                            |
| **Policy & Practice Recommendations** | 20     | Forward-looking, realistic recommendations that protect business interests. Examples: employee training, monitoring, audits, incident response. Recommendations are **actionable and clearly justified**. |
| **Clarity & Professionalism**         | 15     | Clear, logical writing suitable for executives. Polished grammar, spelling, and sentence structure. No unnecessary technical jargon.                                                                      |
| **Formatting & Presentation**         | 10     | Meets length (1–2 pages, single-spaced, 12 pt Times New Roman). Professional PDF format, headings used appropriately.                                                                                     |
| **Overall Impact & Persuasiveness**   | 10     | Report clearly communicates urgency, importance, and recommended actions. Executives can **understand and act on the information**.                                                                       |


### Grading Rubric – Technical Report (To IT Staff)

| Category                              | Points | Criteria                                                                                                                                                                                          |
| ------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Introduction & Context**            | 5      | Provides brief context of the assessment/incident. Explains purpose of report for IT audience.                                                                                                    |
| **Issues Discovered**                 | 25     | Detailed technical descriptions of all issues, including **error messages, misconfigurations, vulnerabilities, malware symptoms**. Clear explanation of scope and impact.                         |
| **Resolution Steps**                  | 25     | Step-by-step remediation details. Includes **commands, scripts, configuration changes, patches applied**. Explains partially resolved issues or workarounds.                                      |
| **Policy & Practice Recommendations** | 20     | Technical recommendations to prevent recurrence. Covers patch management, monitoring, malware detection, access controls, incident response. Justified with best practices or security standards. |
| **Clarity & Technical Accuracy**      | 10     | Logical, readable, and technically accurate. Uses appropriate terminology for IT staff. Clear headings, bullet points, numbered lists for readability.                                            |
| **Formatting & Presentation**         | 10     | Meets length (3+ pages, single-spaced, 12 pt Times New Roman). Professional PDF format. Optional appendices included properly.                                                                    |
| **Evidence & Supporting Material**    | 5      | Relevant screenshots, log snippets, or configuration files included where appropriate. Supports claims without cluttering main report.                                                            |


## Submission Instructions

* **Lab 7: Operating System Defense – Defense Points**
  *No submission is required for this portion of the lab.*
* **Lab 7: Operating System Defense – Memo**
  Submit a single PDF document.
* **Lab 7: Operating System Defense – Technical Report**
  Submit a single PDF document.
