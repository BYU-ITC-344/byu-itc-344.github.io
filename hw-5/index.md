# Homework 5 - Active Directory & Subsystem Security

## Learning Outcomes

By completing this assignment, you will:

* Understand **OS subsystems** (scheduling, memory management, services) and how user privileges map to them.
* Apply the **principle of least privilege** to restrict access in a Windows Server environment.
* Gain hands-on experience deploying and managing **Active Directory Domain Services (AD DS)**.
* Configure **domain policies** (authentication, password, and lockout policies) through Group Policy Objects (GPOs).
* Integrate **cross-platform systems** (Windows 11 + Linux) into Active Directory for centralized management.

## Assignment Overview

This assignment has two major parts:

1. **Windows Server Privilege & Subsystem Control**
1. **Active Directory Deployment and Domain Join (Windows & Linux)**

You will work with a **Windows Server 2022 domain controller**, **one Windows 11 client**, **one Windows 7 client**, and **one Linux client**. Deliverables include **screenshots** of configuration steps and a **memo** explaining your subsystem privilege enforcement and AD security policies. Please read over all the instructions and ensure you know what screenshots you need before beginning. A list of all the deliverables can be found in the deliverables section.

## Assignment Instructions

After each step, take a snapshot of your machines in case you need to revert.

If Proxmox shows

> **The current guest configuration does not support taking new snapshots**

make sure the VM disks use the **qcow2** format.

* In the VM’s **Hardware** tab, select **Disk Action > Move Storage**.
* Set **Labs** as the target storage and choose **qcow2** as the format.

For Windows VMs that require a TPM chip:

* Shut down the VM.
* Remove the existing TPM device (if any).
* Go to **Add > TPM State** and add a new TPM chip.
* Save the TPM state to **local-lvm**, not **Labs**.

### Step 1: Active Directory Deployment & Domain Join

