# CVE-2021-3156
Sudo before 1.9.5p2 contains an off-by-one error that can result in a heap-based buffer overflow, which allows privilege escalation to root via "sudoedit -s" and a command-line argument that ends with a single backslash character. [CVE-2021-3156](https://www.cve.org/CVERecord?id=CVE-2021-3156)

## PoC
The PoC from CptGibbon's [PoC repository](https://github.com/CptGibbon/CVE-2021-3156)

## Setup and Demo
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/19c4b766-7eb5-4d1b-9fb7-e40ce31fd4fb)

![1](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/2aa4a9c5-da2f-48d0-bf28-bd0ef941286d)

![2](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/4817dae9-9acb-4473-b693-55026caf5756)


![3](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/a34706c2-e374-4f83-ab6f-7edeaf4d99b7)

When we run the exploit command in the container, our privileges are elevated to the root user.
