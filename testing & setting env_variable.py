# To set environmental variable navigate through
# control panel <System<advance system settings< environmental variable and then add variable.
# Why environmental variable is used?
# If you work in a project or work on scripts and need to put your secret credentials in that case
# you can use env. variable easily to prevent looking others into your personal info.
# Must restart pycharm after settings the environ variable.
import os

data_base_user = os.environ.get("DB_USER")
pasword = os.environ.get("DB_PASS")
print(data_base_user,pasword)



