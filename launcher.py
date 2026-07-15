import os
import signal
import subprocess
import time
import requests


ROOT = os.path.dirname(os.path.abspath(__file__))

processes = []


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
    "chromium-browser",
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
                print(f"✓ {url} is ready")
                return True

        except:
            pass

        time.sleep(1)

    return False



try:

    # -------------------------
    # Start Flask
    # -------------------------

    print("Starting Flask...")

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



    # -------------------------
    # Build React
    # -------------------------

    print("Building React frontend...")

    subprocess.run(
        [
            "npm",
            "run",
            "build"
        ],
        cwd=ROOT,
        check=True
    )



    # -------------------------
    # Start Vite Preview
    # -------------------------

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



    # -------------------------
    # Wait until ready
    # -------------------------

    if not wait_for("http://127.0.0.1:5000"):
        raise RuntimeError("Flask failed to start")


    if not wait_for("http://127.0.0.1:4173"):
        raise RuntimeError("Frontend failed to start")



    # -------------------------
    # Launch Browser
    # -------------------------

    print("Launching kiosk mode...")

    browser = subprocess.Popen(
        browser_cmd
    )

    processes.append(browser)


    print("\nAgokansie is running!\n")


    browser.wait()



except KeyboardInterrupt:
    pass



finally:

    print("Stopping...")

    for p in processes:

        try:
            p.send_signal(signal.SIGTERM)

        except:
            pass