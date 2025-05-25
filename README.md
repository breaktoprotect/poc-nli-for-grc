<sub>📝 This README was generated with the help of ChatGPT-4o.</sub>

# GRC-NLI (Proof of Concept)

A feasibility study to evaluate whether fine-tuning a Natural Language Inference (NLI) cross-encoder model can determine if a cybersecurity control—such as a procedure or configuration setting—**supports an IT audit statement**.

## 💡 Objective

Use cases include:

-   Internal self-checks before formal audits
-   Automating audit validation workflows

This is part of a larger pipeline:

**🔍 SBERT Retrieval** — top-k cosine similarity
→ **⚖️ Cross-Encoder Reranker** — filters irrelevant results
→ **🧠 NLI Entailment Validator** — confirms support relationship

Compare inference accuracy between:

-   **Original model**: `cross-encoder/nli-deberta-v3-large`
-   **Fine-tuned version**: `./v1_finetuned_nli-deberta-v3-large` (trained on synthetic GRC pairs)

## ⚠️ Notes

> All datasets are **synthetically generated** using GPT-4o. This project is strictly for testing and research purposes.

---

## 🧠 Models

| Model                                 | Description                      |
| ------------------------------------- | -------------------------------- |
| `cross-encoder/nli-deberta-v3-large`  | Pretrained DeBERTa cross-encoder |
| `./v1_finetuned_nli-deberta-v3-large` | Fine-tuned version for GRC tasks |

---

## 🧾 Data

### Training Set

-   \~100 synthetic control–audit pairs
-   Labels: `entailment`, `contradiction`, `neutral`

> File: `entailment_training_dataset.py`

### Evaluation Sets

-   3 synthetic test sets to benchmark model performance

> File: `entailment_eval_dataset.py`

---

## 🔎 Example Training Samples

```json
{
    "control": "BitLocker is enabled on all drives",
    "audit_statement": "Drives are encrypted with full disk encryption",
    "expected_label": "entailment"
}
```

```json
{
    "control": "Firewall is turned off",
    "audit_statement": "Devices are protected by firewalls",
    "expected_label": "contradiction"
}
```

```json
{
    "control": "Staff are trained quarterly on security topics",
    "audit_statement": "VPN logins require two-factor authentication",
    "expected_label": "neutral"
}
```

---

## 📁 Structure

```
.
├── entailment_eval_dataset.py
├── entailment_training_dataset.py
├── run_inference.py
├── train_model.py
├── v1_finetuned_nli-deberta-v3-large/
```

---

## ⚙️ Usage

```bash
# Run inference
python run_inference.py

# Fine-tune model
python train_model.py

# Install dependencies
pip install -r requirements.txt
```

---

## 🖥️ Raw Console Output

