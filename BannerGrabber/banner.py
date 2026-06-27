from scanner import grab_banner
from parser import parse_banner

banner=grab_banner(host,port)
info = parse.banner(banner)
print(info)
