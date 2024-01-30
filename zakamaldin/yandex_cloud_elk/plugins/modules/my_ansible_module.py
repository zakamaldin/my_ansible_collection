#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from pathlib import Path

DOCUMENTATION = r'''
---
module: my_ansible_module.py

short_description: This is my module for creating fie with text inside.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my module for creating fie with your text inside on remote machine.

options:
    path:
        description: Remote's machine path, where you want to create a file.
        required: true
        type: str
    text:
        description: Text that will be placed inside file
        required: true
        type: str

author:
    - Zakamaldin Andrey (@zakamaldin)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  zakamaldin.my_ansible_collection.my_ansible_module:
    name: hello world

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    file = Path(module.params["path"])

    if not Path(module.params["path"]).is_file():
        file.parent.mkdir(exist_ok=True, parents=True)
        file.write_text(module.params["content"])
        result["changed"] = True
        result["content"] = module.params["content"]
        module.exit_json(**result)

    if not file.read_text() == module.params["content"]:
        file.write_text(module.params["content"])
        result["changed"] = True
        result["new_content"] = module.params["new_content"]
        module.exit_json(**result)
    
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()