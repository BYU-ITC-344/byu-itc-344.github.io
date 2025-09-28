# IT&C 344 Midterm Practice

### Questions

#### True/False 

1. An operating system provides hardware abstraction, allowing applications to run without needing to manage device details directly.

1. A microkernel contains only the essential services needed for core OS functions, while additional services run in user space.

1. One of the primary enterprise risks of rolling release distributions is that frequent, untested patches may introduce instability or downtime in production environments.

1. In distributed computing clusters, adopting a rolling release model reduces operational risk since all nodes always remain on the latest patch level.
   
1. Enterprise deployments often plan hardware closer to the recommended or maximum requirements rather than the bare minimum.

1. Containers require a separate guest operating system for each application they run.

1. Containers and virtual machines can be used together, for example by running Docker inside a VM on a hypervisor.

1. A **group** is a named set of users that can share permissions collectively.

1. In Windows, a user may only belong to one group at a time.
  
1. By default in Windows, files and directories inherit the permissions of their parent directory.


#### Matching

**Instructions:** Match the OS concept (Column A) with the correct definition (Column B).

**Column A – Terms**
- A. Hardware Abstraction
- B. Cooperative Multitasking
- C. Preemptive Multitasking
- D. File System
- E. Device Driver
- F. Kernel
- G. Monolithic Kernel
- H. Microkernel
- I. Client OS
- J. Server OS

**Column B – Definitions**

1. A method where processes voluntarily yield CPU time to others.
2. OS core that manages hardware and fundamental services.
3. Simplifies programming by hiding hardware complexity from applications.
4. The part of the OS that communicates directly with hardware components.
5. Architecture where the majority of OS services run in kernel space for performance.
6. Storage system that defines how files are stored, retrieved, and organizeD.
7. OS optimized for running end-user applications and interacting with local devices.
8. OS designed for scalability, concurrency, and handling network-based client requests.
9. A multitasking approach where the OS forcibly switches between processes.
10. Kernel architecture where only minimal services (e.g., scheduling, IPC) run in kernel space, with others in user space.

#### Multiple Choice

1. A user, Tim, is sitting at a Windows 10 computer running an application when he sees a message that another user is trying to access the computer remotely using RDP. The other user cannot access the computer until Tim signs out of Windows. What type of OS is the computer most likely running?
    
    - A. 	single-user
    - B. 	single-tasking
    - C. 	multiuser
    - D. 	server


1. On a preemptive multitasking system, what event can occur to preempt a running process and allow a new process to get control of the CPU?
 	
   - A. 	time slice expiration
 	- B. 	an infinite loop
 	- C. 	a lower priority process requires the CPU
 	- D. 	a memory error


1. Which of the following is true about the Linux OS?

 	- A. 	It is a proprietary OS, developed by Novell.
 	- B. 	It is at the heart of many embedded and real-time systems.
 	- C. 	There is no GUI option for any of the distributions.
 	- D. 	The command line interface is called PowerShell.

1. Which of the following is a difference between installing an OS on a virtual machine versus a physical computer?

 	- A. 	You do not require a license to install Windows on a virtual machine.
 	- B. 	On a physical computer, you don't need to be concerned about device drivers.
 	- C. 	On a virtual machine, you must install the same OS that is running on the host computer.
 	- D. 	You must choose the type of network connection on a virtual machine.


1. Which of the following is NOT a task in preparation for installing an OS?

 	- A. 	Make sure the computer meets hardware requirements.
 	- B. 	Ensure the hardware is working correctly.
 	- C. 	Be aware of the computer's storage configuration.
 	- D. 	Perform a low-level format on the installation disk.


1. Which of the following best describes a VM snapshot?

   - A. A complete standalone copy of the VM, including OS and data.
   - B. A point-in-time capture that saves changes (delta disk), memory state, and metadata.
   - C. A compressed image used only to deploy new VMs.
   - D. A bootloader stored in ROM that starts the OS.

1. Which of the following is a key difference between privileged and unprivileged LXC containers?

   - A. Privileged containers map root inside the container to root on the host.
   - B. Unprivileged containers do not support networking.
   - D. Privileged containers run slower due to UID translation.
   - D. Unprivileged containers require a hypervisor to run.


1. Which virtualization technology provides the strongest isolation?

   - A. Docker containers
   - B. LXC containers
   - C. Type 1 Hypervisor
   - D. Type 2 Hypervisor

1. What is the risk of CPU and memory overcommitment in a hypervisor?

   - A. Reduced kernel security and namespace conflicts.
   - B. Host swapping, performance degradation, and possible VM crashes.
   - C. Preventing snapshots and rollbacks from working.
   - D. Increased power consumption only.


1. Which of the following describes how Docker achieves isolation?

   - A. By running each container on its own hypervisor.
   - B. By using kernel namespaces and control groups (cgroups).
   - C. By requiring a full guest OS for each container.
   - D. By using BIOS-level hardware partitioning.
   

#### Short Answer

1. In the Input-Processing-Output (IPO) model, how do interrupts influence the interaction between input devices and processing?

1. Discuss the tradeoff between performance and flexibility in virtualized network devices. Provide an example scenario where performance is prioritized, and another where flexibility is preferred.

1. What technical challenges arise when running a hypervisor inside another hypervisor (“VMception”), and how can these challenges be mitigated?

1. How can CPU virtualization be achieved when the guest architecture differs from the host CPU architecture?

