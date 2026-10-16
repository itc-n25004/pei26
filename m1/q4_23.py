ip_address = '192.168.3.1'
ip_spl = ip_address.split('.')
bin_exp = ''
for i in ip_spl:
    bin_exp += bin(int(i))[2:]+'.'
    print(bin_exp)
print(bin_exp[:-1])