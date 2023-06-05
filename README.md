Telegram
=========

Creates a shell script to send messages to Telegram.

You will be able to send a Telegram message by runing the following command:

```
./telegram_message.sh "token" "chat_id" "message"

```


Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

```
telegram_host_path: "/usr/local/bin"
```
The path where the telegram_message.sh script will be installed.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - iasensio.telegram

License
-------

MIT

