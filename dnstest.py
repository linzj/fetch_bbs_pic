import os, sys, os.path
import dns.message, dns.query, dns.rdtypes.IN.A

def main():
    q = dns.message.make_query('wanimal1983.org', 0x1)
    m = dns.query.udp(q, '8.8.8.8')

    print(str(m.answer[0].items[0]))

if __name__ == '__main__':
    main()
