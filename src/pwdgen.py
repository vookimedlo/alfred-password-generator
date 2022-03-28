#!/opt/homebrew/bin/python3

import json
import os
import sys
from functools import reduce
from subprocess import Popen, PIPE

length = sys.argv[1]
#length = "10"
alfreditems = {"items": []}

def generate_password(*args):
    arguments = ["/opt/homebrew/bin/pwgen"] + list(args) + [length, "1"]
    process = Popen(arguments, stdout=PIPE)
    (output, err) = process.communicate()
    exitCode = process.wait()
    return (exitCode, output, err)

def create_alfred_item(alfreditems, uid, title, subtitle, autocomplete, arg):
    alfreditems['items'].append({
        "uid": uid,
        "title": title,
        "subtitle": subtitle,
        "autocomplete": autocomplete,
        "arg": arg,
        })

def populate_menu(alfreditems, title, *password_args):
    (exitCode, output, err) = generate_password(*password_args)

    if exitCode == 0:
        output = (bytes(output).replace(b'\n', b'')).decode("utf-8")
        create_alfred_item(alfreditems, title, title, output, title, output)
        return True
    return False

passwords = [["Alphanumeric password", "-snc"],
             ["Alphanumeric password with special characters", "-sncy"],
             ["Numeric password", "-A", "--remove-chars", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]]

if reduce((lambda x, y: x and y), map(lambda x: populate_menu(alfreditems, *x), passwords)) == False:
    alfreditems = {"items": []}
    create_alfred_item(alfreditems, 1, "Password Generator", "Failure! Cannot generate a password!", "", "")

dump = json.dumps({'items': alfreditems['items']}, indent=4)
sys.stdout.write(dump)
