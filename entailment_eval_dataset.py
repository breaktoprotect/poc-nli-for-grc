grc_eval_set_1 = {
    "name": "Control vs. Audit Statement NLI Inference Evaluation Set #1",
    "dataset": [
        {
            "control": "CrowdStrike endpoint detection and response agent is installed",
            "audit_statement": "We have endpoint protection software installed",
            "expected_label": "entailment",
        },
        {
            "control": "BitLocker encryption is enabled on all drives",
            "audit_statement": "All drives are protected with full disk encryption",
            "expected_label": "entailment",
        },
        {
            "control": "USB ports are blocked via Group Policy",
            "audit_statement": "Removable media is disabled on all machines",
            "expected_label": "entailment",
        },
        {
            "control": "Antivirus definitions are outdated by 30 days",
            "audit_statement": "Our antivirus system is up to date",
            "expected_label": "contradiction",
        },
        {
            "control": "Windows Firewall is disabled on all endpoints",
            "audit_statement": "All endpoints are protected by host-based firewalls",
            "expected_label": "contradiction",
        },
        {
            "control": "Audit log retention is configured for 90 days",
            "audit_statement": "We retain logs for compliance for at least 30 days",
            "expected_label": "entailment",
        },
        {
            "control": "Users can install software without admin approval",
            "audit_statement": "Only authorized software can be installed by users",
            "expected_label": "contradiction",
        },
        {
            "control": "Multi-factor authentication is enforced for VPN access",
            "audit_statement": "VPN logins require two-factor authentication",
            "expected_label": "entailment",
        },
        {
            "control": "Default administrator account is renamed and disabled",
            "audit_statement": "The default admin account has been secured",
            "expected_label": "entailment",
        },
        {
            "control": "Screen lock timeout is set to 30 minutes",
            "audit_statement": "Screens automatically lock after short periods of inactivity",
            "expected_label": "neutral",
        },
    ],
}

grc_eval_set_2 = {
    "name": "Control vs. Audit Statement NLI Inference Evaluation Set #2",
    "dataset": [
        {
            "control": "Windows Defender SmartScreen is enabled for all browsers",
            "audit_statement": "SmartScreen protection is active in all web browsers",
            "expected_label": "entailment",
        },
        {
            "control": "Removable media auto-run is disabled via GPO",
            "audit_statement": "USB devices do not execute programs automatically when plugged in",
            "expected_label": "entailment",
        },
        {
            "control": "Windows Remote Desktop is only accessible via VPN",
            "audit_statement": "Remote access to desktops is limited to secure VPN channels",
            "expected_label": "entailment",
        },
        {
            "control": "Firewall logging is not enabled for outbound connections",
            "audit_statement": "Outbound traffic is logged by the firewall for all hosts",
            "expected_label": "contradiction",
        },
        {
            "control": "All local admin accounts must use unique passwords",
            "audit_statement": "Administrator passwords are the same across all machines",
            "expected_label": "contradiction",
        },
        {
            "control": "PowerShell script execution is restricted by policy",
            "audit_statement": "No restrictions are applied to script execution environments",
            "expected_label": "contradiction",
        },
        {
            "control": "Audit policy includes command line process creation events",
            "audit_statement": "The audit log captures the full command lines of launched processes",
            "expected_label": "entailment",
        },
        {
            "control": "Legacy SMBv1 protocol is disabled on all servers",
            "audit_statement": "File sharing protocols in use support only modern SMB versions",
            "expected_label": "entailment",
        },
        {
            "control": "Access to Control Panel is restricted for standard users",
            "audit_statement": "Standard users can modify system settings via Control Panel",
            "expected_label": "contradiction",
        },
        {
            "control": "TLS 1.0 and TLS 1.1 are disabled across all systems",
            "audit_statement": "Only modern TLS protocols are enabled in the environment",
            "expected_label": "entailment",
        },
    ],
}

