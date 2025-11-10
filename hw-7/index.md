# Homework 7 – Linux User Management, Authentication, Services & Security

## Learning Outcomes

By completing this assignment, you will:

* Understand how **Linux manages user identities and authentication** through local files and PAM (Pluggable Authentication Modules).
* Learn to implement **least privilege access** using `sudoers` and group-based permissions.
* Strengthen the security of **SSH services** by enforcing key-based authentication and disabling insecure configurations.
* Develop skills in creating and enforcing **system security policies** through user and service configuration.

## Assignment Overview

Linux systems rely on a combination of user accounts, group membership, authentication subsystems (such as PAM), and service configurations (such as SSH) to control access and maintain security. Administrators can enforce **security policies** that define who can log in, what privileges they can escalate to, and how remote access is controlled.

In this assignment, you will configure and test several core Linux security mechanisms that support both **local authentication** and **remote access control**. You will practice enforcing least privilege principles, explore how Linux validates users through PAM, and harden SSH to prevent unauthorized access.

The assignment is divided into two main parts:

1. **User Management and Authentication Controls (Ubuntu Desktop)**
1. **SSH Service Hardening (Ubuntu Server)**

## Part 1: Ubuntu Desktop – User Management & Authentication Controls

### Step 1: Create and Manage User Accounts

1. Take a snapshot of your **Ubuntu Server**VM

1. Inside your VM. Open a terminal and create the following users:

  - analyst1
  - intern1

### Step 2: Configure `sudoers` for Least Privilege using User-Based Permissions

1. **Edit the sudoers file safely**

   Always use:

   ```bash
   sudo visudo
   ```

   `visudo` validates syntax before saving — preventing system lockouts from syntax errors.


1. **Add user-specific rules under “User privilege specification”**

   ```text
   analyst1 ALL=(ALL:ALL) ALL
   intern1  ALL=(ALL:ALL) /usr/bin/apt-get update, /usr/bin/cat /var/log/auth.log
   ```

   **Explanation:**

   * `analyst1 ALL=(ALL:ALL) ALL`
     → `analyst1` can run *any command* as *any user or group* on *any host*.
     *(Full administrative access.)*

   * `intern1 ALL=(ALL:ALL) /usr/bin/apt-get update, /usr/bin/cat /var/log/auth.log`
     → `intern1` can run **only** the two listed commands:

     * `sudo apt-get update` - Allowed
     * `sudo apt-get upgrade` - Denied


1. **How command matching works**

   * Sudo compares the **absolute command path** and **arguments** to what’s listed.
   * Examples:

     | Entry                     | Effect                                                  |
     | ------------------------- | ------------------------------------------------------- |
     | `/usr/bin/apt-get`        | Allows any apt-get command                              |
     | `/usr/bin/apt-get update` | Allows only `update`                                    |
     | `/usr/bin/apt-get *`      | Allows apt-get with any single argument (use carefully) |

   **Verify permissions:**

   ```bash
   sudo -l                 # Show what the current user can run
   sudo -U intern1 -l      # (Run as root) Show intern1’s allowed commands
   ```
   Take a screenshot of the output of these two commands.

1. **Prefer restricting “run-as” user**

   Instead of `(ALL:ALL)`, restrict to root when possible:

   ```text
   intern1 ALL=(root) /usr/bin/apt-get update, /usr/bin/cat /var/log/auth.log
   ```

   Reduces privilege exposure and makes intent clearer.

1. **Use aliases for cleaner configuration**

   ```text
   Cmnd_Alias APT_UPDATE = /usr/bin/apt-get update
   Cmnd_Alias VIEW_AUTH  = /usr/bin/cat /var/log/auth.log

   intern1 ALL=(root) APT_UPDATE, VIEW_AUTH
   ```

   Easier to maintain and audit as your sudoers file grows.

1. **Verify permissions:**

   ```bash
   sudo -l                
   sudo -U intern1 -l 
   ```
   Take a screenshot of the output of these two commands.


1. **Optional: Allow passwordless execution**

   ```text
   intern1 ALL=(root) NOPASSWD: APT_UPDATE, VIEW_AUTH
   ```
   Use `NOPASSWD` ONLY when operationally required. It removes an authentication checkpoint and reduces accountability.


### Step 3: Configure `sudoers` using Group-Based Permissions

Group-based sudo rules are more scalable and consistent for teams. Instead of listing individual users, you define group rules using `%groupname`.

