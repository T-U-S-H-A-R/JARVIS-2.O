import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import socket

# ---------- AUTO PORT SELECT FUNCTION ----------
def get_free_port(start_port=8000, limit=20):
    port = start_port
    for _ in range(limit):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("No free ports found!")

PORT = get_free_port(8000)    # auto free port

# ---------- SCRIPT MAPPING (Only Requested Scripts) ----------
scripts = {
    # સિસ્ટમ અને યુટિલિટીઝ
    "/shutdown": "shutdown.py",
    "/restart": "restart.py",
    "/battery": "battery.py",
    "/camera": "camera.py",
    "/time": "time.py",
    "/calendar": "calendar.py", # યુઝર રિક્વેસ્ટ પ્રમાણે ઉમેર્યું
    "/weather": "weather.py",   # યુઝર રિક્વેસ્ટ પ્રમાણે ઉમેર્યું
    
    # ગ્રાફ્સ (Trigonometry)
    "/sin": "sin.py",
    "/cos": "cos.py",
    "/tan": "tan.py",
    "/cot": "cot.py",
    "/sec": "sec.py",
    "/cosec": "cosec.py",
    
    # ગ્રાફ્સ (Parabola)
    "/upward_parabola": "upward_parabola.py",
    "/downward_parabola": "downward_parabola.py",
    "/right_shift_parabola": "right_shift_parabola.py",
    "/left_shift_parabola": "left_shift_parabola.py",
    
    # ભાષાઓ (Languages)
    "/control": "control.py", # All Languages
    "/german": "german.py",
    "/friday": "friday.py",
    "/japan": "japan.py",
    "/russia": "russia.py",
    "/china": "china.py",
    "/italian": "italian.py",
    "/french": "french.py",
    "/jarfrinova": "jarvis_friday_nova.py"
}

# ---------- HANDLER ----------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # If script URL exists (executes script and returns 'Running...')
        if self.path in scripts:
            subprocess.Popen(["python", scripts[self.path]])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Running {scripts[self.path]}".encode())
            return

        # Serve background image (a.jpg)
        if self.path == "/a.jpg" and os.path.exists("a.jpg"):
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            with open("a.jpg", "rb") as f:
                self.wfile.write(f.read())
            return

        # ---------- MAIN UI PAGE (Mobile Optimized & Filtered) ----------
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>JARVIS Mobile Panel</title>
<style>
    body {
        /* Background image and full screen setup */
        background-image: url('/a.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        text-align: center;
        color: white;
        font-family: Arial, sans-serif;
        height: 100vh; /* Ensure full viewport height */
        display: flex;
        flex-direction: column;
    }

    h1 {
        margin: 10px 0;
        padding: 5px;
        font-size: 5vw; /* Responsive font size */
        text-shadow: 3px 3px 8px black;
    }

    /* MOBILE OPTIMIZATION: CSS Grid Layout */
    .button-container {
        display: flex;
        flex-wrap: wrap; 
        justify-content: center;
        
        flex-grow: 1; 
        
        display: grid;
        /* 4 columns for mobile view */
        grid-template-columns: repeat(4, 1fr); 
        gap: 5px; 
        
        padding: 0 5px 5px 5px; 
        
        position: relative; 
        overflow-y: hidden; 
    }

    .rect-btn {
        /* Button style adjustments for small screen */
        width: auto; 
        padding: 8px 3px; 
        margin: 0; 
        
        background-color: white;
        color: black;
        border: none;
        font-size: 3vw; /* Very small, responsive font size */
        font-weight: bold;
        cursor: pointer;
        border-radius: 4px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
        transition: 0.2s;
        
        white-space: nowrap; 
        overflow: hidden; 
        text-overflow: ellipsis;
    }
    .button-container button:nth-child(7n+1) { background-color: #111; color: #EEE; } /* Black */
    .button-container button:nth-child(7n+2) { background-color: #333; color: #EEE; } /* Dark Gray */
    .button-container button:nth-child(7n+3) { background-color: #555; color: #EEE; } /* Medium Dark Gray */
    .button-container button:nth-child(7n+4) { background-color: #777; color: #111; } /* Mid Gray (Dark Text) */
    .button-container button:nth-child(7n+5) { background-color: #AAA; color: #111; } /* Light Gray (Dark Text) */
    .button-container button:nth-child(7n+6) { background-color: #CCC; color: #111; } /* Lighter Gray (Dark Text) */
    .button-container button:nth-child(7n+7) { background-color: #EEE; color: #111; } /* White (Dark Text) */

    .rect-btn:hover {
        transform: scale(1.05); 
        box-shadow: 0px 0px 10px #EEE; 
        opacity: 0.9;
    }
</style>
</head>
<body>
    <h1>JARVIS CONTROL PANEL</h1>

    <div class="button-container">
        <button class="rect-btn" onclick="window.location.href='/shutdown'">Shutdown</button>
        <button class="rect-btn" onclick="window.location.href='/restart'">Restart</button>
        <button class="rect-btn" onclick="window.location.href='/battery'">Battery</button>
        <button class="rect-btn" onclick="window.location.href='/camera'">Camera</button>
        <button class="rect-btn" onclick="window.location.href='/time'">Time</button>
        <button class="rect-btn" onclick="window.location.href='/calendar'">Calendar</button>
        <button class="rect-btn" onclick="window.location.href='/weather'">Weather</button>
        
        <button class="rect-btn" onclick="window.location.href='/sin'">Sin X</button>
        <button class="rect-btn" onclick="window.location.href='/cos'">Cos X</button>
        <button class="rect-btn" onclick="window.location.href='/tan'">Tan X</button>
        <button class="rect-btn" onclick="window.location.href='/cot'">Cot X</button>
        <button class="rect-btn" onclick="window.location.href='/sec'">Sec X</button>
        <button class="rect-btn" onclick="window.location.href='/cosec'">Cosec X</button>
        <button class="rect-btn" onclick="window.location.href='/upward_parabola'">Upward Parabola</button>
        <button class="rect-btn" onclick="window.location.href='/downward_parabola'">Downward Parabola</button>
        <button class="rect-btn" onclick="window.location.href='/right_shift_parabola'">Right Shift Parabola</button>
        <button class="rect-btn" onclick="window.location.href='/left_shift_parabola'">Left Shift Parabola</button>
        
        <button class="rect-btn" onclick="window.location.href='/control'">All Languages</button>
        <button class="rect-btn" onclick="window.location.href='/german'">German</button>
        <button class="rect-btn" onclick="window.location.href='/friday'">Friday</button>
        <button class="rect-btn" onclick="window.location.href='/japan'">Japan</button>
        <button class="rect-btn" onclick="window.location.href='/russia'">Russia</button>
        <button class="rect-btn" onclick="window.location.href='/china'">China</button>
        <button class="rect-btn" onclick="window.location.href='/italian'">Italian</button>
        <button class="rect-btn" onclick="window.location.href='/french'">French</button>
        <button class="rect-btn" onclick="window.location.href='/jarfrinova'">JARVIS-FRIDAY-NOVA</button>
    </div>
</body>
</html>
""")

# ---------- RUN SERVER ----------
ip = socket.gethostbyname(socket.gethostname())
print(f"\nServer running on: http://{ip}:{PORT}\n")

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
