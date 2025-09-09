# Homework 2 - Virtualization Foundations & Security
 
## Introduction
 
Virtualization is a cornerstone of modern enterprise IT infrastructure. Hypervisors like **Proxmox VE** (a Type 1 hypervisor) allow multiple virtual machines (VMs) to run on a single physical host, but they also introduce new security risks.
 
In this assignment, you will explore Proxmox VE’s architecture and implement security practices to reduce the attack surface of virtualized environments. You will configure **datacenter-level firewalls**, **VM-level firewalls**, and **role-based access control (RBAC)**, while also reflecting on how these measures support least privilege and system hardening.
 
Through hands-on practice, you will gain experience with **firewall configuration**, **user and group permissions**, and **VM isolation**, as well as analyze how these features strengthen security in a virtualization platform.
 
## Assignment Instructions
 
### Step 1: Basic Hardening
 
Securing your Proxmox VE environment begins with protecting administrative access. By default, Proxmox allows the `root` account to log in directly to the web GUI. While this is convenient, it creates a **single point of failure**: if the root password is compromised, an attacker gains full control of your hypervisor and all VMs. Direct root login is a common attack vector (e.g., brute-force or credential stuffing). Disabling it improves both **security** and **accountability** by requiring administrators to log in with individual accounts. This does not disable the root account entirely—it only prevents direct GUI login. Administrators can still sign in with their own accounts and then switch to the root user when elevated privileges are required. This principle applies across all operating systems, not just Proxmox—it is a general security best practice to disallow direct root logins. Once you disable direct root login, you’ll need a new administrative account for day-to-day management. This ensures that actions are tied to individual users, supporting **least privilege** and **auditing**.




#### Understanding PAM vs PVE Users
 
When you create a user in Proxmox, you must choose an **authentication realm**:
 
- **PAM (Linux system user)**
   - Linked directly to the underlying Linux operating system’s `/etc/passwd` and PAM (Pluggable Authentication Modules).
   - A PAM user exists both in Proxmox **and** as a system account on the host.
   - Advantage: Can be reused for SSH and other system-level authentication.
   - Risk: If compromised, it could give both **Proxmox access** and **Linux host access**.
 
- **PVE (Proxmox internal user)**
   - Exists **only inside Proxmox** and is managed entirely through the Proxmox VE web interface.
   - Not a system-level Linux account—cannot log in via SSH.
   - Advantage: Safer for administrative separation, since access is limited to Proxmox management only.
   - Common choice for lab users, students, and Proxmox-only accounts.
 
Adding 2FA strengthens account security by requiring both a password **and** a time-based one-time code. Proxmox supports TOTP (Time-based One-Time Password) apps like **Duo Mobile**, **Google Authenticator**, or **Authy**.
 
**Best Practice:** For long-term administration, create **PVE users** for Proxmox management, and reserve **PAM users** only when you specifically need OS-level access.
 
#### Practical Steps
 
To reduce this risk, you will:
 
1. Disable the default **`root` login** over the web GUI.
   1. Navigate to **Datacenter → Permissions → Users**.
   1. Edit the user and disable the account
   1. Apply the changes
 
1. Create a new **admin user** for management.
   1.  Navigate to **Datacenter → Permissions → Users**.
   1. Click **Add → User**.
   1. Enter details for your new admin account:
      * **User name:** e.g., `admin`
      * **Realm:** Select `Proxmox VE authentication server` (recommended)
      * **Password:** Choose a strong password.
      * **Enabled:** Leave checked.
      * **Comment** Admin user account
      * Leave everything else blank
   1. Next, assign the new user administrator privileges:
      1. Navigate to **Datacenter → Permissions**.
      1. Click **Add → User Permission**.
      1. Select:
         * **Path:** `/` (applies permissions across the entire datacenter)
         * **User:** `admin` or whatever you called your admin user
         * **Role:** `Administartor`
   1. Enable Two-Factor Authentication (2FA)**
      1. In the web GUI, go to:
         **Datacenter → Permissions → Two Factor**.
      1. Click **Add → TOTP**.
      1. Select the user account you want to secure (e.g., `admin@pve`).
      1. A **QR code** will appear on the screen.
      1. On your phone:
         * Open your authenticator app (Duo Mobile, Google Authenticator, or Authy).
         * Choose **Add account → Scan QR code**.
         * Scan the QR code shown in Proxmox.
      1. The app will generate a **6-digit code**. Enter this code into the **Verify Code** field in Proxmox.
      1. Click **OK/Save** to confirm.
      1. Log out of Proxmox and then use the new admin account to log in using the password you created. It should then ask you for a TOTP code
   1. **Test the new login:**
      1. Log out of the Proxmox web GUI.
      1. Log back in using the **new admin account** and the password you created.
      1. After entering the password, Proxmox should prompt you for a **TOTP code**. Open your authenticator app and enter the current 6-digit code to complete the login.
 
