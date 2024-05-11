# CVE-2020-28502

This affects the package xmlhttprequest before 1.7.0; all versions of package xmlhttprequest-ssl. Provided requests are sent synchronously (async=False on xhr.open), malicious user input flowing into xhr.send could result in arbitrary code being injected and run. [CVE-2020-28502](https://nvd.nist.gov/vuln/detail/CVE-2020-28502)

## Setup and Demo

The PoC from s-index's [PoC repository](https://github.com/s-index/CVE-2020-28502)

## Setup and Demo

The image namzoyatuk/xmlhttprequest-cve7 built by Dockerfile provided in the [PoC repository](https://github.com/s-index/CVE-2020-28502)

Deployment to Kubernetes can be done by executing below commands:

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

We can see the pod and service are up and running
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/2d2b780d-d8bb-4379-a263-37c3ea5f64a7)
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/222d34f0-a68a-4db2-8520-9c79d6f32cdb)
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/7e287ba4-7d91-413a-a2cf-da425aefa40f)

### Reverse Shell

Listen client
```
nc -l 8888
```
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/a05c7622-1496-41e4-9e7e-67e2f8be8d4c)



Submit Payload
![Screenshot from 2024-05-11 18-36-40](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/47a7c1e4-fe87-417f-ae8d-4e2a730cd8e1)

After sending the request we are now inside the container.
![image](https://github.com/turkbera/Ceng489-Kuberenetes-Attack-Scenarios/assets/54873326/0b56d675-aed4-4039-9281-9f81d5317c86)



