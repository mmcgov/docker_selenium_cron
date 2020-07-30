#!/bin/bash

printenv | grep -v "email_1" >>/etc/environment
printenv | grep -v "password_1" >>/etc/environment

exec $@