1. **Create Security Groups**
   * Create two groups named **analysts** and **interns**.
   * Add the user **analyst1** to the *analysts* group and the user **intern1** to the *interns* group.

   * `groupadd` creates new groups (`analysts` and `interns`).
   * `usermod -aG` appends the user to the specified supplementary group(s).

     * `-a` = *append* (keep existing groups).
     * `-G` = *specify group(s)* to add the user to.
   * **Important:** Always use **`-aG`** together.
     Using just `-G` (without `-a`) replaces all existing group memberships and may remove the user from critical groups like `sudo`.

1. **Verify Groups:**

   ```bash
   groups analyst1             
   groups intern1
   ```
   Take a screenshot of the output of these two commands.


1. **Edit sudoers file**

   Remove the rules you created for Step 2.2. Make sure you take a screenshot before you remove them.
   Add group-based privilege rules:

   ```
   %analysts ALL=(ALL:ALL) ALL
   %interns  ALL=(root) APT_UPDATE, VIEW_AUTH
   ```

   **Explanation:**

   * `%analysts` → all members of the `analysts` group have full sudo privileges.
   * `%interns` → all members of the `interns` group can only update packages and view auth logs as root.


1. **Verify permissions:**

   ```
   sudo -l                
   sudo -U intern1 -l 
   ```
   Take a screenshot of the output of these two commands.



#### Advantages of group-based sudoers

   * **Scalability:** Easier to add/remove users — no file edits required.
   * **Consistency:** Ensures identical permissions across multiple users.
   * **Auditability:** Clear role separation in `/etc/group` and sudoers.
   * **Safer:** Reduces human error by centralizing role definitions.


#### Evaluation Order

When creating **permissions and groups**, it’s important to understand how Linux evaluates access control rules.
Different subsystems (file permissions, ACLs, and sudo policies) have **different evaluation orders**, meaning which rule “wins” when multiple apply.

The `/etc/sudoers` file follows a specific evaluation order:

1. **User-specific rules** are checked first.
1. **Group-based rules** (e.g., `%analysts ALL=(ALL) /usr/bin/apt-get update`) are checked second.
1. **Defaults** (e.g., `Defaults requiretty`, `Defaults logfile=...`) apply last if no specific match is found.

**Key point:** If a user has both a **user** and **group** sudo rule, the **user rule overrides** the group rule.
This allows administrators to make **exceptions** for specific users without rewriting group policies.

**Example:**

```text
# User rule
intern1 ALL=(root) /usr/bin/cat /var/log/auth.log

# Group rule
%interns ALL=(root) /usr/bin/apt-get update

# Result
intern1 can run both commands — their user rule adds privileges beyond the group rule.
```

* However, if a user rule *restricts* commands more narrowly than a group rule, that restriction takes precedence for that user.


### Step 4: Explore Linux Authentication Subsystem (PAM)

**Pluggable Authentication Modules (PAM)** is a flexible, modular framework used by Linux and Unix systems to manage authentication, account, session, and password policies. Rather than hardcoding authentication methods into each service (like SSH, login, or sudo), PAM allows administrators to configure authentication rules dynamically through configuration files in `/etc/pam.d/`. Each service can “plug in” different modules, such as password complexity checks, multi-factor authentication, or LDAP/Active Directory integration. This modular design makes it easier to enforce consistent security policies across multiple services while allowing fine-grained control over who can log in, when, and under what conditions. Essentially, PAM decouples authentication logic from individual applications, centralizing security management and simplifying policy enforcement.


1. Examine the PAM configuration for login authentication:

   ```bash
   cat /etc/pam.d/common-auth
   ```
1. Identify the modules used for password authentication (e.g., `pam_unix.so`, `pam_deny.so`).

1. Modify the failure delay by adding:

   ```
   auth optional pam_faildelay.so delay=5000000
   ```

   This enforces a **5-second delay** on failed logins to mitigate brute-force attempts. 

1. **Verify the delay:**

   * Enter the wrong password and see if the 5 second delay is enforced.
   * Take a screenshot of the `/etc/pam.d/common-auth` file


### Step 5: Configure a Password Policy for Users

A strong password policy is critical for enforcing account security and reducing the risk of compromise. In Linux, password policies can be enforced via **PAM modules** and system configuration files.


