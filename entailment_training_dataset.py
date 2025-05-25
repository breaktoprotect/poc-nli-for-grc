grc_training_data = [
    {
        "control": "Logs are collected and stored for 180 days",
        "audit_statement": "Log data is retained for audit compliance",
        "expected_label": "entailment",
    },
    {
        "control": "BitLocker is enabled on all drives",
        "audit_statement": "Drives are encrypted with full disk encryption",
        "expected_label": "entailment",
    },
    {
        "control": "Browser access to risky sites is blocked",
        "audit_statement": "Web filtering prevents access to dangerous sites",
        "expected_label": "entailment",
    },
    {
        "control": "Audit logs are shipped to a centralized SIEM",
        "audit_statement": "Logs are monitored centrally",
        "expected_label": "entailment",
    },
    {
        "control": "USB access is blocked via group policy",
        "audit_statement": "Removable storage devices are not allowed",
        "expected_label": "entailment",
    },
    {
        "control": "Strong passwords are enforced",
        "audit_statement": "Users must create complex passwords",
        "expected_label": "entailment",
    },
    {
        "control": "MFA is enforced for VPN connections",
        "audit_statement": "VPN requires multiple factors to authenticate users",
        "expected_label": "entailment",
    },
    {
        "control": "Guest accounts are disabled",
        "audit_statement": "No one can log in using guest credentials",
        "expected_label": "entailment",
    },
    {
        "control": "Removable devices require encryption",
        "audit_statement": "External drives must use encryption",
        "expected_label": "entailment",
    },
    {
        "control": "Antivirus is deployed on all endpoints",
        "audit_statement": "Endpoints have antivirus software installed",
        "expected_label": "entailment",
    },
    {
        "control": "Firewall is turned on for all devices",
        "audit_statement": "Devices are protected by firewalls",
        "expected_label": "entailment",
    },
    {
        "control": "Sensitive data is encrypted in transit",
        "audit_statement": "Data sent across networks is protected",
        "expected_label": "entailment",
    },
    {
        "control": "Administrative tools require elevated permissions",
        "audit_statement": "Only admins can use certain tools",
        "expected_label": "entailment",
    },
    {
        "control": "RDP is only accessible through VPN",
        "audit_statement": "Remote desktop can\u2019t be accessed from public internet",
        "expected_label": "entailment",
    },
    {
        "control": "Local administrator accounts are disabled",
        "audit_statement": "Users cannot log in as local admins",
        "expected_label": "entailment",
    },
    {
        "control": "Default admin account is renamed and disabled",
        "audit_statement": "Default credentials are not usable",
        "expected_label": "entailment",
    },
    {
        "control": "Only signed scripts are allowed to run",
        "audit_statement": "Unsigned PowerShell scripts are blocked",
        "expected_label": "entailment",
    },
    {
        "control": "Patch updates are installed weekly",
        "audit_statement": "Systems are kept up to date regularly",
        "expected_label": "entailment",
    },
    {
        "control": "Auto-lock is set for 10 minutes of inactivity",
        "audit_statement": "Systems lock automatically when idle",
        "expected_label": "entailment",
    },
    {
        "control": "Application whitelisting is implemented",
        "audit_statement": "Only approved applications can run",
        "expected_label": "entailment",
    },
    {
        "control": "Guest accounts are enabled",
        "audit_statement": "Guest accounts are disabled",
        "expected_label": "contradiction",
    },
    {
        "control": "Patch updates are not enforced",
        "audit_statement": "Systems are updated weekly",
        "expected_label": "contradiction",
    },
    {
        "control": "Any user can run unsigned scripts",
        "audit_statement": "Only signed PowerShell scripts are allowed",
        "expected_label": "contradiction",
    },
    {
        "control": "Antivirus is outdated",
        "audit_statement": "Endpoints have up-to-date antivirus",
        "expected_label": "contradiction",
    },
    {
        "control": "RDP is exposed to the public internet",
        "audit_statement": "Remote desktop access requires VPN",
        "expected_label": "contradiction",
    },
    {
        "control": "No centralized log storage is used",
        "audit_statement": "Logs are retained for compliance",
        "expected_label": "contradiction",
    },
    {
        "control": "Firewall is turned off",
        "audit_statement": "Devices are protected by firewalls",
        "expected_label": "contradiction",
    },
    {
        "control": "MFA is not configured",
        "audit_statement": "VPN logins require multiple authentication factors",
        "expected_label": "contradiction",
    },
    {
        "control": "USB ports are open on all machines",
        "audit_statement": "Removable storage devices are not allowed",
        "expected_label": "contradiction",
    },
    {
        "control": "BitLocker is disabled",
        "audit_statement": "Drives are encrypted with full disk encryption",
        "expected_label": "contradiction",
    },
    {
        "control": "Wi-Fi passwords are rotated every 6 months",
        "audit_statement": "USB ports are disabled by policy",
        "expected_label": "neutral",
    },
    {
        "control": "IT helpdesk tickets are closed within SLA",
        "audit_statement": "Web filtering blocks risky domains",
        "expected_label": "neutral",
    },
    {
        "control": "Building access is secured with keycards",
        "audit_statement": "Audit logs are sent to SIEM",
        "expected_label": "neutral",
    },
    {
        "control": "Users complete compliance training",
        "audit_statement": "Sensitive files are encrypted",
        "expected_label": "neutral",
    },
    {
        "control": "Conference rooms have monitors",
        "audit_statement": "Firewall is enabled on laptops",
        "expected_label": "neutral",
    },
    {
        "control": "Printers are deployed in each department",
        "audit_statement": "Drives are encrypted with full disk encryption",
        "expected_label": "neutral",
    },
    {
        "control": "Staff are trained quarterly on security topics",
        "audit_statement": "VPN logins require two-factor authentication",
        "expected_label": "neutral",
    },
    {
        "control": "Mobile devices are managed using MDM",
        "audit_statement": "Only authorized apps are allowed to run",
        "expected_label": "neutral",
    },
    {
        "control": "Each user has an email account",
        "audit_statement": "Multi-factor authentication is enabled for VPN",
        "expected_label": "neutral",
    },
    {
        "control": "Network switches are labeled",
        "audit_statement": "Default admin accounts are renamed",
        "expected_label": "neutral",
    },
    {
        "control": "CrowdStrike endpoint detection and response agent is installed",
        "audit_statement": "We have endpoint protection software installed",
        "expected_label": "entailment",
    },
    {
        "control": "All servers use disk encryption via BitLocker",
        "audit_statement": "Server disks are encrypted at rest",
        "expected_label": "entailment",
    },
    {
        "control": "Audit logs are maintained for 90 days and sent to the SIEM",
        "audit_statement": "We retain logs centrally for compliance needs",
        "expected_label": "entailment",
    },
    {
        "control": "All USB storage access is blocked on company laptops",
        "audit_statement": "Removable storage is restricted",
        "expected_label": "entailment",
    },
    {
        "control": "RDP sessions require both VPN and MFA",
        "audit_statement": "Remote desktop access is secured with multiple authentication layers",
        "expected_label": "entailment",
    },
    {
        "control": "Antivirus definitions have not been updated in 2 months",
        "audit_statement": "Endpoints are secured with current antivirus signatures",
        "expected_label": "contradiction",
    },
    {
        "control": "Local admin access is granted to all users",
        "audit_statement": "Only IT staff have administrator access",
        "expected_label": "contradiction",
    },
    {
        "control": "Patch management is performed once a year",
        "audit_statement": "Patches are applied weekly",
        "expected_label": "contradiction",
    },
    {
        "control": "Printers are secured with PIN-based access",
        "audit_statement": "Drives are encrypted with BitLocker",
        "expected_label": "neutral",
    },
    {
        "control": "Conference rooms have occupancy sensors",
        "audit_statement": "Audit logs are reviewed weekly",
        "expected_label": "neutral",
    },
    {
        "control": "Power-saving mode is enabled on monitors",
        "audit_statement": "MFA is enforced for VPN access",
        "expected_label": "neutral",
    },
    {
        "control": "System event logs are retained for 6 months",
        "audit_statement": "System logs are stored for at least 180 days",
        "expected_label": "entailment",
    },
    {
        "control": "Removable media is blocked on servers",
        "audit_statement": "USB storage devices are not permitted on server infrastructure",
        "expected_label": "entailment",
    },
    {
        "control": "Remote PowerShell access is disabled for non-admin users",
        "audit_statement": "Only administrators can use PowerShell remotely",
        "expected_label": "entailment",
    },
    {
        "control": "Users must reset their passwords every 60 days",
        "audit_statement": "Password expiration is enforced regularly",
        "expected_label": "entailment",
    },
    {
        "control": "Unpatched systems are allowed on the network",
        "audit_statement": "All systems are updated regularly",
        "expected_label": "contradiction",
    },
    {
        "control": "No backups are performed for user data",
        "audit_statement": "User data is backed up weekly",
        "expected_label": "contradiction",
    },
    {
        "control": "Guest Wi-Fi is isolated from internal network",
        "audit_statement": "Guest wireless cannot access internal systems",
        "expected_label": "entailment",
    },
    {
        "control": "System hardening standards are not applied",
        "audit_statement": "Servers follow baseline security configurations",
        "expected_label": "contradiction",
    },
    {
        "control": "The company cafeteria uses smart trays",
        "audit_statement": "BitLocker is deployed on company laptops",
        "expected_label": "neutral",
    },
    {
        "control": "Conference room bookings are automated via Outlook",
        "audit_statement": "Firewall policies are enforced at the endpoint",
        "expected_label": "neutral",
    },
    {
        "control": "USB ports are disabled on all user laptops",
        "audit_statement": "Removable media is not allowed on end-user devices",
        "expected_label": "entailment",
    },
    {
        "control": "Group policy blocks access to USB storage devices",
        "audit_statement": "Removable media is disabled across the enterprise",
        "expected_label": "entailment",
    },
    {
        "control": "Access to external drives via USB is prohibited",
        "audit_statement": "The use of removable media is restricted",
        "expected_label": "entailment",
    },
    # Admin secured ≈ renamed and disabled
    {
        "control": "Default administrator account is renamed and disabled",
        "audit_statement": "The default admin account has been secured",
        "expected_label": "entailment",
    },
    {
        "control": "We have disabled and renamed all default administrative accounts",
        "audit_statement": "Default admin credentials have been secured",
        "expected_label": "entailment",
    },
    {
        "control": "Built-in admin accounts are no longer in use",
        "audit_statement": "Default administrator accounts are secured",
        "expected_label": "entailment",
    },
    # MFA ≈ 2FA for VPN
    {
        "control": "Multi-factor authentication is enforced for VPN access",
        "audit_statement": "VPN logins require two-factor authentication",
        "expected_label": "entailment",
    },
    {
        "control": "VPN users must authenticate with two factors",
        "audit_statement": "MFA is required for VPN access",
        "expected_label": "entailment",
    },
    {
        "control": "Two-factor authentication is required to access the VPN",
        "audit_statement": "Multi-factor authentication is enabled for remote access",
        "expected_label": "entailment",
    },
    # Training data added 25 May 2025 12:13pm (SGT)
    {
        "control": "Accounts inactive for over 45 days are locked automatically",
        "audit_statement": "Dormant user accounts are not accessible",
        "expected_label": "entailment",
    },
    {
        "control": "Only TLS 1.2 and TLS 1.3 are permitted on enterprise systems",
        "audit_statement": "Legacy encryption protocols are disabled",
        "expected_label": "entailment",
    },
    {
        "control": "The built-in Administrator account is renamed and disabled",
        "audit_statement": "Default privileged accounts are secured",
        "expected_label": "entailment",
    },
    {
        "control": "Only trusted file paths are permitted for execution via AppLocker",
        "audit_statement": "Application control enforces an approved execution list",
        "expected_label": "entailment",
    },
    {
        "control": "PowerShell Constrained Language Mode is enforced for all users",
        "audit_statement": "Scripting capabilities are restricted by policy",
        "expected_label": "entailment",
    },
    {
        "control": "Network shares are inaccessible without authentication",
        "audit_statement": "Anonymous access to shared folders is not allowed",
        "expected_label": "entailment",
    },
    {
        "control": "Security updates must be applied within 48 hours of release",
        "audit_statement": "Patching is enforced within two days for critical vulnerabilities",
        "expected_label": "entailment",
    },
    {
        "control": "Group Policy prevents installation of unsigned drivers",
        "audit_statement": "Unverified drivers cannot be installed on managed systems",
        "expected_label": "entailment",
    },
    {
        "control": "Credential Guard is required on all domain-joined laptops",
        "audit_statement": "Credential theft protections are active on employee endpoints",
        "expected_label": "entailment",
    },
    {
        "control": "Guest access to SMB shares is disabled by default",
        "audit_statement": "Unauthenticated users cannot access file shares",
        "expected_label": "entailment",
    },
    {
        "control": "Only TLS 1.2 and above are permitted",
        "audit_statement": "TLS 1.0 is allowed for legacy applications",
        "expected_label": "contradiction",
    },
    {
        "control": "Local administrator accounts must be disabled",
        "audit_statement": "Users may sign in using built-in administrator credentials",
        "expected_label": "contradiction",
    },
    {
        "control": "Credential Guard is enforced on all enterprise laptops",
        "audit_statement": "Enterprise systems do not use Credential Guard protections",
        "expected_label": "contradiction",
    },
    {
        "control": "USB storage access is blocked through device control policy",
        "audit_statement": "Users are allowed to use USB drives for file transfer",
        "expected_label": "contradiction",
    },
    {
        "control": "PowerShell execution is limited to signed scripts only",
        "audit_statement": "PowerShell scripts can be executed without restriction",
        "expected_label": "contradiction",
    },
    {
        "control": "Only authenticated users can access file shares",
        "audit_statement": "Anonymous access to shared folders is enabled for all users",
        "expected_label": "contradiction",
    },
    {
        "control": "Software installation requires elevated administrative approval",
        "audit_statement": "Users can install applications without requiring admin rights",
        "expected_label": "contradiction",
    },
    {
        "control": "Firewall rules block all incoming SMB traffic",
        "audit_statement": "Incoming SMB connections are accepted on open ports",
        "expected_label": "contradiction",
    },
    {
        "control": "Remote Desktop Protocol is disabled on all production systems",
        "audit_statement": "RDP is enabled for external access to servers",
        "expected_label": "contradiction",
    },
    {
        "control": "Screens must lock after 10 minutes of inactivity",
        "audit_statement": "Workstations remain unlocked indefinitely",
        "expected_label": "contradiction",
    },
    {
        "control": "Windows Hello for Business is disabled",
        "audit_statement": "MFA is enabled for cloud applications",
        "expected_label": "neutral",
    },
    {
        "control": "AppLocker enforces signed binaries only",
        "audit_statement": "Web filtering prevents downloads from malicious sites",
        "expected_label": "neutral",
    },
    {
        "control": "Antivirus signatures are updated hourly",
        "audit_statement": "Audit logs are retained for 90 days",
        "expected_label": "neutral",
    },
    {
        "control": "Password complexity requirements are enabled",
        "audit_statement": "RDP is accessible only through VPN",
        "expected_label": "neutral",
    },
    {
        "control": "BitLocker is enforced on removable media",
        "audit_statement": "USB ports are blocked on corporate desktops",
        "expected_label": "neutral",
    },
    {
        "control": "Only whitelisted apps can run on endpoints",
        "audit_statement": "Sensitive data is encrypted in transit",
        "expected_label": "neutral",
    },
    {
        "control": "Security baselines are applied through Group Policy",
        "audit_statement": "Email access is protected by conditional access policies",
        "expected_label": "neutral",
    },
    {
        "control": "Account lockout threshold is set to 5 failed attempts",
        "audit_statement": "TLS 1.3 is required for HTTPS endpoints",
        "expected_label": "neutral",
    },
    {
        "control": "Only compliant mobile devices may connect via MDM",
        "audit_statement": "Desktop firewall is enabled for all Windows endpoints",
        "expected_label": "neutral",
    },
    {
        "control": "Legacy software is restricted from running",
        "audit_statement": "Default domain policy applies logon hours",
        "expected_label": "neutral",
    },
]
