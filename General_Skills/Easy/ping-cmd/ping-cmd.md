# 🔮 Challenge: ping-cmd
**Category:** Web/General | **Difficulty:** Easy | **Author:** Yahaya Meddy | **Environment:** Ubuntu 22.04 (VirtualBox)

## 📝 Challenge Description
The server offers a service to ping an IP address (specifically Google's `8.8.8.8`). The goal is to bypass the intended functionality and trick the server into revealing hidden files.

---

## 🔍 Step-by-Step Analysis

### 1. Initial Testing (Sanity Check)
In the first step, I performed a standard ping to verify the service's behavior and ensure the connection via Netcat was stable.

**![Normal Ping](img/ping-cmd1.png)**

* **Input:** `8.8.8.8`
* **Result:** The server executed the ping command as expected. However, it was clear that standard input would not yield any flags.

### 2. Exploiting Command Injection (Listing Files)
Knowing that the server likely uses a shell to execute the ping, I used the semicolon (`;`) operator. In Linux, the semicolon acts as a command separator, allowing multiple commands to run sequentially.

**![Listing Directory](img/ping-cmd2.png)**

* **Command used:** `8.8.8.8 ; ls`
* **Technical Explanation:** The server executes: `ping 8.8.8.8 ; ls`. 
    The shell finishes the `ping` and immediately starts the `ls` command.
* **Discovery:** The output revealed two interesting files: `script.sh` and, more importantly, **`flag.txt`**.

### 3. Capturing the Flag
Now that the filename was known, I replaced the `ls` command with `cat` to read the contents of the flag file.

**![Reading Flag](img/ping-cmd3.png)**

* **Command used:** `8.8.8.8 ; cat flag.txt`
* **Result:** The server printed the flag directly into the terminal output.

---

## 🚩 Final Flag
`picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_d1fdbdd0}`

---

## 💡 Technical Deep Dive: Why did this work?
This attack is called **Command Injection**. It happens when an application passes unsafe user-supplied data (in this case, the IP string) to a system shell. 

1.  **Vulnerable Code Logic:** The server likely runs something like: 
    `system("ping -c 2 " + user_input);`
2.  **Input Manipulation:** By entering `; cat flag.txt`, we change the logic to:
    `system("ping -c 2 8.8.8.8 ; cat flag.txt");`
3.  **Shell Execution:** The OS sees two separate instructions and executes both with the privileges of the server application.

### Environment & Tools
* **OS:** Ubuntu 22.04 LTS (VirtualBox).
* **Tool:** `nc` (Netcat) for network communication.
* **Advantage:** Performing this in a Linux VM allows for immediate testing of command syntax (like `;` or `&&`) before sending it to the target.
