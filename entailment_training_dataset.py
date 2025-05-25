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
    {
        "control": "Users are permitted to set passwords without complexity requirements",
        "audit_statement": "All user passwords must be complex and difficult to guess",
        "expected_label": "contradiction",
    },
    {
        "control": "Unencrypted traffic is allowed on the internal network",
        "audit_statement": "Data in transit must always be encrypted",
        "expected_label": "contradiction",
    },
    {
        "control": "Backups are stored without any form of encryption",
        "audit_statement": "Backup data is encrypted for confidentiality",
        "expected_label": "contradiction",
    },
    {
        "control": "RDP is open to the internet without restriction",
        "audit_statement": "Remote access is secured through VPN and MFA",
        "expected_label": "contradiction",
    },
    {
        "control": "Employee accounts are never disabled regardless of inactivity",
        "audit_statement": "Dormant accounts must be locked automatically",
        "expected_label": "contradiction",
    },
    {
        "control": "There are no controls preventing software installation by users",
        "audit_statement": "Users must receive approval to install new applications",
        "expected_label": "contradiction",
    },
    {
        "control": "SMBv1 is enabled for compatibility with legacy systems",
        "audit_statement": "Legacy protocols are disabled on all machines",
        "expected_label": "contradiction",
    },
    {
        "control": "Audit logs are deleted every 15 days to save space",
        "audit_statement": "System logs are retained for 90 days or longer",
        "expected_label": "contradiction",
    },
    {
        "control": "Default administrative accounts are left active on all systems",
        "audit_statement": "Built-in administrator accounts are disabled by policy",
        "expected_label": "contradiction",
    },
    {
        "control": "Email traffic is not scanned for malware or phishing",
        "audit_statement": "Inbound email is filtered to detect malicious content",
        "expected_label": "contradiction",
    },
    {
        "control": "USB storage is permitted without encryption or logging",
        "audit_statement": "Use of removable storage is restricted and monitored",
        "expected_label": "contradiction",
    },
    {
        "control": "All traffic from guest Wi-Fi can access internal resources",
        "audit_statement": "Guest network is isolated from corporate systems",
        "expected_label": "contradiction",
    },
    {
        "control": "Accounts are never reviewed or audited",
        "audit_statement": "User access is reviewed periodically",
        "expected_label": "contradiction",
    },
    {
        "control": "Servers allow anonymous login via FTP",
        "audit_statement": "Anonymous access to services is prohibited",
        "expected_label": "contradiction",
    },
    {
        "control": "All Windows updates are deferred indefinitely",
        "audit_statement": "Systems receive security patches regularly",
        "expected_label": "contradiction",
    },
    # --- NEUTRALS ---
    {
        "control": "Conference rooms use motion detectors to save energy",
        "audit_statement": "Backups are encrypted before being transferred offsite",
        "expected_label": "neutral",
    },
    {
        "control": "Printers are enabled with secure print release",
        "audit_statement": "Email filtering is configured to block external spam",
        "expected_label": "neutral",
    },
    {
        "control": "Employees must badge in to access office elevators",
        "audit_statement": "All administrator activity is logged centrally",
        "expected_label": "neutral",
    },
    {
        "control": "Desktop wallpaper is standardized across all machines",
        "audit_statement": "TLS 1.0 and 1.1 are disabled for web servers",
        "expected_label": "neutral",
    },
    {
        "control": "Security teams use threat intelligence feeds to assess risk",
        "audit_statement": "USB devices are restricted to authorized users only",
        "expected_label": "neutral",
    },
    {
        "control": "Facilities access is restricted after business hours",
        "audit_statement": "Users must change their password every 60 days",
        "expected_label": "neutral",
    },
    {
        "control": "Meeting rooms have sound masking installed",
        "audit_statement": "Encrypted file transfers are required for confidential data",
        "expected_label": "neutral",
    },
    {
        "control": "The HR department uses DocuSign for internal approvals",
        "audit_statement": "Multi-factor authentication is enforced on all VPN connections",
        "expected_label": "neutral",
    },
    {
        "control": "Printers are equipped with badge authentication",
        "audit_statement": "Firewall rules restrict incoming SMB traffic",
        "expected_label": "neutral",
    },
    {
        "control": "Work anniversary messages are automated in the intranet portal",
        "audit_statement": "Security logs are retained for incident investigations",
        "expected_label": "neutral",
    },
    {
        "control": "All mobile devices are encrypted using MDM policies",
        "audit_statement": "Email access requires device compliance checks",
        "expected_label": "neutral",
    },
    {
        "control": "Password expiration is enforced every 90 days",
        "audit_statement": "Accounts must be reviewed for dormant usage",
        "expected_label": "neutral",
    },
    {
        "control": "Remote access is restricted to authorized devices",
        "audit_statement": "Administrator accounts are reviewed quarterly",
        "expected_label": "neutral",
    },
    {
        "control": "Backups are encrypted and replicated to a secondary data center",
        "audit_statement": "Event logs are retained in a central SIEM",
        "expected_label": "neutral",
    },
    {
        "control": "Software updates are managed via WSUS",
        "audit_statement": "Access to file shares requires authentication",
        "expected_label": "neutral",
    },
    {
        "control": "Only company-issued laptops are allowed on the corporate Wi-Fi",
        "audit_statement": "MFA is required for VPN logins",
        "expected_label": "neutral",
    },
    {
        "control": "Secure boot is enabled on all servers",
        "audit_statement": "Web browsing is restricted by content filters",
        "expected_label": "neutral",
    },
    {
        "control": "SIEM correlates login events across multiple platforms",
        "audit_statement": "TLS 1.0 is disabled on all Windows endpoints",
        "expected_label": "neutral",
    },
    {
        "control": "Endpoint detection is integrated with threat intelligence feeds",
        "audit_statement": "Users are required to lock their screens when away",
        "expected_label": "neutral",
    },
    {
        "control": "Guest wireless requires SMS-based onboarding",
        "audit_statement": "Privileged accounts are granted just-in-time access",
        "expected_label": "neutral",
    },
    # --- SEMANTIC ENTAILMENTS ---
    {
        "control": "Security controls ensure only signed executables can run",
        "audit_statement": "Execution of unverified binaries is blocked",
        "expected_label": "entailment",
    },
    {
        "control": "User accounts that remain inactive for 60 days are disabled automatically",
        "audit_statement": "Dormant accounts are inaccessible",
        "expected_label": "entailment",
    },
    {
        "control": "TLS 1.0 and SSL are disabled on internal systems",
        "audit_statement": "Outdated encryption protocols are not supported",
        "expected_label": "entailment",
    },
    {
        "control": "Access to system utilities requires elevation",
        "audit_statement": "Standard users cannot launch administrative tools",
        "expected_label": "entailment",
    },
    {
        "control": "Removable media is automatically blocked on servers",
        "audit_statement": "USB devices are not usable in server environments",
        "expected_label": "entailment",
    },
    {
        "control": "Workstations auto-lock after 5 minutes of inactivity",
        "audit_statement": "Devices enter a secure state when idle",
        "expected_label": "entailment",
    },
    {
        "control": "All email attachments are scanned before delivery",
        "audit_statement": "Files transmitted via email are screened for malware",
        "expected_label": "entailment",
    },
    {
        "control": "Security patches are installed within 24 hours of CVE publication",
        "audit_statement": "Critical vulnerabilities are mitigated promptly",
        "expected_label": "entailment",
    },
    {
        "control": "Administrator access requires VPN connection and MFA",
        "audit_statement": "Privileged users must authenticate using multiple methods remotely",
        "expected_label": "entailment",
    },
    {
        "control": "BitLocker is used to encrypt all fixed drives",
        "audit_statement": "Hard disks are secured using full disk encryption",
        "expected_label": "entailment",
    },
    {
        "control": "Security monitoring alerts on privilege escalation attempts",
        "audit_statement": "Unauthorized elevation of permissions triggers an alert",
        "expected_label": "entailment",
    },
    {
        "control": "Device control restricts access to external USB ports",
        "audit_statement": "Peripherals such as flash drives are blocked",
        "expected_label": "entailment",
    },
    {
        "control": "Screen lock activates automatically when users step away",
        "audit_statement": "Idle systems enforce session locking",
        "expected_label": "entailment",
    },
    {
        "control": "Security baselines require disabling local admin accounts",
        "audit_statement": "Built-in administrator login is not permitted",
        "expected_label": "entailment",
    },
    {
        "control": "Remote PowerShell access is limited to jump servers",
        "audit_statement": "PowerShell is only available through secure administrative hosts",
        "expected_label": "entailment",
    },
]