#### **Screenshots to Capture Before Continuing to Step 2**
 
* **User List:** Show your newly created admin account.
* **Permissions Tab:** Show that your new user has the **Administrator** role assigned.
* **Two-Factor Authentication:** Show the TOTP setup page for your new admin account.




### Step 2: Permissions & Access Control
 
Managing permissions effectively is critical for minimizing risk and enforcing **least privilege** in Proxmox. This step introduces **user-based** and **role-based** permissions, followed by practical exercises in creating users and groups.
 
#### User-Based vs Role-Based Permissions
 
Setting up permissions by assigning privileges directly to individual users is an example of **user-based permissions** (like the admin user created in Step 1). While this works for small environments, it has limitations:
 
* **Scalability issues:** Each user must be managed separately. Adding or removing users requires updating permissions for each one.
* **Higher chance of errors:** Manual assignment increases the likelihood of mistakes or overlooked privileges.
* **Difficult auditing:** Tracking access for multiple users becomes cumbersome as the environment grows.
 
**Role-Based Access Control (RBAC)** addresses these limitations by assigning **permissions to roles** instead of individual users. Users are then assigned to one or more roles. Benefits include:
 
* **Simplified management:** Update permissions for a role once, and all assigned users inherit the change automatically.
* **Least privilege enforcement:** Roles can be designed to provide only the permissions needed for specific tasks.
* **Improved auditing and accountability:** Roles clearly define access, and it’s easy to see which users inherit which privileges.
* **Better scalability:** Efficiently manages large groups of administrators, operators, or students.
 
**Example in Proxmox:**
Instead of giving each student VM-start privileges individually, create a **“VM-Operator” role** and assign all students to that role. Any updates to the role automatically apply to all students, ensuring consistent and secure permission management.
 
#### Practical Steps
 
1. **Create Groups in Proxmox**
   1. **Steps to create a group:**
      1. Navigate to **Datacenter → Permissions → Groups**.
      1. Click **Create → Group**.
      1. Enter the **Group Name** and **Comment/Description**.
      1. Click **Add**.
      1. Repeat this for all groups in the table
                                                                       
      | **Group**     | **Purpose / Role** | **Example Permissions**                                                                             |
      | ------------- | ------------------ | --------------------------------------------------------------------------------------------------- |
      | **Admins**    | Full privileges    | Can start/stop VMs, modify firewall, manage users and groups, full datacenter access                |
      | **Operators** | Limited management | Can start/stop VMs, view logs, basic VM management, but cannot change firewall or admin settings    |
      | **General**   | Minimal access     | Can start/stop assigned VMs, view status, complete lab exercises, but cannot modify system settings |
      | **Read-only** | Auditing only      | Can view logs, monitor VM status, and check configurations, but cannot make any changes             |
 
1. **Assign Users to Groups**
   1. Create the following users (Use the same steps as before, but select a group for the user)
      | **User**                        | **Assigned Group(s)**         | **Effective Role / Permissions**                                                                           |
      | ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
      | **Alice**  | Admins                        | Full datacenter control: manage VMs, firewall, users, and groups                                           |
      | **Bob**  | Operators                     | Limited management: start/stop VMs, view logs, basic VM tasks                                              |
      | **Carol**  | General (Students)            | Minimal access: start/stop assigned VMs, view status, complete labs                                        |
      | **Dave**  | Read-only, General (Students) | Auditing + Student access: can view logs and start/stop VMs, but cannot modify firewall or system settings |
 
1. Permission Verification
   - Log in as a group member and attempt tasks to confirm that **permissions behave as expected**.
   - Examples:
      - Students should only start/stop assigned VMs.
      - Operators can manage VMs but not firewall rules.
      - Admins have full privileges.
 
**Useful Notes**
 
* Users inherit **permissions from their group’s assigned roles**, not from individual assignments.
* Changing a role automatically updates permissions for all users in that group.
* This ensures **least privilege** and simplifies administration.





