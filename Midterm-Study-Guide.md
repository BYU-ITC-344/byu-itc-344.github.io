---
title: Midterm Study Guide
---
The midterm exam is designed to take approximately 45 minutes. You will have the entire class period plus the lab period to take the exam -- 1 hour 50 minutes. So there should be plenty of time if you want to take it slowly. You will take it on LearningSuite so please bring your computer (or preferred device) to class. The exam is closed-book, closed-notes, closed-internet.

All questions are _selected response_. That is, multiple choice, multi-select, true/false, matching, etc. On a multiple choice question, if you think more than one answer could be correct, always select the _best_ answer.

On matching questions you get 1 point for each correct answer. Matches are not always 1:1. The same answer may match multiple prompts and there may be answers that don't match any prompt.

On multi-select questions you get 1 point for selecting each correct answer and you get -1 (negative one) point for selecting each incorrect answer. However, your overall score for multi-select cannot fall below 0.

You should review the pop quizzes - especially questions that you got wrong. Variations of a few questions from the quizzes may appear on the exam.

The following study questions are to help you prepare for the exam. These are open-ended questions intended to get you to think about the subject in depth and consider what we have talked about in class. Accordingly, they are not in the same format of the exam, they have broader coverage than the exam, and they are harder than the questions on the exam. You need not compose an answer for each of these. Rather, just consider the subject matter.

For studying, use whatever resources you prefer: textbook, slide deck, web search, etc. You may pose these study questions to AI but remember that it sometimes gives wrong answers.

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
* How were Local Area Networks (LANs) used before the internet? Do they still serve that function?
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