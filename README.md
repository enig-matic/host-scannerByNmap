# host-scannerByNmap

# Nmap Host Discovery Scanner

A simple Python script that uses the `python-nmap` module to check whether a target host is up or cannot be detected on the network.

## Features

- Check whether a host is up or down.
- Accept a target IP address through command-line arguments.
- Use Nmap host discovery (`-sn`) without performing a port scan.
- Display the host status in the terminal.
- Include a `--no-dns` command-line option.

## Requirements

- Python 3
- Nmap
- `python-nmap` Python package

**. Install the Python module**

```bash
python3 -m pip install python-nmap
```

## Usage

Run the script using a target IP address:

```bash
python3 [file-name].py 192.168.1.1
```

Replace `192.168.1.1` with the IP address of a device you own or have permission to test.

### Example output

If the host is detected:

```text
Make sure that you Enter the Valid Host
<------------------------------------->
Host is up
```

If the host cannot be detected, the script may display:

```text
unable to find host, check your internet!
```

## Command-Line Arguments

| Argument | Description |
|---|---|
| `ip` | Required target IP address |
| `-h`, `--help` | Display help information |
| `-n`, `--no-dns` | Intended to indicate that DNS resolution should be disabled |

Display the help menu:

```bash
python3 demo.py --help
```

## How It Works

1. Imports `argparse` to handle command-line arguments.
2. Imports `nmap` to communicate with Nmap.
3. Accepts the target IP address from the user.
4. Runs Nmap with the `-sn` option for host discovery.
5. Checks whether Nmap detected the target.
6. Displays the reported host status.

## Important Note

The `--no-dns` option in the current code does not actually disable DNS resolution. Although the argument is defined, its value is not used in the scan. To disable DNS resolution, pass `-n` to Nmap:

```python
scanner.scan(hosts=ip, arguments='-sn -n')
```

Also, a host that does not respond to discovery probes is not necessarily offline. Firewalls and network configurations can affect detection.

## Disclaimer

This tool is intended for educational purposes and authorized network testing only. Scan only systems and networks you own or have explicit permission to test.

## Author

Created as a Python and Nmap learning project.
