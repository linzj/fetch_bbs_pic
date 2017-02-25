import os, sys, os.path
import dns.message, dns.query, dns.rdtypes.IN.A

def doresolve(name):
    q = dns.message.make_query(name, 0x1)
    m = dns.query.udp(q, '8.8.8.8')
    if not m.answer:
        return None
    return (str(m.answer[0].items[0]))

class DNSResolver(object):
    def __init__(self):
        self.cache_ = {}

    def resolve(self, name):
        val = self.cache_.get(name)
        if val:
            return val
        val = doresolve(name)
        if not val:
            return None
        self.cache_[name] = val
        return val

