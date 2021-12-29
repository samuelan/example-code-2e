#!/usr/bin/env python3
import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 4  # <1>


def probe(domain: str) -> tuple[str, bool]:  # <2>
    
    try:
        socket.getaddrinfo(domain, None)  # <4>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


def main() -> None:  # <5>
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() for name in names)  # <7>
    coros = [probe(domain) for domain in domains]  # <8>
    for coro in coros:  # <9>
        domain, found = coro  # <10>
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    main()  # <11>