1. **Install Active Directory Domain Services (AD DS)**

   * Promote your Windows Server 2022 system to a **Domain Controller (DC)**.
   * Document the setup process with **screenshots** of role installation and domain creation.
   * You can use [this](https://infrasos.com/how-to-setup-active-directory-on-windows-server-2022/) guide to help get your Active Directory set up
   * Set your root domain name to your `netid.itc344`. So if your net id is `friedchicken1`. your root domain name would be `friedchicken1.itc344`

  > Note: You will need to turn off the firewall you created in Homework 2 for the Windows server VM to allow the necessary traffic in to be able to join the domain. You could also create more firewall rules to allow the traffic in. Either option works

1. **Join a Windows 11 Client to the Domain**

  * Configure your Windows 11 VM to join your new domain.
  * Verify domain membership by logging in with a **domain user account**.
  * Provide **screenshots** of successful domain join and user login.

1. **Join a Windows 7 Client to the Domain**

  * Configure your Windows 7 VM to join your new domain.
  * Verify domain membership by logging in with a **domain user account**.
  * Provide **screenshots** of successful domain join and user login.

1. **Join a Linux Client to Active Directory**

  * Use a Linux machine (You can use either Linux VM).
  * Install and configure the necessary packages (e.g., **realmd, sssd, adcli, krb5-user**).
  * Join the Linux device to the AD domain:
  * Provide **screenshots** of successful AD integration.

### Step 2: User Creation & Management

1. **User Creation & Privilege Levels**

On your Windows Server Active Directory domain, create **four domain user accounts**, each assigned to a group with different privilege levels. This will allow you to test and document the differences in permissions between low, medium, and high-privileged accounts.

### **User Accounts**

1. **Domain User**

    * **Full Name:** John Doe
    * **Username:** `jdoe`
    * **Group(s):** *Domain Users*
    * **Description:** Basic level access for all domain users.

    **Group permissions (Domain Users):**

      * Default group for all users in AD.
      * Can log on to domain-joined machines.
      * Access shared resources where `Domain Users` has been explicitly granted rights.
      * Change their own password.
      * No administrative rights on domain controllers, servers, or workstations (unless explicitly added elsewhere).

1. **Domain User**

      * **Full Name:** Jane Smith
      * **Username:** `jsmith`
      * **Group(s):** *Domain Users*
      * **Description:** Basic level access for all domain users.

      **Group permissions (Domain Users):**

        * Same as above → standard user rights only.

1. **DNS Admin**

    * **Full Name:** Jane Smith Admin
    * **Username:** `jsmith-admin`
    * **Group(s):** *DNS Admin*
    * **Description:** Elevated privileges to manage DNS records.

    **Group permissions (DNS Admins):**

      * Can create, modify, and delete DNS zones and records in Active Directory–integrated DNS.
      * Can manage DNS server settings (forwarders, scavenging, logging).
      * Potentially powerful because DNS control can enable redirection of domain traffic (security sensitive).
      * No automatic admin rights on domain controllers or member servers beyond DNS service.

1. **Domain Admin**

    * **Full Name:** John Doe Admin
    * **Username:** `jdoe-admin`
    * **Group(s):** *Domain Admins*
    * **Description:** Full administrative rights across the entire domain.

    **Group permissions (Domain Admins):**

      * Automatically a member of the **local Administrators group** on every domain-joined workstation and server.
      * Full administrative rights on all domain controllers.
      * Can create, delete, and manage any AD object (users, groups, computers, OUs).
      * Can link/edit Group Policies across the domain.
      * Can modify domain-wide configurations (FSMO roles, replication, trusts).
      * Highest level of privilege in the domain (except *Enterprise Admins* in multi-domain forests).

**Best practice reminder**:

* Keep `Domain Admins` membership very limited.
* Use separate “-admin” accounts for elevated rights (as you’ve done).
* Consider scoped admin groups (e.g., *Server Admins*, *Workstation Admins*) if you don’t want every admin to be a `Domain Admin`.

### Step 3: Group Policies

**Objective:** Enforce secure authentication practices for all domain-joined computers by requiring domain login and disabling insecure legacy authentication methods.

### Steps to create and configure the policy:

1. **Create a new Group Policy Object (GPO):**

   * Open **Group Policy Management**.
   * Right-click your domain name in the left-hand pane.
   * Select **“Create a GPO in this domain, and Link it here…”**.
   * Name it: `Domain Authentication Policy`.

1. **Link and enforce the policy:**

   * After creating the GPO, right-click it and ensure both **Enforced** and **Link Enabled** are checked.
   * Select **Edit…** to configure the policy settings.

### Authentication Policy (Require Domain Login)

**Configure security settings:**

  * Navigate to:

    ```
    Computer Configuration → Policies → Windows Settings → Security Settings → Local Policies → Security Options
    ```

  * **Enable:**
    **"Accounts: Limit local account use of blank passwords to console logon only"**

    * **Explanation:** Prevents local accounts without passwords from logging in over the network.
    * **Why we use it:** Accounts with blank passwords are a major security risk. Enabling this ensures that blank-password accounts can only log in at the physical console, reducing the chance of unauthorized remote access.

  * **Set:**
    **"Network security: LAN Manager authentication level" → Send NTLMv2 response only. Refuse LM & NTLM**

    * **Explanation:** Forces network authentication to use the modern, secure NTLMv2 protocol while refusing weaker LM and NTLM protocols.
    * **Why we use it:** LM and NTLM are vulnerable to password-cracking attacks. Using NTLMv2 only strengthens network security and prevents legacy protocol attacks.
    * **Impact on legacy systems:**

      * Older systems such as Windows XP, or legacy applications that only support LM or NTLM will **fail to authenticate**.
      * These systems must be upgraded or reconfigured to support NTLMv2, otherwise they cannot access domain resources.

### Result

All domain-joined machines will enforce secure authentication by:

* Preventing network logons with blank local passwords.
* Refusing insecure legacy authentication protocols over the network.
* Requiring legacy systems to upgrade or be reconfigured to support modern protocols.

This policy is part of a **defense-in-depth strategy** to protect the domain from unauthorized access. By disabling blank-password network logons and enforcing NTLMv2, we reduce the risk of password-based attacks and lateral movement within the network. Legacy systems that cannot comply represent a security gap and must be upgraded or isolated. However, if there are legacy systems on the network that are still in use, they will no longer be able to authenticate, which could cause issues if the legacy system is using a **service account, application, or automated process that relies on LM or NTLM authentication**.

* Examples include:

  * Older file servers or NAS devices that only support NTLMv1
  * Legacy applications connecting to SQL Server or other domain resources
  * Scheduled tasks or scripts using stored credentials with outdated protocols

**Mitigation strategies:**

1. Upgrade the legacy system or application to support NTLMv2.
2. Isolate legacy systems on a separate network segment and apply alternative authentication methods.
3. Create temporary exception policies in a controlled manner (not recommended long-term).

This ensures security is maintained while minimizing disruption to critical legacy services.

### Password Policy

  * In **Group Policy Management**, configure the **Default Domain Policy** (recommended for passwords).
  * Navigate to:

    * **Computer Configuration → Policies → Windows Settings → Security Settings → Account Policies → Password Policy**
  * Set:
    * **Enforce password history:** 10 previous passwords
    * **Maximum password age:** 90 days
    * **Minimum password length:** 16 characters
    * **Password must meet complexity requirements:** Enabled

**Account Lockout Policy**

* In the same **Account Policies → Account Lockout Policy** section:

  * **Account lockout threshold**: 3 invalid attempts.
  * **Account lockout duration**: 15 minutes.
  * **Reset account lockout counter after**: 5 minutes.


### Step 4: Test Group Policies

#### Force Group Policy Update

   * On Windows clients, run:

     ```powershell
     gpupdate /force
     ```
   * On Linux clients, restart **sssd** or log out/in:

     ```bash
     sudo systemctl restart sssd
     ```

#### **Windows 11 Client**

* **Password complexity and length:**

  * Try setting a weak password (e.g., `password123`) → should be rejected by policy.
  * Ensure new passwords are at least **16 characters** and meet complexity requirements.

* **Account lockout:**

  * Enter the wrong password **three times** → account should lock for **15 minutes**.
  * Verify the lockout counter resets after **30 minutes**.

#### **Windows 7 Client**

* **Network authentication:**

  * You may need to force Windows 7 to use NTLM instead of NTLMv2
  * Attempt to connect login from Windows 7  → should fail due to **NTLMv2-only enforcement**.

#### **Linux Client**

* **Non-domain login:**

  * Attempt to log in with a **non-domain user** → login should fail.

* **Domain user password policy:**

  * Log in as a domain user and attempt to change the password with `passwd` → weak passwords (<16 characters or failing complexity) should be denied.

* **Account lockout:**

  * Attempt SSH login with invalid credentials **three times** → account should lock according to the domain lockout policy.
  * Verify account status with:

    ```powershell
    Get-ADUser -Identity <user> -Properties LockedOut
    ```

## Common Windows GPO security settings

Here’s a **reference table** of common GPO security settings, organized by category, including purpose and example settings:

| **Category**                                   | **Purpose / Description**                                 | **Example Settings**                                                                                                                         |
| ---------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Account Policies**                           | Enforce secure credentials and Kerberos usage             | Password complexity, history, expiration; Account lockout threshold, duration; Kerberos ticket lifetimes                                     |
| **Local Policies – User Rights Assignment**    | Define which accounts can perform specific system actions | Log on locally, log on via RDP, shut down system, back up files, take ownership                                                              |
| **Local Policies – Security Options**          | Configure system-wide security behavior                   | Restrict local account usage of blank passwords, LAN Manager authentication level, rename Administrator account, force Ctrl+Alt+Del at logon |
| **Event Log Settings**                         | Control logging behavior and retention                    | Max log size, retention method, access permissions for Application, Security, System logs                                                    |
| **Audit Policy / Advanced Auditing**           | Track user actions and system changes                     | Logon/logoff events, account management, object access, policy changes, sensitive file/registry access                                       |
| **Windows Firewall & Network Protection**      | Control network traffic and protect systems               | Domain/private/public profile rules, inbound/outbound restrictions, packet logging                                                           |
| **Application Control / Software Restriction** | Prevent unauthorized or risky applications                | AppLocker rules, software whitelisting/blacklisting, script execution control                                                                |
| **Windows Update / Patch Management**          | Keep systems updated                                      | Automatic updates, scheduled installation, user override restrictions                                                                        |
| **BitLocker / Disk Encryption**                | Protect data at rest                                      | Enforce full disk encryption, recovery key storage, encryption policy for removable drives                                                   |
| **Administrative Templates**                   | Customize OS and app behavior                             | USB/removable drive restrictions, control panel access, browser security settings, antivirus/Defender configuration                          |
| **Miscellaneous Security**                     | Additional hardening measures                             | Enforce password-protected screensavers, inactivity timeouts, restrict anonymous access to shares, control delegation and trusts             |

**Usage Tips:**

* Use this table as a **planning reference** before implementing GPOs.
* Not every setting is required—choose based on **risk, compliance, and operational needs**.
* Combine these settings with monitoring and incident response for full security coverage.



## Deliverables

| **Task**                               | **Deliverable**                                                                                                                                                                                                                                                                       | **Points** |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **User Privilege & Subsystem Control** | Screenshots and explanation showing **least-privilege enforcement** (e.g., restricted local account logins, role-based group membership)                                                                                                                                              | 30         |
| **AD DS Deployment**                   | Screenshots of **Server 2022 Active Directory Domain Services (AD DS) installation** and initial **domain creation**                                                                                                                                                                  | 15         |
| **Windows Domain Join**             | Screenshots verifying a **Windows 7 & 11 clients successfully joined to the domain** and a **domain user login**                                                                                                                                                                           | 15         |
| **Linux Domain Join**                  | Screenshots verifying **Linux client AD integration** (e.g., successful domain user login, SSSD/Kerberos configuration)                                                                                                                                                               | 20         |
| **Group Policy Enforcement**           | Screenshots + explanation of applied **security GPOs**, including: <br>• Password Policy <br>• Account Lockout Policy <br>• Authentication Policy | 20         |

### Submission Requirements

* Submit a **single PDF** file containing:
  * Screenshots (clearly labeled and readable).
  * The two memos (subsystem control + AD policy memo).
* Upload the PDF to **Learning Suite**. Other formats will not be accepted.