---
title: Final Exam Study Guide
---
The final exam is designed to take approximately 45 minutes. That was also my intention for the midterm but most people completed the midterm in less than half that time. Accordingly, the final is roughly twice as long as the midterm. It has 59 questions worth a total of 80 exam points. Those exam points will be scaled to 50 points in the course.

You will have the entire class period plus the lab period to take the exam -- 1 hour 50 minutes. So there should be plenty of time if you want to take it slowly. You will take it on LearningSuite so please bring your computer (or preferred device) to class. Or, you may use a lab computer. The exam is closed-book, closed-notes, closed-internet.

You may bring one **blank** piece of scratch paper and a pen or pencil.

All questions are _selected response_. That is, multiple choice, multi-select, true/false, matching, etc. On a multiple choice question, if you think more than one answer could be correct, always select the _best_ answer.

On matching questions you get 1 point for each correct answer. Matches are not always 1:1. The same answer may match multiple prompts and there may be answers that don't match any prompt.

On multi-select questions you get 1 point for selecting each correct answer and you get -1 (negative one) point for selecting each incorrect answer. However, your overall score for a multi-select question cannot fall below 0.

You should review the pop quizzes and the midterm exam - especially questions that you got wrong. Nearly half of the questions on the final exam are variations of the ones in the quizzes and midterm. Many of the remaining questions are on the same topics.

The following study questions are to help you prepare for the exam. These are open-ended questions intended to get you to think about the subject in depth and consider what we have talked about in class. Accordingly, they are not in the same format of the exam, they have broader coverage than the exam, and they are harder than the questions on the exam. You need not compose an answer for each of these. Rather, just consider the subject matter.

For studying, use whatever resources you prefer: textbook, slide deck, web search, etc. You may pose these study questions to AI but remember that it sometimes gives wrong answers.

As this is a comprehensive exam, the first sections of this guide are the same as those from the midterm.

## Operating System Fundamentals
* What are the two basic jobs of an operating system?
* How does security impact the two basic jobs?

## Installing and Booting Operating Systems
* "Booting" an operating system involves incrementally loading larger and more capable pieces of code. Where is the first piece of code located? Where are the second and third pieces?
* What does a computer boot when _installing_ an operating system? Where does it get that code to boot?
* Once the operating system has been installed where does it typically boot from?
* What is an "ISO file"? How is it used when installing an OS on a virtual machine? How would you use an ISO file to install an OS on a physical computer?

## VMs and Containers
* What is the difference between a virtual machine and a container?
* What is the difference between a Type 1 Hypervisor and a Type 2 Hypervisor?
* What is the difference between a Virtual Machine Image, A Virtual Machine, and a Snapshot?
* What is the difference between a Dockerfile, a Docker Image, and a Docker Container?
* Why can you run an x86 architecture container on an ARM-based Mac (M1, M2, or M3 processor)?

## Cloud Computing
* What is Infrastructure as a Service (IaaS)? How would you use it?
* What is Platform as a Service (PaaS)? How would you use it?
* What is Software as a Service (SaaS)? How would you use it?
* Who are the typical buyers of each form of cloud computing?
* The alternatives to cloud computing are an On-Premise Data Center and Colocation. These predate cloud computing. When would you still choose one of them?
* What is a private cloud? Does BYU have one?

## File and Printer Sharing
* How were Local Area Networks (LANs) used before the internet? Do they still serve those functions?
* How does a computer discover printers on the network?
* There are a lot of different print and file sharing protocols. Why do you think that is?

## Access Control
* The fundamental components of access control are Users, Groups, Permissions, and Assets. How do these relate to each other?
* What is a _role_ and how does it relate to the fundamental components?
* If you have a thumb drive formatted with the typical FAT file system, can set access controls on the files it contains? Why or why not?

## Backup Planning
* What digital media can be used for backups?
* What are the advantages and disadvantages of backing up to the cloud?
* Do you suppose that cloud storage is also backed up? How might OneDrive, iCloud, Google Drive, Box.com and related services be backed up?
* What is different about backing up databases?
* What would be the main components of a backup plan?

## Modern Operating Systems
* Contemporary operating systems are all preemptive multitasking. What are the task models from earlier operating systems? If preemptive multitasking is superior, why might the other models have been chosen?
* PCs running DOS originally had a Command-Line Interface (CLI). With Windows they gained a Graphical User Interface (GUI). MacOS originally had a GUI and later gained a CLI. What are the relative advantages of a CLI and a GUI? Why do contemporary operating systems have both?
* CPUs are known by their register size: 8, 16, 32, and 64 bits. Is the address size always the same as the register size? Why might it be bigger or smaller?

## File Systems
* What are directories and subdirectories? What is the root directory?
* What is a file path? What characters are used as delimiters in file paths?
* What are the differences between FAT, NTFS, and MacOS File Systems?
* What are hard links and soft links? What are the advantages and disadvantages of each?

## Securing Access
* What are the three primary ways of authenticating a person?
* What is multi-factor authentication?
* How does encrypting file systems and communication channels protect data?
* Why is data not encrypted in main memory?

## Firewalls and Anti-Malware
* What is a host firewall and how does it differ from a network firewall?
* What is signature-based malware detection?
* What is anomaly-based malware detection?

## Security Policy
* What are the different components to a security policy?
* What is the effect of each component?

## CPU and Memory
* What is the difference between a RISC and a CISC architecture?
* What is pipelining in a CPU context?
* What are the major components of a CPU? (Control unit (CU), Arithmetic Logic Unit (ALU), Memory Controller, Cache Memory)
* What are the three layers of cache on a CPU? What characteristics distinguish each?
    * Is the layer dedicated to a single core or shared?
    * Does the layer have separate caches for data and code?
    * How fast is the layer?
    * How big is the layer?
    * (You will not need to know the actual sizes or speeds. Just relative values; which layers are bigger and which are faster.)
* What is the difference between kernel memory and user memory?
    Where does a process have its code, data, heap and stack? (In user memory)
    Where does the operating system have its code, data, heap and stack? (In kernel memory)

## Process Scheduling
* What is a process and what is a thread?
* Do threads in the same process share memory?
* What is proprietary to a thread? (register values and stack)
* What is proprietary to a process? (user memory)
* How is CPU capacity divided among processes and threads?

## Storage Devices
* What are the basic storage technologies? (Magnetic, Optical, and Flash)
* How magnetic storage store data? (As magnetized regions on a medium.)
* How does optical storage store data? (As reflective and opaque regions on a disc.)
* How does flash storage store data? (As electrical charges on a chip.)
* What are the commonly used RAID levels and what are their characteristics?
    * Commonly-used are RAID-0, RAID-1, RAID-5, and RAID-6

## Network Fundamentals
* What are the seven layers in the OSI network model and how do they map to the five layers in actual Internet protocols?
* What are the three common network addresses and how are they used? (IPv4, IPv6, and MAC)
* Be prepared to recognize the notation used for each of the three address types.
