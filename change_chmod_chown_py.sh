#!/bin/bash
# **********************************************************
# * Author : liangliangSu
# * Email : sll917@hotmail.com
# * Create time : 2022-11-01 23:08
# * Filename : change_chmod_chown_py.sh
# **********************************************************
chmod -R u+rwx *.py */*.py
chmod u+rwx */ 
chmod g-wx *.py && chmod g+r *.py
chmod -R g-wx */*.py && chmod g+r */*.py
chmod g-wx */ 
chmod o-wx *.py && chmod o+r *.py
chmod -R o-wx */*.py && chmod o+r */*.py
chmod o-wx */ 
chown -R sll:sll *.py */*.py
chown sll:sll */  

