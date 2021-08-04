#!/user/bin/python3

#connects to all ssh severs listed
import pexpect

#connect and login
child = pexpect.spawn('ssh agent01@10.0.2.4')
child.expect('password:')
child.sendline('517625')
print('logged in')

#run the ip addr command and logs ip
child.expect('/[.*/]/$')
child.sendline('ip addr')
child.expect('.*')
print(child.before)

#logs out of remote shell
child.sendline('exit')
print('logged out')