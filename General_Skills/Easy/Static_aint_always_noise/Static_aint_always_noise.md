# 🔮 Challenge: Static ain't always noise
**Category:** General Skills | **Difficulty:** Easy | **Author:** syreal

## 📝 Challenge Description
*"Can you look at the data in this binary? The bash script might help!"*

This challenge demonstrates how to extract human-readable information from a compiled binary file using both provided helper scripts and standard Linux utilities like `strings` and `grep`.

---

## 🔍 Analysis
We are provided with two files:
1. `static`: A compiled binary file.
2. `ltdis.sh`: A shell script designed to assist in "dissecting" the binary.

Before executing the script, I inspected its contents to understand how it processes the binary.

<div align="center">
  <img src="img/Static_aint_always_noise1.png" alt="Script Analysis" width="800"/>
  <p><i>Figure 1: Analyzing the 'ltdis.sh' script with 'cat' reveals it automates the creation of string and disassembly files.</i></p>
</div>

The script is a wrapper that automates the use of other tools (likely `strings` and `objdump`) to generate two output files from the binary: a strings file and a disassembly file.

---

## 🛠️ Solution

### Step 1: Making the Script Executable
By default, the script lacks execution permissions. I granted them using the `chmod` command.

<div align="center">
  <img src="img/Static_aint_always_noise2.png" alt="Permissions and Execution" width="800"/>
  <p><i>Figure 2: Granting executable permissions and running the script on the 'static' binary.</i></p>
</div>

As shown in **Figure 2**, running `./ltdis.sh static` processed the binary and informed the user about the newly created output files.

### Step 2: Locating the Flag
The script generated a file named `static.ltdis.strings.txt`. This file contains all human-readable sequences extracted from the binary. I utilized `grep` to quickly search through this file for the `picoCTF` flag format.

<div align="center">
  <img src="img/Static_aint_always_noise3.png" alt="Final Flag Extraction" width="800"/>
  <p><i>Figure 3: Piping 'grep' on the generated strings file instantly isolates the flag.</i></p>
</div>

*Note: The actual flag value may vary based on the specific challenge instance.*

---

## 🚩 Final Flag
<details>
  <summary>Click to reveal the flag</summary>
  
  `picoCTF{st4t1c_41nt_4lw4ys_n01s3_38383a53}` *(Beispiel-Flag, bitte mit deiner echten ersetzen!)*
</details>

---

## 💡 Key Takeaways
* **Static Analysis:** Information can often be gathered from a binary without ever executing it.
* **Script Understanding:** Analyzing provided tools (`.sh` scripts) to understand their underlying commands is an essential skill.
* **Efficient Forensics:** Using `strings` and `grep` is a powerful combination for basic malware analysis and forensic investigation.