### Step 3: Datacenter Firewall
 
Securing the **datacenter level** in Proxmox is critical because this is where the hypervisor itself is managed. Any compromise here could give an attacker full control over all nodes and VMs in the cluster. By configuring datacenter-wide firewall rules, you restrict who can even *reach* the management interfaces. This drastically reduces the attack surface and ensures only trusted sources can interact with Proxmox.
 
In this step, you’ll configure firewall rules so that **only your management connection** can access Proxmox services. For this example, the trusted management IPs are:
 
   - **172.16.24.2** (your admin workstation)
   - **172.16.96.2** (TA admin workstation)
 
**⚠️ WARNING:** You **must add the allow rules first** (for SSH and HTTPS from 172.16.24.2) **before enabling the datacenter firewall**. If you turn on the firewall without adding them, you will **immediately** lose access to Proxmox.
 
#### Tasks
 
**Firewall Rule Options**
 
| **Option**           | **Description**                                                                                                            | **Examples / Best Practices**                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Direction**        | Whether the rule applies to **incoming (In)** or **outgoing (Out)** traffic.                                               | Most rules should be **Inbound (In)** to protect the Proxmox host. |
| **Action**           | What happens to matching traffic: <br>• `Accept` → allow <br>• `Drop` → silently discard <br>• `Reject` → deny with error. | Use **Accept** for trusted sources, **Drop** for everything else.  |
| **Interface**        | Network interface the rule applies to (e.g., `vmbr0`). Leave blank = all interfaces.                                       | Leave blank unless targeting a specific network bridge.            |
| **Source**           | IP address or network **sending** the traffic.                                                                             | `172.16.24.2` (management workstation)                             |
| **Destination**      | IP address or network **receiving** the traffic. Blank = this Proxmox node.                                                | Leave blank for host-local rules.                                  |
| **Enable**           | Activates the rule. It can be unchecked to temporarily disable it.                                                            | Always check when ready.                                           |
| **Macro**            | Predefined shortcuts for common services (SSH, HTTPS, Ping, etc.).                                                         | Use **SSH** or **HTTPS** macros for quick setup.                   |
| **Protocol**         | Type of traffic: `TCP`, `UDP`, `ICMP`, etc.                                                                                | SSH and HTTPS = `TCP`.                                             |
| **Source Port**      | Port on the source machine. Usually left blank (dynamic).                                                                  | Leave blank in most cases.                                         |
| **Destination Port** | Port on the Proxmox host (service being accessed).                                                                         | SSH = `22`, Proxmox Web = `8006`.                                  |
| **Comment**          | Notes for documentation.                                                                                                   | *“Allow HTTPS from management workstation.”*                       |
| **Log Level**        | Level of detail to log when the rule is triggered. Useful for auditing and troubleshooting.                                    | Enable logging for Drop/Reject rules.                              |
 
1. Add the firewall rules
   1. Navigate to **Datacenter → Firewall**
   1. Click **Add** to create a rule
 
   1. **Allow SSH (port 22)**
      * Ensures only the management workstations can connect to the Proxmox node via SSH.
      * Blocks brute force or unauthorized SSH attempts from other hosts.
 
   1. **Allow HTTPS (port 8006)**
      * Restricts web GUI access to your management system.
      * Prevents attackers from scanning the network so that they cannot even see the login page.
 
   1. **Drop all other inbound traffic by default**
      * Enforces a “deny-all, allow-by-exception” security model.
      * Any traffic not explicitly allowed is automatically blocked, providing a strong baseline.
      * This should already be set
 
1. **Verify Rules with a TA**
   - Before making changes active, double-check with a TA to confirm your rules are correct. A single mistake (such as forgetting to allow HTTPS or SSH from your management IP) could lock you out of the Proxmox web interface.
 
1. **Activate the Datacenter Firewall**
   * Navigate to **Datacenter → Firewall → Options**.
   * Find the **Firewall** setting.
   * Click and switch it to **Enabled**.





### Step 4: VM-Level Firewall
 
VM-level firewalls in Proxmox allow you to **control traffic at the VM network interface**, providing isolation between VMs and reducing the attack surface inside the virtual network. Use your **Windows Server 2022** VM for the step.
 
#### Tasks
 
