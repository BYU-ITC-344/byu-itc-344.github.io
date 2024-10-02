---
title: Final Project
---

The final project is worth 250 points overall which accounts for nearly 25% of your grade:
* Ungraded: Team Formation
* 100 Points: A working project
* 90 Points: Final presentation
* 50 Points: Documentation
* 10 Points: Peer evaluation

You will form teams of 3 or 4 people. For the "team formation" assignment (which is not graded) you will report who is on your team. You may also notify us and be assigned to an instructor-assembled team. The documentation and working project only need to be submitted by one person in your team. The in-class presentation will be graded by the professor and the peer evaluations will have to be submitted by each student.

### Documentation
Throughout your project, you should document your progress and the steps you took along the way. Any problems or errors encountered should also be included. If someone else were to read your documentation they should be able to recreate your project.

### A Working Project
By the end, you should have a functioning project that is ready to be used.

### Final Presentation
During the last week of classes, your group will present your project, explaining what you have done and demonstrating any deliverables of the product that you have created.

### Peer Evaluation
At the conclusion of your project, you will fill out an evaluation of each team member's performance during the project. The composite score from yourself and your teammates will make up your grade for this section.

## Project Options
Choose one of the following projects. Each of these is intentionally challenging and will require you to look up information online. You may also seek insight from experts who have done this sort of thing before. While getting direction from experts is a good idea, all work must be done by members of your team. For most projects you will build upon existing source or tools. In your documentation, be sure to indicate what external tools and resources you used.

#### Create Your Own Linux Distro
There are some great resources for creating your own Linux distro from scratch using source code. A good starting point is [Linux From Scratch](https://www.linuxfromscratch.org/). You will need to create a functioning distro and justify the design decisions you made during the process. Think of a specific use case or task that you want this operating system to do and design it with that goal in mind.

#### Create a Kubernetes Cluster
Kubernetes is an open-source container-orchestration tool that helps to manage a cluster of containers. You'll need at least 3 different computers set up with containers running on all of them. You can test the load-balancing by creating fake traffic and test failover by shutting down one of the computers to see how it manages the reduced resources. Your three+ computers may be physical or virtual machines.

#### Modify an Operating System to Contain Needed Tools
Choose a base operating system and configure the settings and add useful tools for a specific purpose. Then compile it into an iso file that can be installed on a computer or VM. For example, you may build an image for forensics tools, malware analysis, threat hunting, defensive security, network monitoring, etc. Make sure that it is a significant time commitment. In your documentation include the required system resources installation instructions.

#### Resource Monitoring Dashboard for Data Center Infrastructure
Create a web-based Resource Monitoring Dashboard with user authentication, real-time data visualization, and alerting capabilities. Live server and resource data may be obtained using  using [SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol), [IPMI](https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface), [DRAC/iDRAC](https://en.wikipedia.org/wiki/Dell_DRAC), [UPNP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play), and/or related protocols. The dashboard may be comprehensive, monitoring a variety of device types (servers, routers, switches, etc.); or it may be specialized. Examples of specialized monitors are monitoring VMs in a Proxmox instance, or monitoring a set of Dell servers using their proprietary iDRAC protocol. The monitor should offer should offer live views of infrastructure data such as network traffic, server load, storage hardware health, power, and temperature data. Users should be able to observe resource status in real time and receive notifications for critical events. Specialized monitors should offer the ability to perform operations such as provisioning VMs in the case of Proxmox.

#### Process Scheduling Simulator
Build a process scheduling simulator that models the behavior of various scheduling algorithms such as Round Robin, Priority Scheduling, and Shortest Job First. Include visualizations of process execution. Analyze the performance of each algorithm under different load conditions.

#### Create a New Lab for IT&C 344
Create a new lab of similar difficulty to the labs you have been assigned in this class. The subject of the lab must be pre-approved by your instructor. In future classes we hope to incorporate systems-level programming assignments written in C so that type of lab is preferred. Below are some ideas. A good lab will mix more than one of these concepts.

* Use fork and exec to launch one or more child processes.
* Execute a pipeline of CLI applications with the stdout of each app redirected to the stdin of its successor.
* Read and write binary or textual data to files.
* Demonstrate a race condition and show how to prevent it using synchronization tools such as file locks or mutexes.
* Build a CLI tool that does something useful when incorporated into a Bash pipeline. You can draw inspiration from simple CLI tools like `grep`, `sed`, `sort`. `head`. `tail`, `uniq`, `wc`, and `nl`. Also see [this article](https://www.geeksforgeeks.org/filters-in-linux).

#### Other
Other projects must be approved by the professor. They should be related to operating systems and have similar scale and difficulty to the ones listed above.
