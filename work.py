import sys
import subprocess


cli_arguments= sys.argv
hostname_arg = cli_arguments[0]

ansible = "ansible"
inventory_file_path = os.getcwd() + filename
 

print(hostname_arg)

ansible_ping_output = subprocess.Popen([ansible, '-l', 'my_text_file.txt'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)