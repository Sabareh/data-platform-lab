# CI and local registry plan

Status: selected architecture, not deployed. Updated 2026-10-14.

The source repository stays on GitHub. A self-hosted GitHub Actions runner and
a local container registry will share one supporting RHEL VM outside Kubernetes.
VM name, address, storage allocation and executor details remain to be configured.

```text
GitHub repository and Actions workflow
             |
             v
Supporting RHEL VM
  Runner: test code, build images with Podman
             |
             v
  Local registry: persist and serve built images
             |
             v
Kubernetes nodes: kubelet -> CRI-O -> application containers
```

The runner connects outbound to GitHub for jobs and pushes images locally. There
is no need to publish the registry to the internet. Cluster nodes independently
need network access, certificate trust and pull credentials for the registry.
GitHub stores source code; the registry stores built images. Publishing an image
does not deploy it: an explicit deployment workflow will update Kubernetes.

CNCF Distribution is the proposed initial registry, hosted with Podman and
persistent storage, HTTPS and authentication. Harbor remains an optional later
exercise. Co-location conserves laptop resources but couples registry availability
and security to the build VM; keep it running when nodes need image pulls.

Build pipelines should start with one concurrent job. Before registering a runner
for this public repository, restrict which workflows can execute on it: do not
run untrusted fork pull-request code on the persistent lab runner. Registry and
deployment credentials must stay outside Git, with narrowly scoped access.

GitLab Runner, Jenkins and Kubernetes-executor CI Pods were explored as learning
alternatives. They are not the selected local implementation. This is a personal
lab design, not a claim about any employer's deployed architecture.

Next: finish the Kubernetes foundation, then provision the supporting VM and
verify a local image push/pull before automating it through GitHub Actions.
