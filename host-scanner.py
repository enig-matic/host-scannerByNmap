import argparse
import nmap

scanner = nmap.PortScanner()

def main():

    print("Make sure that you Enter the Valid Host")
    print("<------------------------------------->")

    parse = argparse.ArgumentParser(description='Nmap Scanner')
    parse.add_argument('ip',help="Enter Target IP Address")
    parse.add_argument('-n','--no-dns',action='store_true',default=True,help='block sending dns information')
    
    args = parse.parse_args()
    
    ip = args.ip
    
    scanner.scan(hosts=ip,arguments='-sn -n')
    
    if ip in scanner.all_hosts():
        stat = scanner[ip].state()
    
        if stat == 'up':
            print(f"\nHost is {stat}")
    
        else:
            print(f"Host is {stat}")
    else :
        print("unable to find host, check your internet!")
    

if __name__ == "__main__":
    main()
