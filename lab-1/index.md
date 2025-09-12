---
title: Lab 1 - Hypervisors & Operating Systems
---
# Lab 1 - Hypervisors & Operating Systems

## Introduction

Welcome to the first lab of IT&C 344!

Labs are designed to take several hours to complete, and as such, they should not be left to the last minute to do. You should expect to work on each lab for 10-15 hours (5-6+ hours a week). Procrastinate these labs at your own risk!

The labs outline your objectives and give some instructions on how to proceed. However, most of the how-todo will come from your research and diligence. You must practice your research and problem-solving skills as you would when working in IT and Cybersecurity. The labs are designed to be a beneficial learning experience, but if you cannot find a solution after working on the problem by yourself for a significant amount of time and putting in genuine effort, the TAs are there to assist you.


### Virtual Machines

A **virtual machine (VM)** is like a computer inside your computer. It runs its own operating system and applications, just like a real computer, but it does so using software that mimics physical hardware. This includes virtual CPU, memory (RAM), storage, and network interfaces.

Virtual machines run on top of a **hypervisor**, which is a program that manages the virtual environment and connects the VM to the actual physical hardware of your computer. Because a VM includes a full operating system and virtual hardware, it usually takes up more system resources and can be slower to start compared to other methods of virtualization.

### Containers

A **container** is another way to run applications in a virtualized environment, but it works differently from a VM. Instead of emulating an entire computer, a container shares the host computer’s operating system while keeping applications isolated from each other.

This makes containers much **lighter and faster** than VMs. They start quickly, use fewer system resources, and multiple containers can run on the same host without interfering with each other. Containers are ideal for running individual applications or services rather than full operating systems.

### Hypervisors

A **hypervisor** is the software that makes virtual machines possible. It sits between the physical hardware of your computer and the virtual machines, managing how resources like CPU, memory, and storage are shared.

Hypervisors allow multiple operating systems to run on the same physical computer at the same time, each in its own isolated virtual environment.

There are two main types of hypervisors:

1. **Type 1 (Bare-metal or native hypervisors)**

   * Run directly on the physical hardware, without needing an existing operating system.
   * They are faster and more secure, which is why they are often used in data centers and servers.
   * Examples: VMware ESXi, Microsoft Hyper-V, Citrix XenServer and Proxmox.

1. **Type 2 (Hosted hypervisors)**

   * Run on top of an existing operating system, like Windows or Linux.
   * Easier to set up for desktops or laptops but slightly slower than Type 1.
   * Examples: Oracle VirtualBox, VMware Workstation.


### Lab Note

In this lab, you will be working with a **Type 1 hypervisor** and virtual machines. Most of the labs build on each other, so **do not delete your previous work** and try to stay up to date. You will be informed when an operating system is no longer needed.


## Lab Technologies

By the end of this lab, you will have **installed or worked with** the following technologies:

### Hypervisor

- **Proxmox* – A Type 1 hypervisor and virtualization management platform used in this lab and all future labs.

### Operating Systems

You will have experience working with a variety of operating systems, including:


| **Category**   | **Technology / OS**          | **Notes**                                           |
| -------------- | ---------------------------- | --------------------------------------------------- |
| **Hypervisor** | Type 1 Hypervisor            | Runs virtual machines directly on physical hardware |
|                | Proxmox VE                   | Type 1 hypervisor and virtualization platform       |
| **Windows OS** | Windows 7                    | Older desktop version                               |
|                | Windows 11 Pro               | Latest desktop version                              |
|                | Windows Server 2022 (GUI)    | Server version with graphical interface             |
| **Linux OS**   | Ubuntu Desktop 22.04,23.04 or 24.04 | Desktop Linux for general use                       |
|                | Ubuntu Server 22.04          | Server-focused Linux                                |
|                | Arch Linux                   | Lightweight, customizable Linux                     |


## Instructions

Congratulations! You have just been hired as a **Cybersecurity Intern specializing in operating system management**.

Your first assignment is to set up a **virtualized environment** for play-testing common operating systems. Jim (your supervisor) has already prepared a **Proxmox machine (Type 1 hypervisor)** for you to use.

Your task is to **create and deploy virtual machines (VMs)** of the operating systems listed in the lab technologies section.


### Step 1: Hypervisor Login via VPN

You should have received **VPN credentials** via your BYU email to access the network containing your Proxmox instance. These credentials are provided in an **OVPN file**.

Follow these steps to connect:

#### Installing OpenVPN

1. **Download the OpenVPN Client**
   - Go to <a href="https://openvpn.net/client/" target="_blank">https://openvpn.net/client/</a> and download the **OpenVPN Connect** version.

1. **Install the Client**
   - Run the installer and follow the prompts. Allow any permissions requested.

