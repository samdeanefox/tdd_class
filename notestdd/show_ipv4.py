''' Goal:  Learn to parse column-oriented text intended for humans
           such as the output for the IOS CLI:

           # show ipv4 int bri

    Key Lesson:  Parsing column-oriented text is not fast, not easy, not fun, and not reliable! 

    * The case can be switched between "up", "Up", and "UP".
    * Fields can have missing values which confounds str.split() and unpacking.
    * Field values can contain spaces  which confounds str.split() and unpacking.
    * Column alignment can shift between consecutive runs.

    Main strategy:  Figure-out how a human would correctly parse the data,
                    and then teach the computer to do the same.

    Anti-Nike rule: Just don't do it!  This data was intended for humans.
                    It was not intended to be parsed reliably.
                    Instead, get better data:  JSON, CSV, XML, YAML, Pickle, Marshal, etc.

'''

with open('notestdd/ipv4_int_bri.txt') as f:
    header = next(f)
    in_start = header.find('Interface')
    ip_start = header.find('IP-Address')
    st_start = header.find('Status')
    pr_start = header.find('Protocol')
    for line in f:
        # line = line.rstrip()
        # interface, ipaddr, status, protocol = line.split()
        interface = line[in_start: ip_start].rstrip()
        ipaddr = line[ip_start: st_start].rstrip()
        status = line[st_start: pr_start].rstrip()
        protocol = line[pr_start:].rstrip()
        
        if status.lower() == 'up':
            print(f'{ipaddr:15s} {interface}')
 