1. Edit PAM password settings

    1. Open the PAM password configuration file:

         ```bash
         sudo nano /etc/pam.d/common-password
         ```

    1. Locate the `pam_unix.so` line, which handles traditional password authentication, and add options for complexity, minimum length, and history:

         ```text
         password  requisite  pam_pwquality.so retry=3 minlen=12 ucredit=-1 lcredit=-1 ocredit=-1
         password  required   pam_pwhistory.so remember=2 enforce_for_root
         password  [success=1 default=ignore] pam_unix.so obscure sha512 use_authtok try_first_pass
                  
         ```

      * Take a screenshot of the `/etc/pam.d/common-password` file


      **Explanation of options:**

         * `retry=3` - Allow 3 attempts before rejecting the change.
         * `minlen=12` - Minimum password length of 12 characters.
         * `ucredit=-1` - Require at least 1 uppercase letter.
         * `lcredit=-1` - Require at least 1 lowercase letter.
         * `dcredit=-1` - Require at least 1 digit.
         * `ocredit=-1` - Require at least 1 special character.
         * `sha512` - Use SHA-512 hashing for password storage.
         * `remember=5` - Remeber the last 5 passwords.

1. Set password expiration and history

    1. Edit `/etc/login.defs` to configure system-wide defaults:

        ```text
        PASS_MAX_DAYS   90    # Maximum days before password expires
        PASS_MIN_DAYS   7     # Minimum days before a password can be changed
        PASS_WARN_AGE   14    # Warn user 14 days before expiration
        ```

      * Check that the settings have been applied using

      ```
      sudo chage -l intern1
      ```

      * You'll notice that the settings will not be applied. These settings will only apply to newly created users. To apply these settings to an existing user, run

      ```
      sudo chage -M 90 -m 7 -W 14 <user>
      ```

      * Run `sudo chage -l <user>` again to verify they have now been applied.

      * Take a screenshot of the `/etc/login.defs` file and your testing showing the settings applied to the user.



1. **Test the password policy**

   1. Attempt to change a password with `passwd`:
   1. Try using weak passwords (e.g., `password123`) to verify that PAM enforces complexity rules.
   1. Confirm that strong passwords (meeting length, character variety, and history requirements) are accepted.
   1. Change the password again using a password that meetings the requirements
   1. Try changing the password back to an old password that meets the requirements which should be denied
   1. Take a screenshot showing all of the above.

## Part 2: Ubuntu Server – SSH Hardening

### Step 1: Configure Key-Based Authentication

1. On your **Windows 11 VM**, generate two SSH key pairs. One for the user analyst1 and the other for intern1.
   - Use the `ssh-keygen` command in PowerShell. Make sure you give the keys different names when asked `Enter file in which to save the key`. If you leave this blank or choose the same name, you will only one key.
1. Copy the public key to your Ubuntu Server VM:
1. Verify key-based login works
1. Take a screenshot showing both keys work.

### Step 2: Disable Password Authentication and Root Login

Disabling password authentication and root login is a critical step in securing SSH access. By enforcing **key-based authentication** and preventing direct root login, you greatly reduce the risk of brute-force attacks and unauthorized access.


1. Edit the SSH configuration file

   Open the SSH server configuration file with a text editor:

   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

   * This file controls the behavior of the SSH daemon (`sshd`), including authentication methods, login restrictions, and security settings.


1. Update the relevant configuration options

   Locate (or add) the following lines in the file:

   ```text
   PermitRootLogin no
   PasswordAuthentication no
   ```

   **Explanation of each option:**

   * `PermitRootLogin no`

      * Prevents the root account from logging in directly over SSH.
      * Even if an attacker guesses the root password, direct access is blocked.
      * Admins can still gain root privileges by logging in as a normal user and using `sudo`.

   * `PasswordAuthentication no`

      * Disables password-based authentication entirely.
      * Only SSH keys (public/private key pairs) can be used to log in.
      * This eliminates the risk of brute-force password attacks.


1. **Set reasonable values for the following SSH configuration settings**

   * **LoginGraceTime**: The amount of time (in seconds) that the SSH server waits for a user to successfully authenticate after connecting. This helps prevent idle or abandoned connection attempts from consuming server resources.

   * **MaxAuthTries**: The maximum number of authentication attempts allowed per connection. This reduces the risk of brute-force attacks by limiting failed login attempts.
  
   * **MaxSessions** The maximum number of open sessions permitted per network connection. This prevents users or attackers from opening excessive concurrent sessions that could exhaust server resources.
  
   These settings strengthen SSH security by minimizing exposure time, limiting brute-force attempts, and preventing session abuse — all while maintaining usability for legitimate users.


1. **Restart the SSH service**

   After saving the changes, restart the SSH daemon to apply the new configuration:

   ```bash
   sudo systemctl restart ssh
   ```

   **Explanation:**

   * The SSH service must be restarted for the configuration changes to take effect.
   * If something goes wrong, you can still access the server locally to fix configuration mistakes.


1. Test the new SSH settings by attempting to log in from another terminal:

```bash
ssh user@server_ip
```

