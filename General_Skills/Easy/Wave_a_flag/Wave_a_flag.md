# 🔮 Challenge: Wave a flag
**Category:** General Skills | **Difficulty:** Easy | **Author:** syreal

## 📝 Challenge Description
[cite_start]*"Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information... binary: warm"* [cite: 5]

[cite_start]This challenge focuses on interacting with binaries using CLI arguments and discovery flags to reveal hidden functionality or information. [cite: 5]

---

## 🔍 Analysis
The provided file `warm` is a compiled Linux binary. [cite_start]Executing it without arguments results in a prompt suggesting the use of a help flag. [cite: 5]

Static analysis or a simple initial run reveals the program's hint:  
> [cite_start]*"Hello user! Pass me a -h to learn what I can do!"* [cite: 5]

---

## 🛠️ Solution

### Step 1: Execution with the Help Flag
Following the hint provided by the binary, I executed the program with the `-h` flag. [cite_start]This triggered a specific logic branch within the code, revealing the flag. [cite: 4, 5]

### Step 2: Advanced Extraction (Piping)
To demonstrate efficient data extraction—a key skill in security automation—I combined the execution with a pipe to `grep`. [cite_start]This isolates the flag string from the surrounding text. [cite: 5]

```bash
./warm -h | grep -o "picoCTF{.*}"
```
* [cite_start]**`|` (Pipe)**: Redirects the standard output of the binary to the input of the next command. [cite: 5]
* [cite_start]**`grep -o`**: Extracts only the part of the string that matches the pattern `picoCTF{...}`. [cite: 5]

<div align="center">
  <img src="img/Wave_a_flag.png" alt="Complete Execution Workflow" width="800"/>
  [cite_start]<p><i>Figure 1: The terminal showing the initial help prompt and the final successful flag extraction using pipes.</i> [cite: 5]</p>
</div>

---

## 🚩 Final Flag
<details>
  <summary>Click to reveal the flag</summary>
  
  [cite_start]`picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}` [cite: 5]
</details>

---

## 💡 Key Takeaways
* [cite_start]**CLI Discovery**: Help flags (`-h`, `--help`) are the primary method of reconnaissance when analyzing unknown binaries. [cite: 5]
* [cite_start]**Data Piping**: Using pipes with `grep` allows for rapid, automated extraction of sensitive information like flags or keys. [cite: 5]
* [cite_start]**Execution Flow**: Many programs contain hidden messages or functions that are only accessible through specific command-line arguments. [cite: 5]