```
[*] Model in use: cross-encoder/nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #1
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CrowdStrike endpoint detection and response agent is insta   | We have endpoint protection software installed               | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
BitLocker encryption is enabled on all drives                | All drives are protected with full disk encryption           | entailment   | entailment   | True     | 0.98 | [0.00, 0.98, 0.02]
USB ports are blocked via Group Policy                       | Removable media is disabled on all machines                  | neutral      | entailment   | False    | 0.97 | [0.02, 0.00, 0.97]
Antivirus definitions are outdated by 30 days                | Our antivirus system is up to date                           | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Windows Firewall is disabled on all endpoints                | All endpoints are protected by host-based firewalls          | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Audit log retention is configured for 90 days                | We retain logs for compliance for at least 30 days           | neutral      | entailment   | False    | 0.98 | [0.02, 0.00, 0.98]
Users can install software without admin approval            | Only authorized software can be installed by users           | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Multi-factor authentication is enforced for VPN access       | VPN logins require two-factor authentication                 | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Default administrator account is renamed and disabled        | The default admin account has been secured                   | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Screen lock timeout is set to 30 minutes                     | Screens automatically lock after short periods of inactivi   | neutral      | neutral      | True     | 0.98 | [0.01, 0.01, 0.98]

Accuracy: 6 / 10 = 60.00%
---

[*] Model in use: ./v1_finetuned_nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #1
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CrowdStrike endpoint detection and response agent is insta   | We have endpoint protection software installed               | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
BitLocker encryption is enabled on all drives                | All drives are protected with full disk encryption           | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
USB ports are blocked via Group Policy                       | Removable media is disabled on all machines                  | entailment   | entailment   | True     | 0.87 | [0.01, 0.87, 0.12]
Antivirus definitions are outdated by 30 days                | Our antivirus system is up to date                           | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Windows Firewall is disabled on all endpoints                | All endpoints are protected by host-based firewalls          | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Audit log retention is configured for 90 days                | We retain logs for compliance for at least 30 days           | entailment   | entailment   | True     | 0.98 | [0.02, 0.98, 0.00]
Users can install software without admin approval            | Only authorized software can be installed by users           | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Multi-factor authentication is enforced for VPN access       | VPN logins require two-factor authentication                 | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Default administrator account is renamed and disabled        | The default admin account has been secured                   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Screen lock timeout is set to 30 minutes                     | Screens automatically lock after short periods of inactivi   | entailment   | neutral      | False    | 0.99 | [0.00, 0.99, 0.01]

Accuracy: 9 / 10 = 90.00%
---

[*] Model in use: cross-encoder/nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #2
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Windows Defender SmartScreen is enabled for all browsers     | SmartScreen protection is active in all web browsers         | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Removable media auto-run is disabled via GPO                 | USB devices do not execute programs automatically when plu   | neutral      | entailment   | False    | 0.99 | [0.00, 0.01, 0.99]
Windows Remote Desktop is only accessible via VPN            | Remote access to desktops is limited to secure VPN channel   | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Firewall logging is not enabled for outbound connections     | Outbound traffic is logged by the firewall for all hosts     | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
All local admin accounts must use unique passwords           | Administrator passwords are the same across all machines     | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
PowerShell script execution is restricted by policy          | No restrictions are applied to script execution environmen   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Audit policy includes command line process creation events   | The audit log captures the full command lines of launched    | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Legacy SMBv1 protocol is disabled on all servers             | File sharing protocols in use support only modern SMB vers   | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Access to Control Panel is restricted for standard users     | Standard users can modify system settings via Control Pane   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
TLS 1.0 and TLS 1.1 are disabled across all systems          | Only modern TLS protocols are enabled in the environment     | contradiction | entailment   | False    | 0.99 | [0.99, 0.00, 0.01]

Accuracy: 5 / 10 = 50.00%
---

[*] Model in use: ./v1_finetuned_nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #2
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Windows Defender SmartScreen is enabled for all browsers     | SmartScreen protection is active in all web browsers         | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Removable media auto-run is disabled via GPO                 | USB devices do not execute programs automatically when plu   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Windows Remote Desktop is only accessible via VPN            | Remote access to desktops is limited to secure VPN channel   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Firewall logging is not enabled for outbound connections     | Outbound traffic is logged by the firewall for all hosts     | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
All local admin accounts must use unique passwords           | Administrator passwords are the same across all machines     | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
PowerShell script execution is restricted by policy          | No restrictions are applied to script execution environmen   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Audit policy includes command line process creation events   | The audit log captures the full command lines of launched    | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Legacy SMBv1 protocol is disabled on all servers             | File sharing protocols in use support only modern SMB vers   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Access to Control Panel is restricted for standard users     | Standard users can modify system settings via Control Pane   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
TLS 1.0 and TLS 1.1 are disabled across all systems          | Only modern TLS protocols are enabled in the environment     | contradiction | entailment   | False    | 1.00 | [1.00, 0.00, 0.00]

Accuracy: 9 / 10 = 90.00%
---

[*] Model in use: cross-encoder/nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #3
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Administrator approval is required before installing devic   | Drivers cannot be installed without administrative privile   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Interactive logon messages are configured to display legal   | Users are presented with a legal disclaimer during login     | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Windows Hello for Business is disabled on all servers        | Biometric authentication is permitted across the server fl   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Windows Error Reporting is disabled through Group Policy     | Crash and diagnostic data is regularly uploaded to Microso   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Network access: Do not allow anonymous enumeration of SAM    | Unauthorized users cannot list account names on the system   | neutral      | entailment   | False    | 1.00 | [0.00, 0.00, 1.00]
Untrusted fonts are blocked from loading in isolated sessi   | Fonts from unknown sources are permitted to load across al   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Unused local accounts are disabled automatically after 30    | Dormant user accounts remain active without restriction      | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
The 'Guest' account is disabled by policy                    | A built-in account with limited access is still enabled on   | neutral      | contradiction | False    | 0.99 | [0.01, 0.00, 0.99]
Remote PowerShell is only accessible from authorized jump    | All endpoints can be managed remotely via PowerShell from    | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Credential Guard is enabled on supported hardware            | Credential theft protections are active on compliant syste   | entailment   | entailment   | True     | 0.99 | [0.00, 0.99, 0.01]

Accuracy: 8 / 10 = 80.00%
---

[*] Model in use: ./v1_finetuned_nli-deberta-v3-large
[*] Evaluation set name: Control vs. Audit Statement NLI Inference Evaluation Set #3
Control                                                      | Audit Statement                                              | Predicted    | Expected     | Correct? | Conf   | [Contradict, Entail, Neutral]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Administrator approval is required before installing devic   | Drivers cannot be installed without administrative privile   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Interactive logon messages are configured to display legal   | Users are presented with a legal disclaimer during login     | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Windows Hello for Business is disabled on all servers        | Biometric authentication is permitted across the server fl   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Windows Error Reporting is disabled through Group Policy     | Crash and diagnostic data is regularly uploaded to Microso   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Network access: Do not allow anonymous enumeration of SAM    | Unauthorized users cannot list account names on the system   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]
Untrusted fonts are blocked from loading in isolated sessi   | Fonts from unknown sources are permitted to load across al   | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Unused local accounts are disabled automatically after 30    | Dormant user accounts remain active without restriction      | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
The 'Guest' account is disabled by policy                    | A built-in account with limited access is still enabled on   | entailment   | contradiction | False    | 0.90 | [0.00, 0.90, 0.09]
Remote PowerShell is only accessible from authorized jump    | All endpoints can be managed remotely via PowerShell from    | contradiction | contradiction | True     | 1.00 | [1.00, 0.00, 0.00]
Credential Guard is enabled on supported hardware            | Credential theft protections are active on compliant syste   | entailment   | entailment   | True     | 1.00 | [0.00, 1.00, 0.00]

Accuracy: 9 / 10 = 90.00%
---
```

## 📊 Results

| Eval Set | Baseline | Fine-Tuned |
| -------- | -------- | ---------- |
| Set #1   | 60%      | 90%        |
| Set #2   | 50%      | 90%        |
| Set #3   | 80%      | 90%        |

✅ Fine-tuning significantly improved accuracy across all test sets.

---

## 📦 Model Availability

The fine-tuned model (`./v1_finetuned_nli-deberta-v3-large`) is **not included** in this repository.
Feel free to run `train_model.py` to reproduce it locally.

## 💻 Fun Fact

This entire model was fine-tuned on a single NVIDIA 3060 Ti GPU.
Training took only about **5–10 minutes** for the full dataset.
Training used a fixed random seed (`42`) for reproducibility.