grc_eval_set_3 = {
    "name": "Control vs. Audit Statement NLI Inference Evaluation Set #3",
    "dataset": [
        {
            "control": "Administrator approval is required before installing device drivers",
            "audit_statement": "Drivers cannot be installed without administrative privileges",
            "expected_label": "entailment",
        },
        {
            "control": "Interactive logon messages are configured to display legal notices",
            "audit_statement": "Users are presented with a legal disclaimer during login",
            "expected_label": "entailment",
        },
        {
            "control": "Windows Hello for Business is disabled on all servers",
            "audit_statement": "Biometric authentication is permitted across the server fleet",
            "expected_label": "contradiction",
        },
        {
            "control": "Windows Error Reporting is disabled through Group Policy",
            "audit_statement": "Crash and diagnostic data is regularly uploaded to Microsoft",
            "expected_label": "contradiction",
        },
        {
            "control": "Network access: Do not allow anonymous enumeration of SAM accounts is enabled",
            "audit_statement": "Unauthorized users cannot list account names on the system",
            "expected_label": "entailment",
        },
        {
            "control": "Untrusted fonts are blocked from loading in isolated sessions",
            "audit_statement": "Fonts from unknown sources are permitted to load across all sessions",
            "expected_label": "contradiction",
        },
        {
            "control": "Unused local accounts are disabled automatically after 30 days of inactivity",
            "audit_statement": "Dormant user accounts remain active without restriction",
            "expected_label": "contradiction",
        },
        {
            "control": "The 'Guest' account is disabled by policy",
            "audit_statement": "A built-in account with limited access is still enabled on endpoints",
            "expected_label": "contradiction",
        },
        {
            "control": "Remote PowerShell is only accessible from authorized jump servers",
            "audit_statement": "All endpoints can be managed remotely via PowerShell from any host",
            "expected_label": "contradiction",
        },
        {
            "control": "Credential Guard is enabled on supported hardware",
            "audit_statement": "Credential theft protections are active on compliant systems",
            "expected_label": "entailment",
        },
    ],
}

grc_eval_set_4 = {
    "name": "Control vs. Audit Statement NLI Inference Evaluation Set #4",
    "dataset": [
        {
            "control": "Sysmon is deployed on all Windows servers for advanced logging",
            "audit_statement": "Endpoint telemetry includes detailed process and network activity logs",
            "expected_label": "entailment",
        },
        {
            "control": "All administrative access requires approval through privileged access workflow",
            "audit_statement": "Users cannot escalate to admin without going through a formal approval process",
            "expected_label": "entailment",
        },
        {
            "control": "Security patches are installed within 48 hours of critical CVE release",
            "audit_statement": "Vulnerability remediation for critical risks is enforced within two days",
            "expected_label": "entailment",
        },
        {
            "control": "TLS 1.3 is enforced across all externally facing applications",
            "audit_statement": "All public-facing systems support only the most secure transport protocols",
            "expected_label": "entailment",
        },
        {
            "control": "Application whitelisting is not enforced on any server tier",
            "audit_statement": "Only pre-approved software is allowed to execute in the server environment",
            "expected_label": "contradiction",
        },
        {
            "control": "All administrator sessions are automatically recorded and archived",
            "audit_statement": "Privileged user activity is not logged or reviewed",
            "expected_label": "contradiction",
        },
        {
            "control": "Cloud resource access is restricted via role-based access controls",
            "audit_statement": "Access to cloud assets is governed by predefined user roles",
            "expected_label": "entailment",
        },
        {
            "control": "BitLocker is not used to encrypt virtual desktop instances",
            "audit_statement": "Virtual desktops are encrypted to protect at-rest data",
            "expected_label": "contradiction",
        },
        {
            "control": "Removable media usage is monitored but not restricted",
            "audit_statement": "USB device usage is tightly controlled through policy enforcement",
            "expected_label": "contradiction",
        },
        {
            "control": "Physical access to server rooms is protected by biometric scanners",
            "audit_statement": "Multi-factor authentication controls physical entry into critical infrastructure zones",
            "expected_label": "entailment",
        },
    ],
}
