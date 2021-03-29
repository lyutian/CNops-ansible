#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: xxx
description:
    - "xxx".
options:
    state:
        description:
            - absent: xxx
            - present: xxx
        required: true
author:
    - Reynold Liu (lyutian623@gmail.com)
'''

EXAMPLES = '''
xxx
'''

RETURN = '''
message:
    description:
    type: str
'''


def run_module():
    module_args = dict(
        state=dict(
            type='str', required=True,
            choices=['absent', 'present']
        )
    )

    result = dict(
        changed=False,
        output='',
        error_message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    if module.check_mode:
        return result

    if module.params['state'] == 'absent':
        [_, stdout, _] = module.run_command('whereis kubeadm')
        if '/usr/bin/kubeadm' not in stdout:
            result['changed'] = False
        else:
            [_, stdout, stderr] = module.run_command('kubeadm reset -f')
            result['changed'] = True
            result['output'] = stdout
            result['error_message'] = stderr
    elif module.params['state'] == 'present':
        result['changed'] = False

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
