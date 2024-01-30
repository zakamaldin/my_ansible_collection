Role Name
=========
create_file_with_content

Role Variables
--------------

| Name           | Requred | Default Value | Description                        |
| -------------- | ------- | ------------- | -----------------------------------|
| `path` | True | /tmp/dir1/dir2/created_from_role_in_collection.txt | Полный путь до файла, который необходимо создать |
| `content` | True | hello | Содерэимое файла, которое юудет записано внутрь |

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: create_file_with_content }

License
-------

MIT

Author Information
------------------

Zakamaldin Andrey
