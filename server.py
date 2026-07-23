#!/usr/bin/env python3
"""
CyberOps.py - A comprehensive cyber operations tool with graphics using only Python built-in libraries
Compatible with NeilOS cyber operations
"""

import socket
import struct
import os
import sys
import time
import json
import hashlib
import base64
import random
import string
import subprocess
import threading
import queue
import re
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlparse
import ipaddress
import platform
import getpass

# Graphics imports (Python built-in)
try:
    import turtle
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox
except ImportError:
    print("Warning: tkinter not available. GUI features will be disabled.")
    turtle = None
    tk = None

class CyberGraphics:
    """Graphics utilities for cyber operations"""
    
    @staticmethod
    def draw_network_animation(target_ip, ports):
        """Draw network scanning animation using turtle"""
        if not turtle:
            return
        
        screen = turtle.Screen()
        screen.title("CyberOps Network Scan")
        screen.bgcolor("black")
        screen.setup(800, 600)
        
        # Create turtle for drawing
        t = turtle.Turtle()
        t.speed(0)
        t.color("cyan")
        
        # Draw title
        t.penup()
        t.goto(-200, 250)
        t.write(f"Scanning: {target_ip}", font=("Arial", 16, "bold"))
        
        # Draw network nodes
        node_positions = []
        t.penup()
        for i in range(8):
            x = -300 + (i * 80)
            y = random.randint(-100, 100)
            t.goto(x, y)
            t.pendown()
            t.circle(20)
            t.penup()
            node_positions.append((x, y))
            t.goto(x, y - 30)
            t.write(f"Node {i+1}", align="center", font=("Arial", 8))
        
        # Draw connections with port information
        t.color("lime")
        for port in ports[:20]:  # Show first 20 ports
            if port % 2 == 0:  # Even ports are "open"
                idx = port % len(node_positions)
                x, y = node_positions[idx]
                t.goto(x, y + 25)
                t.pendown()
                t.circle(15, None, 20)
                t.penup()
                t.goto(x, y + 40)
                t.write(f"Port {port}", align="center", font=("Arial", 7))
        
        # Animated scanning effect
        t.color("red")
        for _ in range(5):
            for x, y in node_positions:
                t.goto(x, y)
                t.dot(25, "yellow")
                time.sleep(0.1)
                t.dot(20, "black")
        
        t.hideturtle()
        screen.exitonclick()
    
    @staticmethod
    def visualize_hash(text, hash_value):
        """Visualize hash using turtle"""
        if not turtle:
            return
        
        screen = turtle.Screen()
        screen.title("Hash Visualization")
        screen.bgcolor("black")
        screen.setup(800, 600)
        
        t = turtle.Turtle()
        t.speed(0)
        t.color("green")
        
        # Display text
        t.penup()
        t.goto(-300, 200)
        t.write(f"Original: {text[:50]}", font=("Arial", 12))
        
        # Convert hash to binary and draw pattern
        binary = bin(int(hash_value, 16))[2:]
        t.goto(-300, 100)
        
        x, y = -300, 100
        for i, bit in enumerate(binary[:2000]):  # Limit for performance
            if i % 100 == 0:
                x = -300
                y -= 20
            if bit == '1':
                t.pendown()
                t.color("lime")
                t.goto(x, y)
                t.dot(3)
            else:
                t.penup()
                t.goto(x, y)
            x += 2
        
        t.hideturtle()
        screen.exitonclick()
    
    @staticmethod
    def draw_cyber_radar():
        """Draw a cyber radar visualization"""
        if not turtle:
            return
        
        screen = turtle.Screen()
        screen.title("Cyber Defense Radar")
        screen.bgcolor("black")
        screen.setup(800, 600)
        
        t = turtle.Turtle()
        t.speed(0)
        t.color("green")
        
        # Draw radar circles
        for radius in [50, 100, 150, 200, 250]:
            t.penup()
            t.goto(0, -radius)
            t.pendown()
            t.circle(radius)
        
        # Draw crosshairs
        t.penup()
        t.goto(0, -250)
        t.pendown()
        t.goto(0, 250)
        t.penup()
        t.goto(-250, 0)
        t.pendown()
        t.goto(250, 0)
        
        # Animated scanning line
        for angle in range(0, 360, 5):
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color("cyan")
            t.setheading(angle)
            t.forward(250)
            t.penup()
            t.goto(0, 0)
            time.sleep(0.02)
            # Clear previous line
            t.pendown()
            t.color("black")
            t.setheading(angle)
            t.forward(250)
        
        t.hideturtle()
        screen.exitonclick()
    
    @staticmethod
    def draw_cyber_art():
        """Draw cyber-themed art with turtle"""
        if not turtle:
            return
        
        screen = turtle.Screen()
        screen.title("Cyber Art")
        screen.bgcolor("black")
        screen.setup(800, 600)
        screen.colormode(255)
        
        t = turtle.Turtle()
        t.speed(0)
        
        # Create cyber pattern
        colors = [(0, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 0)]
        
        for i in range(100):
            t.color(colors[i % 4])
            t.forward(i * 2)
            t.left(89)
            t.pendown()
            
            # Draw small hexagons for cyber look
            for _ in range(6):
                t.forward(20)
                t.left(60)
            t.penup()
            t.forward(10)
            
            if i % 10 == 0:
                # Draw digital rain effect
                for j in range(10):
                    x = random.randint(-300, 300)
                    y = random.randint(-200, 200)
                    t.goto(x, y)
                    t.write(chr(random.randint(33, 126)), font=("Arial", 10, "bold"))
        
        t.hideturtle()
        screen.exitonclick()

