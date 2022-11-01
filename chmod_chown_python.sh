#!/bin/bapy
#======================================
# File name:chmod_chown.py
# Author:liangliangSu
# Email:sll917@hotmail.com
# Date of writing:2022-10-06 01:42
#======================================
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
