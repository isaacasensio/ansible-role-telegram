# molecule/default/tests/test_default.py

def test_telegram_script_file(host):
    file = host.file('/usr/local/bin/telegram_message.sh')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o755