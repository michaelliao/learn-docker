#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import psutil


def exec_ps():
    ps = [psutil.Process(p)for p in sorted(psutil.pids())]
    pss = [f'{p.pid} {p.name()}' for p in ps]
    return '\n'.join(pss)


def exec_ls():
    return '\n'.join(sorted(os.listdir('/')))


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        s = f'pid = {os.getpid()}'
        if self.path == '/ps':
            s = exec_ps()
        if self.path == '/ls':
            s = exec_ls()
        data = s.encode('utf-8')
        self.send_response(200)
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)
        self.wfile.flush()


def main():
    ip = '0.0.0.0'
    port = 8008
    with socketserver.TCPServer((ip, port), SimpleHandler) as httpd:
        print(f'start http server at {ip}:{port}...')
        httpd.serve_forever()


if __name__ == '__main__':
    main()
