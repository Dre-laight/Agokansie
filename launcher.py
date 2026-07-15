import os
import signal
import subprocess
import time
import requests
import keyboard


ROOT = os.path.dirname(os.path.abspath(__file__))

processes = []

browser = None
backend = None
frontend = None


# -------------------------
# Configure paths
# -------------------------

env = os.environ.copy()
env["FLASK_APP"] = "app.py"


python_exec = os.path.join(
    ROOT,
    "backend",
    "venv",
    "bin",
    "python"
)


browser_cmd = [
    "chromium",
    "--kiosk",
    "--incognito",
    "--disable-infobars",
    "--noerrdialogs",
    "--disable-session-crashed-bubble",
    "--disable-features=Translate",
    "http://127.0.0.1:4173"
]


# -------------------------
# Wait for server
# -------------------------

def wait_for(url, timeout=60):

    print(f"Waiting for {url}...")

    start = time.time()

    while time.time() - start < timeout:

        try:
            r = requests.get(url, timeout=1)

            if r.status_code < 500:
                print(f"✓ {url} ready")
                return True

        except:
            pass

        time.sleep(1)

    return False



# -------------------------
# Stop services
# -------------------------

def stop_services():

    global processes

    print("\nStopping services...")

    for p in processes:

        try:
            p.send_signal(signal.SIGTERM)

        except:
            pass


    processes.clear()

    time.sleep(2)



# -------------------------
# Start everything
# -------------------------

def start_services():

    global backend
    global frontend
    global browser


    print("\nStarting Flask...")


    backend = subprocess.Popen(
        [
            python_exec,
            "-m",
            "flask",
            "run",
            "--host=0.0.0.0"
        ],
        cwd=os.path.join(ROOT, "backend"),
        env=env
    )


    processes.append(backend)



    print("Building React...")


    subprocess.run(
        [
            "npm",
            "run",
            "build"
        ],
        cwd=ROOT,
        check=True
    )



    print("Starting frontend...")


    frontend = subprocess.Popen(
        [
            "npm",
            "run",
            "preview",
            "--",
            "--host",
            "0.0.0.0"
        ],
        cwd=ROOT
    )


    processes.append(frontend)



    if not wait_for("http://127.0.0.1:5000"):
        raise RuntimeError(
            "Flask failed"
        )


    if not wait_for("http://127.0.0.1:4173"):
        raise RuntimeError(
            "Frontend failed"
        )



    print("Opening Chromium...")


    browser = subprocess.Popen(
        browser_cmd
    )


    processes.append(browser)



    print("\nAgokansie running 🚀")
    print("Press F9 to restart\n")




# -------------------------
# Restart handler
# -------------------------

def restart():

    print("\n===== RESTART REQUESTED =====")

    stop_services()

    start_services()



# -------------------------
# Main
# -------------------------

try:

    start_services()          # <-- leave this exactly as-is


    try:
        keyboard.add_hotkey(
            "f9",
            restart
        )
    except ImportError:
        print("⚠ F9 hotkey disabled (need root/input-group permissions on Linux). Continuing without it.")


    while True:

        time.sleep(1)



except KeyboardInterrupt:

    pass



finally:

    stop_services()