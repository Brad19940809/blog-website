#!/usr/bin/env bash

set password 586341
spawn ssh root@192.168.1.102
expect "*password:"
send "$password\r"
