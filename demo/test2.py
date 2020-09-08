import paramiko

# 创建一个SSHClient对象
ssh = paramiko.SSHClient()
# 将信任的主机加到 host_allow 列表
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect("172.16.12.58", "22", "root", "5Flx$gSzk69Ckzw4&15WE%2vWn971U")

# 打印磁盘情况
# 执行df命令，结果放到 dfout 中，如果有错误将放到 dferr 中
dfout=ssh.exec_command('df')

print(list(dfout))