class CyberGUIConsole:
    """GUI Console for cyber operations using tkinter"""
    
    def __init__(self):
        if not tk:
            print("tkinter not available. GUI mode disabled.")
            return
        
        self.root = tk.Tk()
        self.root.title("CyberOps GUI Console")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0a0a0a")
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Cyber.TFrame', background='#0a0a0a')
        style.configure('Cyber.TButton', 
                       background='#00ff00',
                       foreground='black',
                       borderwidth=2,
                       focuscolor='none')
        style.map('Cyber.TButton',
                 background=[('active', '#00cc00')])
        
        self.setup_gui()
        self.cyber_ops = CyberOps()
        
    def setup_gui(self):
        """Setup the GUI layout"""
        # Main container
        main_frame = ttk.Frame(self.root, style='Cyber.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(main_frame, 
                              text="=== CYBEROPS v1.0 ===",
                              fg="#00ff00",
                              bg="#0a0a0a",
                              font=("Courier", 18, "bold"))
        title_label.pack(pady=10)
        
        # Top frame for controls
        control_frame = ttk.Frame(main_frame, style='Cyber.TFrame')
        control_frame.pack(fill=tk.X, pady=5)
        
        # Left controls
        left_frame = ttk.Frame(control_frame, style='Cyber.TFrame')
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Command entry
        cmd_label = tk.Label(left_frame, text="Command:", 
                            fg="#00ff00", bg="#0a0a0a", font=("Courier", 10))
        cmd_label.pack(side=tk.LEFT)
        
        self.cmd_var = tk.StringVar()
        self.cmd_entry = tk.Entry(left_frame, 
                                 textvariable=self.cmd_var,
                                 bg="#1a1a1a",
                                 fg="#00ff00",
                                 font=("Courier", 10),
                                 width=40)
        self.cmd_entry.pack(side=tk.LEFT, padx=5)
        self.cmd_entry.bind('<Return>', self.execute_command)
        
        # Execute button
        self.exec_btn = tk.Button(left_frame, 
                                 text="EXECUTE",
                                 bg="#00ff00",
                                 fg="black",
                                 font=("Courier", 10, "bold"),
                                 command=self.execute_command)
        self.exec_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = tk.Button(left_frame,
                                  text="CLEAR",
                                  bg="#ff4444",
                                  fg="white",
                                  font=("Courier", 10, "bold"),
                                  command=self.clear_output)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Graphics button
        self.graphics_btn = tk.Button(left_frame,
                                     text="GRAPHICS",
                                     bg="#4444ff",
                                     fg="white",
                                     font=("Courier", 10, "bold"),
                                     command=self.show_graphics_menu)
        self.graphics_btn.pack(side=tk.LEFT, padx=5)
        
        # Output area
        output_frame = ttk.Frame(main_frame, style='Cyber.TFrame')
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(output_frame,
                                                    bg="#0a0a0a",
                                                    fg="#00ff00",
                                                    font=("Courier", 10),
                                                    insertbackground="#00ff00",
                                                    wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_label = tk.Label(main_frame,
                                    text="Ready",
                                    fg="#00ff00",
                                    bg="#0a0a0a",
                                    font=("Courier", 9))
        self.status_label.pack(pady=5)
        
        # Custom commands quick buttons
        quick_frame = ttk.Frame(main_frame, style='Cyber.TFrame')
        quick_frame.pack(fill=tk.X, pady=5)
        
        quick_commands = [
            ("Scan", "scan 127.0.0.1 1 100"),
            ("Ping", "ping google.com"),
            ("Hash", "hash test sha256"),
            ("DNS", "dns google.com"),
            ("Info", "system"),
            ("Gen Pass", "genpass 16"),
        ]
        
        for text, cmd in quick_commands:
            btn = tk.Button(quick_frame,
                           text=text,
                           bg="#003300",
                           fg="#00ff00",
                           font=("Courier", 8),
                           command=lambda c=cmd: self.quick_command(c))
            btn.pack(side=tk.LEFT, padx=2)
    
    def quick_command(self, command):
        """Execute a quick command"""
        self.cmd_var.set(command)
        self.execute_command()
    
    def execute_command(self, event=None):
        """Execute a command from the GUI"""
        cmd = self.cmd_var.get().strip()
        if not cmd:
            return
        
        self.output_text.insert(tk.END, f"\n$ {cmd}\n", "command")
        self.output_text.see(tk.END)
        
        # Parse command
        parts = cmd.split()
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1:]
        
        try:
            if command == "scan":
                target = args[0] if args else "127.0.0.1"
                start = int(args[1]) if len(args) > 1 else 1
                end = int(args[2]) if len(args) > 2 else 100
                result = self.cyber_ops.network_scan(target, start, end)
                self.display_result(result)
                
            elif command == "fastscan":
                target = args[0] if args else "127.0.0.1"
                start = int(args[1]) if len(args) > 1 else 1
                end = int(args[2]) if len(args) > 2 else 100
                result = self.cyber_ops.fast_port_scan(target, start, end)
                self.display_result(result)
                
            elif command == "ping":
                target = args[0] if args else "google.com"
                count = int(args[1]) if len(args) > 1 else 4
                self.cyber_ops.ping_host(target, count)
                
            elif command == "hash":
                text = args[0] if args else "test"
                algo = args[1] if len(args) > 1 else "sha256"
                result = self.cyber_ops.hash_string(text, algo)
                self.display_result(result)
                
            elif command == "dns":
                domain = args[0] if args else "google.com"
                result = self.cyber_ops.dns_enumeration(domain)
                self.display_result(result)
                
            elif command == "system":
                result = self.cyber_ops.get_system_info()
                self.display_result(result)
                
            elif command == "genpass":
                length = int(args[0]) if args else 16
                result = self.cyber_ops.generate_password(length)
                self.display_result(result)
                
            elif command == "geolocate":
                ip = args[0] if args else "8.8.8.8"
                result = self.cyber_ops.network_geolocation(ip)
                self.display_result(result)
                
            elif command == "url":
                url = args[0] if args else "https://example.com"
                result = self.cyber_ops.fetch_url(url)
                self.display_result(f"Fetched {len(result) if result else 0} bytes")
                
            elif command == "encrypt":
                text = args[0] if args else "test"
                if len(args) > 1 and args[1] == "xor":
                    key = args[2] if len(args) > 2 else "key"
                    result = self.cyber_ops.xor_encrypt(text, key)
                else:
                    shift = int(args[1]) if len(args) > 1 else 3
                    result = self.cyber_ops.encrypt_caesar(text, shift)
                self.display_result(result)
                
            elif command == "decrypt":
                text = args[0] if args else "whvw"
                if len(args) > 1 and args[1] == "xor":
                    key = args[2] if len(args) > 2 else "key"
                    result = self.cyber_ops.xor_decrypt(text, key)
                else:
                    shift = int(args[1]) if len(args) > 1 else 3
                    result = self.cyber_ops.decrypt_caesar(text, shift)
                self.display_result(result)
                
            elif command == "knock":
                host = args[0] if args else "127.0.0.1"
                ports = [int(p) for p in args[1:]] if len(args) > 1 else [80, 443, 22]
                result = self.cyber_ops.port_knocking(host, ports)
                self.display_result(result)
                
            elif command == "graphics":
                self.show_graphics_menu()
                
            elif command == "clear":
                self.clear_output()
                
            elif command == "help":
                self.show_help()
                
            else:
                self.output_text.insert(tk.END, f"Unknown command: {command}\n")
                
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {e}\n")
        
        self.cmd_var.set("")
        self.output_text.see(tk.END)
        self.status_label.config(text=f"Last command: {cmd}")
    
    def display_result(self, result):
        """Display a result in the output"""
        if result is None:
            self.output_text.insert(tk.END, "No results\n")
            return
        
        if isinstance(result, dict):
            self.output_text.insert(tk.END, json.dumps(result, indent=2) + "\n")
        elif isinstance(result, list):
            for item in result:
                if isinstance(item, dict):
                    self.output_text.insert(tk.END, json.dumps(item) + "\n")
                else:
                    self.output_text.insert(tk.END, str(item) + "\n")
        else:
            self.output_text.insert(tk.END, str(result) + "\n")
    
    def show_graphics_menu(self):
        """Show graphics options"""
        if not turtle:
            messagebox.showinfo("Graphics Unavailable", 
                               "Turtle graphics not available. Install tkinter.")
            return
        
        graphics_window = tk.Toplevel(self.root)
        graphics_window.title("Cyber Graphics")
        graphics_window.geometry("400x400")
        graphics_window.configure(bg="#0a0a0a")
        
        label = tk.Label(graphics_window,
                        text="Select Graphics Animation",
                        fg="#00ff00",
                        bg="#0a0a0a",
                        font=("Courier", 14, "bold"))
        label.pack(pady=20)
        
        graphics_options = [
            ("Network Scan Animation", self.run_network_anim),
            ("Hash Visualization", self.run_hash_vis),
            ("Cyber Radar", self.run_radar),
            ("Cyber Art", self.run_cyber_art),
        ]
        
        for text, command in graphics_options:
            btn = tk.Button(graphics_window,
                           text=text,
                           bg="#003300",
                           fg="#00ff00",
                           font=("Courier", 10),
                           command=command,
                           width=30,
                           height=2)
            btn.pack(pady=5)
    
    def run_network_anim(self):
        """Run network animation in separate thread"""
        threading.Thread(target=lambda: CyberGraphics.draw_network_animation("127.0.0.1", [22, 80, 443, 3306, 8080]), daemon=True).start()
    
    def run_hash_vis(self):
        """Run hash visualization"""
        text = "CyberOps Security"
        hash_val = hashlib.sha256(text.encode()).hexdigest()
        threading.Thread(target=lambda: CyberGraphics.visualize_hash(text, hash_val), daemon=True).start()
    
    def run_radar(self):
        """Run cyber radar"""
        threading.Thread(target=CyberGraphics.draw_cyber_radar, daemon=True).start()
    
    def run_cyber_art(self):
        """Run cyber art"""
        threading.Thread(target=CyberGraphics.draw_cyber_art, daemon=True).start()
    
    def show_help(self):
        """Display help message"""
        help_text = """
=== CYBEROPS HELP ===

Commands:
  scan <target> <start_port> <end_port>
  fastscan <target> <start_port> <end_port>
  ping <host> [count]
  hash <text> [algorithm]
  dns <domain>
  system
  genpass [length]
  geolocate <ip>
  url <url>
  encrypt <text> [shift]
  encrypt <text> xor <key>
  decrypt <text> [shift]
  decrypt <text> xor <key>
  knock <host> <ports...>
  graphics
  clear
  help

Examples:
  scan 192.168.1.1 1 1000
  ping google.com
  hash "Hello World" sha256
  genpass 20
  encrypt "secret" 5
  encrypt "secret" xor key
  knock 127.0.0.1 80 443 22
"""
        self.output_text.insert(tk.END, help_text + "\n")
    
    def clear_output(self):
        """Clear the output text"""
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "=== CyberOps Console ===\nType 'help' for commands\n")
    
    def run(self):
        """Run the GUI"""
        self.clear_output()
        self.root.mainloop()

