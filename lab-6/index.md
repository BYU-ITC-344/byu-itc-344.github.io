# Lab 6: Vulnerability Scanning and Metasploitable

## Overview

Vulnerability scanning and patching are crucial for ensuring operating systems' security and stability. Vulnerability scanning helps identify security weaknesses and potential threats in the system, which attackers could exploit to gain unauthorized access or compromise sensitive data. By regularly conducting vulnerability scans, organizations can stay proactive in identifying potential threats and take measures to mitigate them before they can be exploited.

Patching involves applying updates and fixes to software applications and operating systems to address known vulnerabilities and bugs. Vendors release these patches in response to identified security issues, and failing to apply them promptly can leave systems vulnerable to attacks. Regular patching ensures that systems are running on the latest software versions with security fixes and updates, reducing the risk of exploitation.

In today's digital age, where cyber threats are prevalent and attacks are becoming increasingly sophisticated, vulnerability scanning and patching are essential security practices. Organizations that fail to implement these measures are putting their data, operations, and reputation at risk. Therefore, it is crucial to prioritize these activities and ensure they are performed regularly and effectively.

In this lab, you will practice scanning a machine for vulnerabilities and patching some of the vulnerabilities you find. The VMs that you will need for this lab will appear in your Proxmox instance as VM 1002 (OpenVAS) and 1003 (metasploitable). If you do not see these VMs please contact a TA.

## Lab Technologies

After this lab, you will have worked with:

- Kali Linux
- OpenVAS
- Metasploitable

## Instructions

### Step 1: Create a host-only network

Due to the vulnerable nature of the Metasploitable machine, it will be hosted on a host-only network so it cannot reach the internet. Creating a host-only network in Proxmox involves setting up a virtual network that allows communication between VMs and the Proxmox host but not with external networks. 

1. In the Promox interface click on your server node and go to `System` > `Network`
1. Click on `Create` and select `Linux Bridge`.
1. In the `Create: Linux Bridge` dialog, configure the bridge:
    - **Bridge name**: Set the name to `vmbr1`.
    - **Autostart**: Check this box to ensure the bridge starts automatically when Proxmox boots.
    - **Gateway**: Leave this blank for a host-only network.
    - Click `Create` to save the new bridge.
1. In the left sidebar, click on the VM you want to assign to the new network and click on the `Hardware` tab.
1. If the VM already has a network device double click on it and change the `Bridge` to `vmbr1`
1. If there is no network device, click on `Add` and select `Network Device`.
1. In the `Add: Network Device` dialog select `vmbr1` as the `Bridge`.
1. Click `Add` to save the new network device.

Make sure both the openVAS and Metasploitable VMs are now on the `vmbr1` bridge. You will have to manually set the IP addresses for each machine since there is no DHCP server. Set the IPs in the 192.168.0.0/16 range and make sure they can ping each other. 


### Step 2: Scanning Metasploitable 2

This [guide](https://www.hackingtutorials.org/scanning-tutorials/vulnerability-scanning-openvas-9-0-part-2/) will walk you through how to scan a machine and view the results. The scan will take a while so it is recommended you start it and come back to it later. 

### Step 3: Remediation

After completing the **initial vulnerability scan**, identify and select **five critical vulnerabilities** with a **CVSS score between 9.0 and 10.0**. Note that some issues may not be within your control or permission to fix. You may need to review **more than five vulnerabilities** to identify five that are **remediable**.

**Important guidelines:**

1. If a **single remediation** addresses multiple CVEs, it will **count as only one** vulnerability.
1. You **cannot** simply enable the firewall and claim the issue is resolved; the remediation must directly address the underlying vulnerability.
1. Document your remediation steps clearly, including commands, configuration changes, or updates applied.

### Step 4: Write up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- Answers to all questions
- Screenshots showing the before and after results of the OpenVAS scans


#### Templates

- <a href="lab-6-writeup-template.docx" download>Download the MS Word Write-Up Template (.docx)</a>
- <a href="lab-6-writeup-template.md" download>Download the Markdown Write-Up Template (.md)</a>

## Helpful links  

[NIST](https://nvd.nist.gov/vuln/search)

## Requirements and Points

### Grading Breakdown (100 Points Total)


| **Task**                             | **Points** |
| ------------------------------------ | ---------- |
| Metasploitable 2 has been scanned    | 20         |
| 5 critical problems have been fixed  | 40         |
| Write-Up Questions                   | 40         |             


### Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.