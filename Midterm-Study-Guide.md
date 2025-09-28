---
title: Midterm Study Guide
---
The midterm exam is designed to take approximately 45 minutes. You will have the entire class period plus the lab period to take the exam -- 1 hour 50 minutes. So there should be plenty of time if you want to take it slowly. You will take it on Paper so please bring your Pen/Pencil to class. The exam is closed-book, closed-notes, closed-internet.

All questions are multiple choice, multi-select, true/false, matching, or short response. On a multiple choice question, if you think more than one answer could be correct, always select the _best_ answer.

You should review the pop quizzes - especially questions that you got wrong. Variations of a few questions from the quizzes may appear on the exam.

The following study questions are to help you prepare for the exam. These are open-ended questions intended to get you to think about the subject in depth and consider what we have talked about in class. Accordingly, they are not in the same format of the exam, they have broader coverage than the exam, and they are harder than the questions on the exam. You need not compose an answer for each of these. Rather, just consider the subject matter.

For studying, use whatever resources you prefer: textbook, slide deck, web search, etc. You may pose these study questions to AI but remember that it sometimes gives wrong answers.


## Operating System Fundamentals

* What are the two basic jobs of an operating system?
* How does security impact these two jobs?
* What is the difference between a monolithic kernel and a microkernel?
* What are cooperative multitasking, preemptive multitasking, and single-tasking?
* What risks are associated with rolling release operating systems?
* What best practices mitigate risks when using rolling release OS in enterprise environments?
* What is the role of device drivers in an operating system?

## Installing and Booting Operating Systems

* Where is the first piece of boot code located? Where are the second and third pieces?
* What does a computer boot from when installing an operating system, and where does that code come from?
* Once an OS is installed, where does it typically boot from?
* What is an ISO file? How is it used when installing on a virtual machine? How is it used on a physical computer?
* What is the difference between minimum and recommended hardware requirements?
* What tasks should be performed before installing an OS?
* What are examples of media a system may boot from when installing an OS?


## Virtualization and Containers

* What is the difference between a virtual machine and a container?
* What is the difference between a Type 1 hypervisor and a Type 2 hypervisor?
* What is the difference between a VM image, a VM, and a snapshot?
* What is the difference between a Dockerfile, a Docker image, and a Docker container?
* What is the difference between privileged and unprivileged containers?
* How do Type 1 hypervisors, Type 2 hypervisors, Docker, and LXC containers achieve isolation?
* What is resource overcommitment in a hypervisor? What risks does it create?
* What is the tradeoff between performance and flexibility in virtualized network devices?
* What technical challenges arise when running a hypervisor inside another hypervisor (“VMception”)?
* How can CPU virtualization be achieved when the guest architecture differs from the host CPU architecture?

## Cloud Computing

* What is Infrastructure as a Service (IaaS)? How would you use it?
* What is Platform as a Service (PaaS)? How would you use it?
* What is Software as a Service (SaaS)? How would you use it?
* Who are the typical buyers of each form of cloud computing?
* What is the difference between cloud computing and alternatives such as on-premise or colocation?
* What is a private cloud?


## File and Printer Sharing

* How were Local Area Networks (LANs) used before the internet? Do they still serve those functions today?
* How does a computer discover printers on a network?

## Access Control

* What are the four fundamental components of access control: users, groups, permissions, and assets? How do they relate to each other?
* What is a role, and how does it relate to users, groups, and permissions?
* In Linux or Windows, must every user belong to a group?
* Can you set access controls on a FAT/FAT32-formatted thumb drive? Why or why not?

## Backup Planning

* What types of digital media can be used for backups?
* What are the advantages and disadvantages of backing up to the cloud?
* Are cloud storage services such as OneDrive, iCloud, or Google Drive also backed up? How?
* What is different about backing up databases compared to files?
* What are the main components of a backup plan?


## Modern Operating Systems

* What task models came before preemptive multitasking? Why might those models have been chosen?
* What are the advantages of a CLI compared to a GUI? What are the advantages of a GUI compared to a CLI? Why do modern OS include both?
* What does it mean when CPUs are described by their register size (8, 16, 32, 64 bits)?
* Is the CPU register size always the same as the address size? Why might they differ?
* What is the difference between user mode and privileged mode in a CPU?
* What are the difference in the hardware requirements between windows 7 and 11?
* How do interrupts influence the interaction between input devices and CPU processing?