class CyberOps:
    """Main class containing all cyber operations"""
    
    def __init__(self):
        self.version = "1.0"
        self.author = "NeilOS Cyber Suite"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.results = {}
        
    def print_banner(self):
        """Display cyber operations banner with ASCII art"""
        banner = f"""
╔══════════════════════════════════════════════════════════╗
║     CyberOps v{self.version} - NeilOS Cyber Suite          ║
║     {self.timestamp}                                  ║
╚══════════════════════════════════════════════════════════╝
        """
        print(banner)
        
        # ASCII art banner
        ascii_art = """
        ╔═══════════════════════════════════════╗
        ║   ██████╗██╗   ██╗██████╗ ███████╗  ║
        ║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝  ║
        ║  ██║      ╚████╔╝ ██████╔╝█████╗    ║
        ║  ██║       ╚██╔╝  ██╔══██╗██╔══╝    ║
        ║  ╚██████╗   ██║   ██████╔╝███████╗  ║
        ║   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝  ║
        ╚═══════════════════════════════════════╝
        """
        print(ascii_art)
    
    # ============ NETWORK OPERATIONS ============
    
    def network_scan(self, target, start_port=1, end_port=1024, timeout=1):
        """Scan network ports on a target host"""
        print(f"\n[*] Scanning {target} ports {start_port}-{end_port}")
        open_ports = []
        
        try:
            target_ip = socket.gethostbyname(target)
            print(f"[*] Resolved to: {target_ip}")
            
            # Show animated progress
            for port in range(start_port, end_port + 1):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((target_ip, port))
                    if result == 0:
                        service = self._get_service_name(port)
                        open_ports.append({"port": port, "service": service, "status": "open"})
                        print(f"[+] Port {port} open - {service}")
                    sock.close()
                except Exception:
                    continue
                    
        except socket.gaierror:
            print(f"[-] Could not resolve hostname: {target}")
            return None
            
        self.results['network_scan'] = {
            'target': target,
            'ip': target_ip if 'target_ip' in locals() else 'unknown',
            'open_ports': open_ports,
            'scan_range': f"{start_port}-{end_port}"
        }
        return open_ports
    
    def _get_service_name(self, port):
        """Get service name for common ports"""
        services = {
            20: 'FTP-data', 21: 'FTP', 22: 'SSH', 23: 'Telnet',
            25: 'SMTP', 53: 'DNS', 80: 'HTTP', 110: 'POP3',
            111: 'RPCbind', 135: 'MSRPC', 139: 'NetBIOS', 143: 'IMAP',
            443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 8080: 'HTTP-Alt'
        }
        return services.get(port, 'Unknown')
    
    def dns_enumeration(self, domain):
        """Perform DNS enumeration"""
        print(f"\n[*] DNS Enumeration for: {domain}")
        dns_info = {}
        
        try:
            # A record
            ip = socket.gethostbyname(domain)
            dns_info['A'] = ip
            print(f"[+] A Record: {ip}")
            
            # Reverse DNS
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                dns_info['PTR'] = hostname
                print(f"[+] PTR Record: {hostname}")
            except socket.herror:
                print("[-] No PTR record found")
            
            # MX records (simulated via socket)
            try:
                import re
                mx_records = self._simulate_mx_lookup(domain)
                if mx_records:
                    dns_info['MX'] = mx_records
                    print(f"[+] MX Records: {mx_records}")
            except:
                pass
                
        except socket.gaierror:
            print(f"[-] Could not resolve: {domain}")
            
        self.results['dns_enum'] = dns_info
        return dns_info
    
    def _simulate_mx_lookup(self, domain):
        """Simulate MX lookup using socket (simplified)"""
        mx_records = []
        try:
            mail_servers = [f"mail.{domain}", f"smtp.{domain}", f"mx1.{domain}"]
            for server in mail_servers:
                try:
                    socket.gethostbyname(server)
                    mx_records.append(server)
                except:
                    continue
        except:
            pass
        return mx_records if mx_records else None
    
    def ping_host(self, hostname, count=4):
        """Ping a host using system ping command"""
        print(f"\n[*] Pinging {hostname}")
        
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, str(count), hostname]
        
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            print(output)
            self.results['ping'] = {
                'host': hostname,
                'status': 'success',
                'output': output
            }
            return True
        except subprocess.CalledProcessError as e:
            print(f"[-] Ping failed: {e.output}")
            self.results['ping'] = {
                'host': hostname,
                'status': 'failed',
                'output': e.output if hasattr(e, 'output') else str(e)
            }
            return False
    
    # ============ CRYPTOGRAPHY OPERATIONS ============
    
    def hash_string(self, text, algorithm='sha256'):
        """Generate hash of a string"""
        print(f"\n[*] Hashing text with {algorithm.upper()}")
        
        if algorithm == 'md5':
            hash_obj = hashlib.md5(text.encode())
        elif algorithm == 'sha1':
            hash_obj = hashlib.sha1(text.encode())
        elif algorithm == 'sha256':
            hash_obj = hashlib.sha256(text.encode())
        elif algorithm == 'sha512':
            hash_obj = hashlib.sha512(text.encode())
        else:
            print(f"[-] Unknown algorithm: {algorithm}")
            return None
        
        hash_result = hash_obj.hexdigest()
        print(f"[+] {algorithm.upper()}: {hash_result}")
        
        if 'hashes' not in self.results:
            self.results['hashes'] = {}
        self.results['hashes'][algorithm] = hash_result
        return hash_result
    
    def base64_encode(self, text):
        """Encode text to base64"""
        encoded = base64.b64encode(text.encode()).decode()
        print(f"\n[*] Base64 Encode: {encoded}")
        self.results['base64_encode'] = encoded
        return encoded
    
    def base64_decode(self, encoded_text):
        """Decode base64 text"""
        try:
            decoded = base64.b64decode(encoded_text).decode()
            print(f"\n[*] Base64 Decode: {decoded}")
            self.results['base64_decode'] = decoded
            return decoded
        except:
            print("[-] Invalid base64 string")
            return None
    
    def generate_password(self, length=16, include_special=True):
        """Generate a strong password"""
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n[*] Generated Password: {password}")
        self.results['generated_password'] = password
        
        # Visualize password strength
        strength = self._check_password_strength(password)
        print(f"[+] Strength: {strength}")
        return password
    
    def _check_password_strength(self, password):
        """Check password strength"""
        score = 0
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'\d', password):
            score += 1
        if re.search(r'[!@#$%^&*()_+-=]', password):
            score += 1
        
        if score >= 6:
            return "VERY STRONG"
        elif score >= 4:
            return "STRONG"
        elif score >= 3:
            return "MEDIUM"
        else:
            return "WEAK"
    
    # ============ SYSTEM OPERATIONS ============
    
    def get_system_info(self):
        """Gather system information"""
        print("\n[*] Gathering System Information")
        print("=" * 40)
        
        info = {
            'system': platform.system(),
            'node': platform.node(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': sys.version,
            'platform': platform.platform(),
            'hostname': socket.gethostname(),
            'user': getpass.getuser(),
            'current_time': datetime.now().isoformat()
        }
        
        for key, value in info.items():
            print(f"[+] {key}: {value}")
        
        print("=" * 40)
        self.results['system_info'] = info
        return info
    
    def get_network_interfaces(self):
        """Get network interface information"""
        print("\n[*] Network Interface Information")
        print("=" * 40)
        
        interfaces = []
        if platform.system().lower() == 'windows':
            try:
                output = subprocess.check_output(['ipconfig'], universal_newlines=True)
                print(output)
                interfaces = [{'output': output}]
            except:
                print("[-] Failed to get network interface information")
        else:
            try:
                import fcntl
                interface_names = self._get_linux_interfaces()
                for iface in interface_names:
                    info = self._get_linux_interface_info(iface)
                    if info:
                        interfaces.append(info)
                        print(f"[+] {iface}: {info}")
            except:
                try:
                    output = subprocess.check_output(['ifconfig'], universal_newlines=True)
                    print(output)
                    interfaces = [{'output': output}]
                except:
                    print("[-] Failed to get network interface information")
        
        print("=" * 40)
        self.results['network_interfaces'] = interfaces
        return interfaces
    
    def _get_linux_interfaces(self):
        """Get list of network interfaces on Linux"""
        try:
            with open('/proc/net/dev', 'r') as f:
                content = f.readlines()
            interfaces = []
            for line in content[2:]:
                if ':' in line:
                    interface = line.split(':')[0].strip()
                    interfaces.append(interface)
            return interfaces
        except:
            return ['eth0', 'lo']
    
    def _get_linux_interface_info(self, interface):
        """Get information for a specific interface"""
        info = {}
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = socket.gethostbyname(socket.gethostname())
            info['ip'] = ip
            sock.close()
        except:
            info['ip'] = 'unknown'
        return info
    
    # ============ WEB OPERATIONS ============
    
    def fetch_url(self, url, save_to_file=None):
        """Fetch URL content"""
        print(f"\n[*] Fetching URL: {url}")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            req = Request(url, headers=headers)
            response = urlopen(req, timeout=10)
            content = response.read().decode('utf-8', errors='ignore')
            
            info = {
                'url': url,
                'status': response.getcode(),
                'content_length': len(content),
                'content_preview': content[:500] + '...' if len(content) > 500 else content
            }
            
            print(f"[+] Status: {info['status']}")
            print(f"[+] Content Length: {info['content_length']} bytes")
            print(f"[+] Content Preview: {info['content_preview']}")
            
            if save_to_file:
                with open(save_to_file, 'w') as f:
                    f.write(content)
                print(f"[+] Saved to: {save_to_file}")
            
            self.results['url_fetch'] = info
            return content
            
        except Exception as e:
            print(f"[-] Error fetching URL: {e}")
            return None
    
    def url_analyzer(self, url):
        """Analyze URL structure"""
        print(f"\n[*] Analyzing URL: {url}")
        
        parsed = urlparse(url)
        analysis = {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': parsed.query,
            'fragment': parsed.fragment,
            'hostname': parsed.hostname,
            'port': parsed.port
        }
        
        for key, value in analysis.items():
            print(f"[+] {key}: {value}")
        
        self.results['url_analysis'] = analysis
        return analysis
    
    # ============ SECURITY OPERATIONS ============
    
    def port_knocking(self, host, ports, delay=0.5):
        """Simulate port knocking sequence"""
        print(f"\n[*] Port Knocking on {host}")
        print(f"[*] Sequence: {ports}")
        
        results = []
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                status = "knocked" if result == 0 else "closed"
                print(f"[+] Port {port}: {status}")
                results.append({'port': port, 'status': status})
                time.sleep(delay)
                sock.close()
            except Exception as e:
                print(f"[-] Error on port {port}: {e}")
                results.append({'port': port, 'status': 'error'})
        
        self.results['port_knocking'] = {
            'host': host,
            'sequence': ports,
            'results': results
        }
        return results
    
    def network_geolocation(self, ip_address):
        """Get geolocation information for an IP"""
        print(f"\n[*] Geolocation for IP: {ip_address}")
        print("=" * 40)
        
        try:
            url = f"http://ip-api.com/json/{ip_address}"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req, timeout=5)
            data = json.loads(response.read().decode())
            
            if data.get('status') == 'success':
                geo_info = {
                    'ip': data.get('query'),
                    'country': data.get('country'),
                    'region': data.get('regionName'),
                    'city': data.get('city'),
                    'zip': data.get('zip'),
                    'lat': data.get('lat'),
                    'lon': data.get('lon'),
                    'isp': data.get('isp'),
                    'org': data.get('org')
                }
                for key, value in geo_info.items():
                    print(f"[+] {key}: {value}")
                self.results['geolocation'] = geo_info
                print("=" * 40)
                return geo_info
            else:
                print("[-] Geolocation failed")
                return None
        except Exception as e:
            print(f"[-] Error: {e}")
            return None
    
    # ============ DATA OPERATIONS ============
    
    def encrypt_caesar(self, text, shift):
        """Caesar cipher encryption"""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        print(f"\n[*] Caesar Encrypt (shift={shift}): {result}")
        self.results['caesar_encrypted'] = result
        return result
    
    def decrypt_caesar(self, text, shift):
        """Caesar cipher decryption"""
        return self.encrypt_caesar(text, -shift)
    
    def xor_encrypt(self, text, key):
        """XOR encryption"""
        result = ""
        for i, char in enumerate(text):
            key_char = key[i % len(key)]
            result += chr(ord(char) ^ ord(key_char))
        # Display as hex for better visualization
        hex_result = result.encode('utf-8', errors='ignore').hex()
        print(f"\n[*] XOR Encrypt: {hex_result}")
        self.results['xor_encrypted'] = result
        return result
    
    def xor_decrypt(self, encrypted_text, key):
        """XOR decryption (same as encryption)"""
        return self.xor_encrypt(encrypted_text, key)
    
    # ============ THREADING OPERATIONS ============
    
    def fast_port_scan(self, target, start_port=1, end_port=1024, max_threads=50):
        """Multithreaded port scanning"""
        print(f"\n[*] Fast scanning {target} ports {start_port}-{end_port}")
        print(f"[*] Using {max_threads} threads")
        print("=" * 40)
        
        open_ports = []
        results_queue = queue.Queue()
        
        def scan_port(port):
            try:
                target_ip = socket.gethostbyname(target)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    service = self._get_service_name(port)
                    results_queue.put({'port': port, 'service': service})
                sock.close()
            except:
                pass
        
        threads = []
        for port in range(start_port, end_port + 1):
            if len(threads) >= max_threads:
                for thread in threads:
                    thread.join()
                threads = []
            thread = threading.Thread(target=scan_port, args=(port,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Wait for remaining threads
        for thread in threads:
            thread.join()
        
        # Collect results
        while not results_queue.empty():
            result = results_queue.get()
            open_ports.append(result)
            print(f"[+] Port {result['port']} open - {result['service']}")
        
        print("=" * 40)
        print(f"[+] Total open ports: {len(open_ports)}")
        
        self.results['fast_scan'] = {
            'target': target,
            'ports': open_ports,
            'total_open': len(open_ports)
        }
        return open_ports
    
    # ============ EXPORT OPERATIONS ============
    
    def export_results(self, filename="cyberops_results.json"):
        """Export all results to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\n[+] Results exported to: {filename}")
            return True
        except Exception as e:
            print(f"[-] Error exporting results: {e}")
            return False
    
    def save_report(self, filename="cyberops_report.txt"):
        """Save a human-readable report"""
        try:
            with open(filename, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write(f"CYBEROPS REPORT - {self.timestamp}\n")
                f.write("=" * 60 + "\n\n")
                f.write(json.dumps(self.results, indent=2))
            print(f"\n[+] Report saved to: {filename}")
            return True
        except Exception as e:
            print(f"[-] Error saving report: {e}")
            return False
    
    # ============ MAIN MENU ============
    
    def main_menu(self):
        """Interactive main menu with graphics"""
        self.print_banner()
        
        while True:
            print("\n" + "=" * 50)
            print("CYBER OPERATIONS MENU")
            print("=" * 50)
            print("1. Network Scan")
            print("2. Fast Port Scan (Multi-threaded)")
            print("3. DNS Enumeration")
            print("4. Ping Host")
            print("5. Hash Generator")
            print("6. Base64 Operations")
            print("7. Password Generator")
            print("8. System Information")
            print("9. Network Interfaces")
            print("10. URL Fetch")
            print("11. URL Analyzer")
            print("12. Port Knocking")
            print("13. IP Geolocation")
            print("14. Caesar Cipher")
            print("15. XOR Encryption")
            print("16. Export Results")
            print("17. Clear Results")
            print("18. Show Results")
            print("19. Launch Graphics")
            print("20. Launch GUI Console")
            print("0. Exit")
            print("=" * 50)
            
            choice = input("\nEnter your choice: ")
            
            if choice == '0':
                print("\n[+] Exiting CyberOps. Goodbye!")
                break
            
            elif choice == '1':
                target = input("Enter target IP or hostname: ")
                start = int(input("Enter start port (default 1): ") or "1")
                end = int(input("Enter end port (default 1024): ") or "1024")
                self.network_scan(target, start, end)
                
            elif choice == '2':
                target = input("Enter target IP or hostname: ")
                start = int(input("Enter start port (default 1): ") or "1")
                end = int(input("Enter end port (default 1024): ") or "1024")
                threads = int(input("Enter max threads (default 50): ") or "50")
                self.fast_port_scan(target, start, end, threads)
                
            elif choice == '3':
                domain = input("Enter domain name: ")
                self.dns_enumeration(domain)
                
            elif choice == '4':
                host = input("Enter hostname or IP: ")
                count = int(input("Enter ping count (default 4): ") or "4")
                self.ping_host(host, count)
                
            elif choice == '5':
                text = input("Enter text to hash: ")
                print("Algorithms: md5, sha1, sha256, sha512")
                algo = input("Enter algorithm (default sha256): ") or "sha256"
                self.hash_string(text, algo)
                
            elif choice == '6':
                print("\n1. Encode to Base64")
                print("2. Decode from Base64")
                sub_choice = input("Choose option: ")
                if sub_choice == '1':
                    text = input("Enter text to encode: ")
                    self.base64_encode(text)
                elif sub_choice == '2':
                    text = input("Enter base64 text to decode: ")
                    self.base64_decode(text)
                    
            elif choice == '7':
                length = int(input("Enter password length (default 16): ") or "16")
                special = input("Include special characters? (y/n): ").lower() == 'y'
                self.generate_password(length, special)
                
            elif choice == '8':
                self.get_system_info()
                
            elif choice == '9':
                self.get_network_interfaces()
                
            elif choice == '10':
                url = input("Enter URL: ")
                save = input("Save to file? (leave empty for no): ")
                self.fetch_url(url, save if save else None)
                
            elif choice == '11':
                url = input("Enter URL: ")
                self.url_analyzer(url)
                
            elif choice == '12':
                host = input("Enter target host: ")
                ports = input("Enter ports sequence (comma-separated): ")
                ports = [int(p.strip()) for p in ports.split(',')]
                delay = float(input("Enter delay between knocks (default 0.5): ") or "0.5")
                self.port_knocking(host, ports, delay)
                
            elif choice == '13':
                ip = input("Enter IP address: ")
                self.network_geolocation(ip)
                
            elif choice == '14':
                print("\n1. Encrypt with Caesar")
                print("2. Decrypt with Caesar")
                sub_choice = input("Choose option: ")
                text = input("Enter text: ")
                shift = int(input("Enter shift value: "))
                if sub_choice == '1':
                    self.encrypt_caesar(text, shift)
                else:
                    self.decrypt_caesar(text, shift)
                    
            elif choice == '15':
                print("\n1. Encrypt with XOR")
                print("2. Decrypt with XOR")
                sub_choice = input("Choose option: ")
                text = input("Enter text: ")
                key = input("Enter encryption key: ")
                if sub_choice == '1':
                    self.xor_encrypt(text, key)
                else:
                    self.xor_decrypt(text, key)
                    
            elif choice == '16':
                json_file = input("Enter JSON filename (default cyberops_results.json): ") or "cyberops_results.json"
                txt_file = input("Enter TXT filename (default cyberops_report.txt): ") or "cyberops_report.txt"
                self.export_results(json_file)
                self.save_report(txt_file)
                
            elif choice == '17':
                self.results = {}
                print("[+] Results cleared")
                
            elif choice == '18':
                if self.results:
                    print("\n" + json.dumps(self.results, indent=2))
                else:
                    print("\n[-] No results available")
            
            elif choice == '19':
                self.launch_graphics_menu()
                
            elif choice == '20':
                self.launch_gui_console()
                    
            else:
                print("\n[-] Invalid choice. Please try again.")
            
            if choice != '0':
                input("\nPress Enter to continue...")
    
    def launch_graphics_menu(self):
        """Launch graphics menu"""
        if not turtle:
            print("\n[-] Turtle graphics not available. Please install tkinter.")
            return
        
        print("\n" + "=" * 40)
        print("GRAPHICS MENU")
        print("=" * 40)
        print("1. Network Scan Animation")
        print("2. Hash Visualization")
        print("3. Cyber Radar")
        print("4. Cyber Art")
        print("5. All Graphics")
        print("0. Back")
        print("=" * 40)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            target = input("Enter target IP (default 127.0.0.1): ") or "127.0.0.1"
            ports = input("Enter ports (comma-separated, default 22,80,443,3306): ") or "22,80,443,3306"
            ports = [int(p.strip()) for p in ports.split(',')]
            threading.Thread(target=lambda: CyberGraphics.draw_network_animation(target, ports), daemon=True).start()
            
        elif choice == '2':
            text = input("Enter text to hash (default 'CyberOps Security'): ") or "CyberOps Security"
            hash_val = hashlib.sha256(text.encode()).hexdigest()
            threading.Thread(target=lambda: CyberGraphics.visualize_hash(text, hash_val), daemon=True).start()
            
        elif choice == '3':
            threading.Thread(target=CyberGraphics.draw_cyber_radar, daemon=True).start()
            
        elif choice == '4':
            threading.Thread(target=CyberGraphics.draw_cyber_art, daemon=True).start()
            
        elif choice == '5':
            threading.Thread(target=lambda: self._run_all_graphics(), daemon=True).start()
    
    def _run_all_graphics(self):
        """Run all graphics in sequence"""
        print("\n[*] Starting all graphics...")
        CyberGraphics.draw_cyber_radar()
        CyberGraphics.draw_cyber_art()
        CyberGraphics.visualize_hash("CyberOps Security", hashlib.sha256("CyberOps Security".encode()).hexdigest())
        CyberGraphics.draw_network_animation("127.0.0.1", [22, 80, 443, 3306])
    
    def launch_gui_console(self):
        """Launch the GUI console"""
        if not tk:
            print("\n[-] tkinter not available. GUI console disabled.")
            return
        
        print("\n[+] Launching GUI Console...")
        try:
            gui = CyberGUIConsole()
            gui.run()
        except Exception as e:
            print(f"[-] Error launching GUI: {e}")


def main():
    """Main entry point"""
    try:
        # Check for command line arguments
        if len(sys.argv) > 1:
            if sys.argv[1] == "--gui":
                if tk:
                    gui = CyberGUIConsole()
                    gui.run()
                else:
                    print("tkinter not available. Running in console mode.")
                    app = CyberOps()
                    app.main_menu()
            elif sys.argv[1] == "--graphics":
                if turtle:
                    CyberGraphics.draw_cyber_radar()
                else:
                    print("Turtle graphics not available.")
            else:
                app = CyberOps()
                app.main_menu()
        else:
            app = CyberOps()
            app.main_menu()
            
    except KeyboardInterrupt:
        print("\n\n[!] Operation interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()