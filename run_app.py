import subprocess
import sys


# Start FastAPI
fastapi = subprocess.Popen([
    sys.executable,
    "-m",
    "uvicorn",
    "api:app",
    "--reload"
])

# Start Streamlit
streamlit = subprocess.Popen([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    "app.py"
])

# Keep both running
try:
    fastapi.wait()
    streamlit.wait()

except KeyboardInterrupt:
    fastapi.terminate()
    streamlit.terminate()