1. In the Proxmox web interface, select the **Windows Server VM**.
1. Go to **Firewall → Options**.
1. Set **Firewall** to **Enabled**.
1. Create Allow Rules for Management Access
 
   You want to **allow only necessary management traffic** (RDP, management services) from your `Windows 11` VM.
 
   | **Action** | **Direction** | **Protocol** | **Source**           | **Destination Port** | **Comment**               |
   | ---------- | ------------- | ------------ | -------------------- | -------------------- | ------------------------- |
   | Accept     | In            | TCP          | Windows 11 VM IP     | 3389                 | Allow RDP from management |
   | Drop       | Out           | TCP          | Windows Server VM IP | 22                   | Block Windows Server from ssh access to other devices |
 
   > **Tip:** Only open services that are required for the VM to function. In the case of a Windows server, you would also need to allow ports for AD-related services, but for now, we will just do RDP.
 
1. **From the Windows 11 VM:**
   * Test **RDP** to the Windows Server VM → **should succeed**.
   * Test **SSH** to any Linux VM → **should succeed**.
 
1. **From any other VM:**
   * Attempt **RDP** to the Windows Server VM → **should fail**.
 
1. **From the Windows Server VM:**
   * Attempt **SSH** to any Linux VM → **should fail** (blocked by VM firewall).
 
**Why This Matters**
 
* VM-level firewalls **enforce strict isolation** between VMs.
* Only required ports/services are exposed, minimizing attack vectors.
* Combined with datacenter-level firewall rules, this implements **layered security** (network + VM-level).
 
### Step 5 – Reflection
 
After completing your research and hands-on exercises, write a short 1–2 paragraph reflection addressing the following:
 
1. **Firewalls and Attack Surface:**
 
   * Discuss how **datacenter-wide firewall rules** restrict access to the hypervisor itself, limiting which IPs can connect to SSH and the web GUI.
   * Explain how **VM-level firewalls** provide an additional layer of defense, isolating VMs from each other and only allowing required services.
 
1. **User Groups and Least Privilege:**
 
   * Describe how **role-based access control (RBAC)** ensures users only have the permissions necessary for their tasks.
   * Reflect on how **groups and roles** prevent accidental or malicious changes by limiting access to critical resources.
 
## Deliverables
 
| **Step / Task**                          | **Deliverable**                                                                              | **Points** |
| ---------------------------------------- | -------------------------------------------------------------------------------------------- | ---------- |
| **Step 1: Basic Hardening**              | Screenshot(s) of Proxmox **User List** showing your new admin account                        | 2.5        |
|                                          | Screenshot(s) of **Permissions Tab** showing Administrator role assigned                     | 2.5        |
|                                          | Screenshot(s) of **Two-Factor Authentication setup** for your admin user                     | 5          |
| **Step 2: Permissions & Access Control** | Screenshot(s) of **Groups created** (Admins, Operators, General, Read-only)                  | 5          |
|                                          | Screenshot(s) of **Users assigned to groups** (Alice, Bob, Carol, Dave)                      | 5          |
|                                          | Screenshot(s) of **Permissions Tab** showing Administrator role assigned                     | 5          |
|                                          | Screenshot(s) verifying **permission behavior** for at least one user per group              | 10         |
| **Step 3: Datacenter Firewall**          | Screenshot(s) of **Firewall rules** for SSH (port 22) and HTTPS (port 8006)                  | 5          |
|                                          | Screenshot(s) of **Default drop-all rule**                                                   | 5          |
|                                          | Screenshot(s) of **Datacenter Firewall enabled**                                             | 5          |
| **Step 4: VM-Level Firewall**            | Screenshot(s) of **Windows Server VM firewall enabled**                                      | 5          |
|                                          | Screenshot(s) of **VM firewall rules** allowing RDP from Windows 11 VM                       | 5          |
|                                          | Screenshot(s) of **Testing results**: RDP succeeds from Windows 11 VM, fails from other VMs  | 10         |
|                                          | Screenshot(s) of **Testing results**: SSH blocked from Windows Server VM to Linux VMs        | 10         |
| **Step 5: Reflection**                   | 1–2 paragraph reflection addressing firewalls, attack surface, RBAC, and least privilege     | 20         |
 
### **Notes for Submission**
 
* Include **clear screenshots** showing all configurations and test results. Illegible screenshots cannot be graded.
* Write **reflections in complete sentences**, explaining your security reasoning.
* Submit your assignment in **PDF format** only.