1. **Import the OVPN File**
   - Open the OpenVPN client.
   - Drag and drop the `.ovpn` file from Learning Suite (`Content > Getting Started > VPN`) onto the application **or** click the **plus (+) button** at the bottom right, select **Upload File**, then browse to your `.ovpn` file and select it.

1. **Connect to the VPN**
    - Once the file is imported, click the **radio button** next to the profile to connect.


#### Logging in to Proxmox

1. **Open the Proxmox Web Interface**

   * Visit the Proxmox URL provided in the email.
   * Enter the **username** and **password** from the email.
   * Set the **Realm** to: `Proxmox VE authentication server`.
   * Click **Login**.

2. **Handle the Subscription Pop-up**

   * You may see a message saying:

   ```
   No valid subscription
   ```

   * This is normal; we are using the **free license**.
   * Click **OK** to continue.



### Step 2: Virtual Machines to Install on Proxmox


You will need to create the following virtual machines (VMs) on Proxmox:

| **OS**                        | **Notes**                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 7                     | Create a local user account.                                                                                                                        |                                                                |
| Windows 11 Pro                    | Download the ISO from the official Microsoft website; create a local user account. Hint: You can install Windows 11 Pro without an internet connection. |
| Windows Server 2022 (GUI)     | Create a local administrator account.                                                                                                               |
| Ubuntu Desktop 22.04,23.04 or 24.04 | Download the ISO from the official Ubuntu website.                                                                                                  |
| Ubuntu Server 22.04           | ISO will be provided.                                                                                                                               |
| Arch Linux                    | Download the ISO from the official Arch Linux website.                                                                                              |

### ISO Files

* An **ISO file** is a binary image of a CD, DVD, or Blu-ray disc.
* It can be used as installation media for a VM, appearing to the VM as a physical drive.
* For real computers, an ISO can be burned to a disc or copied to a USB drive.
* **Tip:** Always download ISO files from official sources to ensure safety and authenticity.

**Important:** When uploading ISOs to Proxmox:

* Use the **“Download from URL”** option whenever possible. It will be much faster than trying to upload them from your computer over the VPN.
* Make sure to store the ISOs in the **Labs** storage, **not the LVM or ISOs**.
* If the LVM fills up, the Proxmox instance will crash.

### Network Configuration

You will be provided with a range of IP addresses for your VMs. **Each VM must have a static IP** to access the network. Use the following network settings:

* **Subnet mask:** 255.255.248.0
* **Default gateway:** 172.16.24.1
* **DNS server:** 172.16.24.1

### Resource Management

* Do **not** run all VMs simultaneously; your machine likely does not have enough resources.
* Allocate sufficient CPU, RAM, and storage to each VM to ensure smooth operation.

### Screenshots for Documentation

For each VM, take screenshots of:

1. **Operating system information**
    - **Windows:** Open **System Info**.
    - **Ubuntu Server / Linux:** Run `lsb_release -a`.

1. **IP address**
    - **Windows:** Open a PowerShell terminal and run `ipconfig`.
    - **Ubuntu / Linux:** Run `ip a`.

1. **Internet Test**
    - Run `ping google.com`
    - Verify that you receive reply responses (not timeouts or errors)

These screenshots will serve as evidence that the VM was successfully installed and networked correctly.

### Step 3 – Write Up

You must complete a **write-up** of your work using the provided template. The write-up should include:

- **Answers to all questions**
- **Screenshots for each of the following showing the OS and network information as well as a connectivity test:**
   1. Windows 7                                            
   1. Windows 11 Pro                     
   1. Windows Server 2022 (GUI version)
   1. Ubuntu Desktop 22.04,23.04 or 24.04            
   1. Ubuntu Server 22.04             
   1. Arch Linux                                          

#### Templates

- <a href="lab-1-writeup-template.docx" download>Download the MS Word Write-Up Template (.docx)</a>
- <a href="lab-1-writeup-template.md" download>Download the Markdown Write-Up Template (.md)</a>


### Requirements and Points

| **Task**                                                             | **Points** |
| -------------------------------------------------------------------- | ---------- |
| Installed a working VM running **Windows 7**                         | 10         |
| Installed a working VM running **Windows 11**                        | 10         |
| Installed a working VM running **Windows Server 2022 (GUI version)** | 10         |
| Installed a working VM running **Ubuntu Desktop 22.04,23.04 or 24.04**              | 10         |
| Installed a working VM running **Ubuntu Server 22.04**               | 10         |
| Installed a working VM running **Arch Linux**                        | 20         |
| Completed the **Write-Up**                                           | 30         |


## Submission
Create a single PDF from the given `Write Up` file that contains your written report and screenshots showing that each requirement has been met. Upload the PDF to Learning Suite. Any other file format will not be accepted.

There are many ways to convert from MarkDown to PDF including some online tools. Among the most convenient is the <a href="https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf" target="_blank">yzane Markdown PDF Add-In for VS Code</a>
.
