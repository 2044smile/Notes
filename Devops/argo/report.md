### Argo workflow bug report

#### failed to save outputs: Failed to establish pod watch: unknown (get pods)
- Argo 권한 문제
  - 해결방법
    - ```kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=<namespace>:default -n <namespace>```
  - Reference
    - https://github.com/argoproj/argo-events/issues/705
    - http://donghao.org/2020/06/05/failed-to-establish-pod-watch-in-argo/
    - [Rolebinding](https://www.mankier.com/1/kubectl-create-rolebinding, "kubectl create rolebinding example")
