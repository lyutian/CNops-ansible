### Issues:
- [x] 使用172.172.0.0/16 for calico
- [x] 使用ipvs
    ```
    # yum -y install ipvsadm ipvsset
    # cat > /etc/sysconfig/modules/ipvs.modules <<EOF
    modprobe -- ip_vs
    modprobe -- ip_vs_rr
    modprobe -- ip_vs_wrr
    modprobe -- ip_vs_sh
    modprobe -- nf_conntrack_ipv4
    EOF
    # chmod 755 /etc/sysconfig/modules/ipvs.modules && bash /etc/sysconfig/modules/ipvs.modules && lsmod | grep -e ip_vs -e nf_conntrack_ipv4
    ```

- [x] 添加如下配置到kubeadm.conf
    ```
    ---
    apiVersion: kubelet.config.k8s.io/v1beta1
    kind: KubeletConfiguration
    cgroupDriver: systemd

    ---
    apiVersion: kubeproxy.config.k8s.io/v1alpha1
    kind:  KubeProxyConfiguration
    mode: ipvs
    ```

- [ ] 修改kubeadm.conf
    ```
    controlPlaneEndpoint: "master01:6443"
    ```

- [x] 去掉taint
    ```
    kubectl taint nodes --all node-role.kubernetes.io/master-
    ```

### Temporary notice
```
--------------------------
yum install iscsi-initiator-utils -y
sudo systemctl enable --now iscsid
systemctl status iscsid
kubeclt apply -f openebs-operator.yaml
kubectl get bd -n openebs
kubectl apply -f cstor-pool1-config.yaml
kubectl get spc
kubectl get csp

kubectl apply -f openebs-sc-rep3.yaml
kubectl get sc
kubectl describe sc openebs-sc-statefulset

kubectl apply -f my_openebs_pvc.yaml

--------------------------
[root@master01 ~]# docker images
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
openebs/cstor-pool-mgmt              2.8.0               f44b398c7e88        3 days ago          892MB
openebs/admission-server             2.8.0               757ad59d2f77        3 days ago          208MB
openebs/openebs-k8s-provisioner      2.8.0               ab2025c4a1cf        3 days ago          211MB
openebs/snapshot-provisioner         2.8.0               7c5f15f1f851        3 days ago          74.2MB
openebs/snapshot-controller          2.8.0               653d7952c3a7        3 days ago          73.2MB
openebs/cstor-pool                   2.8.0               60750fa7a35d        3 days ago          845MB
openebs/node-disk-manager            1.4.0               9578c640a01c        3 days ago          120MB
openebs/node-disk-operator           1.4.0               421d167b9ce6        3 days ago          117MB
openebs/m-exporter                   2.8.0               ea5de713e188        3 days ago          855MB
calico/node                          v3.18.1             50b52cdadbcf        5 weeks ago         172MB
calico/pod2daemon-flexvol            v3.18.1             3994c62982cc        5 weeks ago         21.7MB
calico/cni                           v3.18.1             21fdaa2fccee        5 weeks ago         131MB
calico/kube-controllers              v3.18.1             a274b7fd57f5        5 weeks ago         53.4MB
rancher/fleet-agent                  v0.3.4              4c6ca93b4785        6 weeks ago         155MB
k8s.gcr.io/kube-proxy                v1.20.4             c29e6c583067        8 weeks ago         118MB
k8s.gcr.io/kube-controller-manager   v1.20.4             0a41a1414c53        8 weeks ago         116MB
k8s.gcr.io/kube-apiserver            v1.20.4             ae5eb22e4a9d        8 weeks ago         122MB
k8s.gcr.io/kube-scheduler            v1.20.4             5f8cb769bd73        8 weeks ago         47.3MB
k8s.gcr.io/etcd                      3.4.13-0            0369cf4303ff        7 months ago        253MB
k8s.gcr.io/coredns                   1.7.0               bfe3a36ebd25        10 months ago       45.2MB
k8s.gcr.io/pause                     3.2                 80d28bedfe5d        14 months ago       683kB
```