# 🖨️ Challenge: Printer Shares
**Category:** General Skills | **Difficulty:** Easy | **Author:** Janice He | **Environment:** Ubuntu 22.04 (VirtualBox)

## 📝 Challenge Description
*"Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?"*

This challenge involves accessing a remote print server running on an unconventional port (**58899**) to retrieve a sensitive file that was "sent to the printer" by mistake.

> **Note:** This challenge uses **dynamic instances**. Each session provides a unique host and port.

---

## 🔍 Analysis

### 1. Connectivity & Reconnaissance
The first step was to verify the target's availability. I used **Netcat (`nc`)** with the `-vz` flags to perform a "Zero-I/O" scan, confirming the port was reachable.

**Command:** `nc -vz mysterious-sea.picoctf.net 58899`

As confirmed in **Printer_Shares2.png**, the connection succeeded. However, simply connecting via Netcat didn't provide a directory listing or a way to interact with the file system.

### 2. Identifying the Protocol
Based on the "Printer" and "Print Server" context, I suspected the **SMB (Server Message Block)** protocol. SMB is the standard for network file and printer sharing. While it usually runs on port 445, it is common in CTFs to find services on high-numbered ports like **58899**.

### 3. Overcoming Information Gaps
When I first tried to browse the server manually, it didn't return any immediate data. I turned to the **Hints** for guidance:
* *Hint 1:* "Knowing how SMB protocol works would be helpful!"
* *Hint 2:* "smbclient and smbutil are good tools."

This confirmed that I needed to use `smbclient` to enumerate the "Shares" (folders) available on the server.

---

## 🛠️ The Solution: SMB Enumeration & Retrieval

### Step 1: Listing Available Shares
I used `smbclient` with the `-L` (List) flag to see what was available. I used the `-N` flag for an **Anonymous Login** (no password) to see if the server was misconfigured to allow guest access.

`smbclient -L mysterious-sea.picoctf.net -p 58899 -N`

The scan revealed a share named **`shares`** with the description "Public Share With Guests."

### Step 2: Accessing the Files
Once the share name was known, I connected directly to it. Inside the SMB shell, I used standard navigation commands.

<div align="center">
  <img src="img/Printer_Shares1.png" alt="SMB Shell Interaction" width="800"/>
  <p><i>Figure 1: Navigating the SMB share and downloading the target file.</i></p>
</div>

**Execution Steps:**
1.  **`ls`**: Listed the files, revealing `dummy.txt` and the target `flag.txt`.
2.  **`get flag.txt`**: Since the SMB shell doesn't allow direct reading (like `cat`), I used `get` to transfer the file to my local **Ubuntu VM**.

### Step 3: Extracting the Flag
After exiting the SMB session, the file was locally available in my terminal environment.

<div align="center">
  <img src="img/Printer_Shares2.png" alt="Flag Capture" width="800"/>
  <p><i>Figure 2: Verifying the local file and reading the flag.</i></p>
</div>

---

## 🚩 Final Flag
Using the `cat` command on the downloaded file revealed the flag:

`picoCTF{5mb_pr1nter_5h4re5_8caa47ce}`

---

## 💡 Key Takeaways
* **Service Port Mapping:** Never assume a service is down just because it isn't on its default port. Port scanning and context clues are vital.
* **Misconfigured Shares:** Public guest access on SMB shares is a common real-world vulnerability that allows unauthorized data exfiltration.
* **SMB Client Tools:** Familiarity with `smbclient` is essential for navigating network environments within a Linux terminal.