* Password login should fail.
* Only users with the proper private key corresponding to a public key in `~/.ssh/authorized_keys` will succeed.
* Use the wrong key to test LoginGraceTime and MaxAuthTries
* Try opening multiple SSH sessions in exsses of the MaxSessions value




#### Why this matters

* **Reduces attack surface:** Eliminates simple brute-force attacks on user passwords.
* **Prevents root exploitation:** Even if root password is leaked, direct access is blocked.
* **Enforces best practices:** SSH key-based authentication is far more secure than passwords, especially on servers exposed to the Internet.


### Step 3: Restrict SSH Access

1. **Limit SSH logins to specific users**
   Use the `AllowUsers` directive in `/etc/ssh/sshd_config` to specify which user accounts are permitted to log in via SSH.

   ```bash
   AllowUsers analyst1
   ```

   This ensures only **analyst1** can access the system over SSH.


1. **Limit SSH logins to specific groups**
   Use the `AllowGroups` directive to permit SSH access for members of approved groups.

   ```bash
   AllowGroups analysts
   ```
   Only users who belong to the **analysts** group will be allowed SSH access.
   *(This is especially useful when managing access for teams rather than individual users.)*


1. **Deny specific users or groups from accessing SSH**
   You can explicitly block users or groups using the `DenyUsers` and `DenyGroups` directives.

   ```bash
   DenyUsers intern1
   DenyGroups interns
   ```

   This prevents **intern1** and all members of the **interns** group from logging in via SSH, even if other rules might otherwise allow it.


1. **Verify Restrictions**

   * Attempt to connect with both authorized and unauthorized accounts.
   * Authorized users (e.g., `analyst1`) should connect successfully.
   * Unauthorized users (e.g., `intern1` or members of `interns`) should be denied access.


**Note:**

* SSH evaluates **Deny** directives before **Allow** directives.
* After making changes, restart the SSH service to apply them

## Deliverables

Include screenshots that show the following.

| Category                                                       | Task                                                                                                      | Points |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |
| **Part 1: User Management & Authentication Controls (60 pts)** |                                                                                                           |        |
| User Account Creation                                          | Correctly created `analyst1` and `intern1` users, verified existence                                      | 5      |
| Sudoers – User-Based Permissions                               | Configured `analyst1` with full sudo                                                                      | 5      |
| Sudoers – User-Based Permissions                               | Configured `intern1` with limited commands (`apt-get update`, `cat /var/log/auth.log`)                    | 10     |
| Sudoers – Command Verification                                 | Successfully verified permissions using `sudo -l` and `sudo -U intern1 -l`                                | 5      |
| Sudoers – Run-As Restriction                                   | Used `(root)` for `intern1` instead of `(ALL:ALL)`                                                        | 5      |
| Sudoers – Aliases & Clean Config                               | Implemented `Cmnd_Alias` for cleaner configuration                                                        | 5      |
| Sudoers – Group-Based Permissions                              | Created `analysts` and `interns` groups and added users correctly                                         | 5      |
| Sudoers – Group Rules                                          | Configured group-based sudo rules correctly and removed previous user-based rules                         | 5      |
| PAM Authentication                                             | Modified `/etc/pam.d/common-auth` to include `pam_faildelay.so delay=5000000`                             | 5      |
| Password Policy – Login.defs                                   | Configured `PASS_MAX_DAYS`, `PASS_MIN_DAYS`, and `PASS_WARN_AGE` in `/etc/login.defs`                     | 5      |
| Password Policy Verification                                   | Tested password complexity, history enforcement, and expiration                                           | 5      |
| **Part 2: SSH Hardening (40 pts)**                             |                                                                                                           |        |
| Key-Based Authentication                                       | Generated keys for both `analyst1` and `intern1`, copied public keys correctly, verified login            | 5      |
| SSH Config – Security                                          | Edited `/etc/ssh/sshd_config` to the above specifications                                                 | 10     |
| SSH Config – Restrict Users                                    | Configured `AllowUsers` or `AllowGroups` correctly                                                        | 5      |
| SSH Config – Deny Users/Groups                                 | Configured `DenyUsers`/`DenyGroups` correctly for `intern1` and `interns`                                 | 5      |
| SSH Verification                                               | Verified login restrictions for allowed and denied users                                                  | 5      |
| SSH Restart & Testing                                          | Restarted SSH service and tested configuration changes                                                    | 10     |


## Submission Requirements

* Submit a **single PDF** containing:
  * Screenshots of all configurations and command outputs.
* Upload to **Learning Suite** by the deadline.
* Other formats will not be accepted.
