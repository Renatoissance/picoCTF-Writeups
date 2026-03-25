\# Challenge: Log Hunt

\*\*Category:\*\* General Skills  

\*\*Difficulty:\*\* Easy  

\*\*Author:\*\* Yahaya Meddy



\## 📝 Challenge Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.



\---



\## 🔍 Analysis

After downloading and opening the `server.log` file, I noticed that the log entries were cluttered with standard INFO, WARN, and ERROR messages. However, many entries contained a specific keyword: `FLAGPART`.



In the initial inspection, it became clear that the flag was broken into several fragments scattered across different timestamps.



!\[Initial Log Inspection](./img/log\_hunt1.png)



\## 🛠️ Solution

To avoid searching through thousands of lines manually, I used the Windows Command Line tool `FINDSTR` to filter the log for all occurrences of the keyword "FLAGPART".



\*\*Command used:\*\*

```cmd

FINDSTR /C:"FLAGPART" server.log

```



The output (as seen below) revealed the fragments in a repetitive pattern. By identifying the unique parts and concatenating them, the full flag was reconstructed.



!\[Filtering with FINDSTR](./img/log\_hunt2.png)



\### Reconstructed Fragments:

1\. `picoCTF{us3\_`

2\. `y0urlinux\_`

3\. `sk1lls\_`

4\. `cedfa5fb}`



\---



\## 🚩 Final Flag

<details>

&#x20; <summary>Click to reveal the flag</summary>

&#x20; 

&#x20; `picoCTF{us3\_y0urlinux\_sk1lls\_cedfa5fb}`

</details>



\---



\## 💡 What I learned

\* \*\*Pattern Recognition:\*\* Identifying specific keywords (`FLAGPART`) within high-volume log data.

\* \*\*CLI Efficiency:\*\* Using `FINDSTR` (the Windows equivalent to Linux `grep`) to filter relevant information from noise.

\* \*\*Data Recovery:\*\* Reassembling a secret string from scattered log fragments.

