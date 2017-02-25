import os, sys, os.path
import dns.message, dns.query, dns.rdtypes.IN.A

def main():
    name = 'wanimal1983.org'
    if len(sys.argv) > 1:
        name = sys.argv[1]
    q = dns.message.make_query(name, 0x1)
    m = dns.query.udp(q, '223.5.5.5')
    if m.answer:
        print(str(m.answer[0].items[0]))

if __name__ == '__main__':
    main()
