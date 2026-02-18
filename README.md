
# 🛡️ Controlled Keylogger Implementation for Security Research

## 📌 1. Abstract

This project is a controlled implementation of a keylogging system developed in Python to study input interception, encrypted data handling, authentication controls, persistence behavior, and network transmission patterns.

The objective is not operational deployment, but technical understanding of how such systems function so they can be detected, analyzed, and mitigated in real-world security environments.

All testing was performed inside isolated virtual machines.

---

## 🎯 2. Research Objectives

* 🔎 Analyze OS-level keyboard event interception
* 🔐 Implement symmetric encryption for secure log storage
* 👁️ Study authentication-gated decryption workflows
* ♻️ Examine startup persistence mechanisms
* 🌐 Observe outbound HTTP-based data transmission patterns
* 🛡️ Evaluate detection surfaces for EDR and monitoring tools

---

## 🧰 3. Technical Stack

* 🐍 **Python 3.x**
* ⌨️ `pynput` – keyboard event listener
* 🔐 `cryptography` (Fernet – AES-based symmetric encryption)
* 📷 `opencv-python` – biometric authentication prototype
* 🌐 `urllib` – HTTP-based network transmission
* 📦 `PyInstaller` – executable packaging

---

## 🏗️ 4. System Architecture

### 🔄 High-Level Flow

```
┌────────────────────┐
│  Keyboard Listener │
│   (pynput hook)    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Log Buffering    │
│ (in-memory queue)  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Encryption Layer  │
│   (Fernet / AES)   │
└─────────┬──────────┘
          │
          ├───────────────┐
          ▼               ▼
┌──────────────┐   ┌────────────────┐
│ Local Storage│   │ Network Module │
│  (.enc file) │   │  (HTTP POST)   │
└──────────────┘   └────────────────┘
          │
          ▼
┌────────────────────┐
│ Biometric Auth Gate│
│ (OpenCV LBPH)      │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│  Decryption & View │
└────────────────────┘
```

---

## ⚙️ 5. Core Components (Technical Breakdown)

### ⌨️ 5.1 Input Capture Layer

* Low-level keyboard hooks via `pynput`
* Event-driven architecture
* Non-blocking listener thread
* Key normalization for special keys
* Timestamp tagging for event correlation

**🛑 Detection Surface:**

* Suspicious background listeners
* Hook-based API monitoring
* Behavioral anomaly detection

---

### 🔐 5.2 Encryption Module

* Fernet (AES-128 CBC + HMAC authentication)
* Symmetric key generation
* Authenticated encryption
* Encrypted log file output (`.enc`)

**🧠 Security Insight:**
Encrypted payloads may bypass simple string detection, but entropy analysis and behavioral monitoring remain effective.

---

### 👁️ 5.3 Authentication Layer (Biometric Prototype)

* Haar Cascade for face detection
* LBPH for recognition
* Authentication gate before decryption

Purpose:

* Demonstrates access control layering
* Protects locally stored encrypted logs

---

### ♻️ 5.4 Persistence Study (Lab Only)

Startup registration behavior was analyzed to understand:

* Common persistence vectors
* Registry/startup folder monitoring
* EDR detection of abnormal autoruns

No uncontrolled deployment occurred.

---

### 🌐 5.5 Network Transmission Module

* Periodic HTTP-based data transmission
* Standard library implementation
* Buffered payload packaging

**🛑 Detection Surface:**

* Outbound anomaly detection
* Periodic POST pattern recognition
* Encrypted payload entropy inspection

---

## 📚 6. Research Report

### 🧩 6.1 Threat Model Simulation

This implementation models a simplified information-stealer architecture to evaluate:

* Attack chain stages
* Data collection methods
* Exfiltration timing strategies
* Defensive visibility points

---

### 🛡️ 6.2 Observed Defensive Control Points

| Layer          | Detection Strategy                    |
| -------------- | ------------------------------------- |
| ⌨️ Input Hook  | API monitoring / EDR behavioral flags |
| ♻️ Persistence | Autorun registry auditing             |
| 🔐 Encryption  | High-entropy file monitoring          |
| 🌐 Network     | Traffic anomaly detection             |
| 🧠 Process     | Background execution profiling        |

---

### 🔎 6.3 Key Findings

* Behavioral detection is more effective than signature detection.
* Persistence is often the weakest stealth component.
* Encrypted storage increases complexity but leaves entropy artifacts.
* Periodic outbound traffic is highly fingerprintable.

---

## ⚖️ 7. Ethical & Legal Boundaries

* 🧪 Implemented in isolated VM environments only
* 🚫 No unauthorized systems monitored
* 🔒 No real user credentials collected
* 📂 Private repository (not publicly distributed)
* 🎓 Intended strictly for cybersecurity education and analysis

Understanding offensive mechanisms improves defensive capability.

---

## 🗂️ 8. Repository Structure

```
keylogger-research-lab/
│
├── README.md
│
├── src/
│   ├── input_listener.py
│   ├── encryption.py
│   ├── auth_biometric.py
│   ├── network_module.py
│   ├── persistence_study.py
│   └── main.py
│
├── viewer/
│   └── log_viewer.py
│
├── research/
│   ├── threat_model.md
│   ├── detection_analysis.md
│   └── findings_summary.md
│
├── diagrams/
│   └── architecture.png
│
├── requirements.txt
└── LICENSE
```

---

## 🚧 9. Limitations

* Prototype-level biometric accuracy
* Simplified threat simulation
* No advanced obfuscation mechanisms
* Not intended for production deployment

---

## 👨‍💻 10. Author

**[NIKHIL MANVI]**
Cybersecurity Intern
[VIJESHA IT SERVICE LLP]
[2026]
