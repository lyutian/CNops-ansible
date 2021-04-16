## Notice
- need `root` user for all the nodes.
- the `master_join.sh` and `worker_join.sh` are only valid in 24 hours.

## Setup ansible environment
- install pip
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get_pip.py
    ```
- install requirements package
    ```
    pip install -r requirements.txt
    ```

## Edit config files
- `inventory/hosts.yaml`
  - host ip and credential
  - NIC, network interface card name
- `inventory/group_vars/all.yaml`
  - repository source
  - virtural IP
  - k8s version

## Run script
- clean up environment
    ```
    ansible-playbook k8s-cleanup.yaml
    ```
- setup HA kubernetes
    ```
    ansible-playbook k8s-HA-cluster-setup.yaml
    ```
> Tips:
>   1. playbook can be re-run if it failed before.
>   2. you can start at specific step by adding `--start-at-task="push master_join script"`
>   3. add `-vvv` to get more debug information.