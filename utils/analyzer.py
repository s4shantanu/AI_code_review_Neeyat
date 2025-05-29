import subprocess

def analyze_code(path):
    pylint_output = subprocess.getoutput(f"pylint {path}")
    bandit_output = subprocess.getoutput(f"bandit -r {path}")
    radon_output = subprocess.getoutput(f"radon cc {path} -s")

    return {
        "pylint": pylint_output,
        "bandit": bandit_output,
        "radon": radon_output,
    }
