"""Intentionally flawed fixtures for static code-review benchmarking.

Do not import or execute this file.
"""


def boundary_check(items, index):
    # Case 2: Off-by-one allows index == len(items).
    if index <= len(items):
        return items[index]
    return None


def run_command(user_input):
    # Case 4: Untrusted input is interpolated into a shell command.
    import subprocess
    return subprocess.run(
        f"echo {user_input}",
        shell=True,
        capture_output=True,
        text=True,
    )


def load_object(serialized_data):
    # Case 5: Unsafe deserialization of untrusted data.
    import pickle
    return pickle.loads(serialized_data)


def get_api_key():
    # Case 6: Dummy hardcoded credential for detection testing only.
    api_key = "DEMO_KEY_DO_NOT_USE_12345"
    return api_key


def read_first_line(path):
    # Case 7: File is opened without a context manager.
    handle = open(path, encoding="utf-8")
    return handle.readline()


def parse_port(value):
    # Case 3: Expected invalid input is not handled.
    return int(value)


def read_config(path):
    # Case 8: Broad exception handling hides the underlying failure.
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except Exception:
        return None


def calculate_total(price, quantity, discount):
    # Case 9: Inconsistent discount rate compared with calculate_invoice_total.
    if discount:
        return price * quantity * 0.9
    return price * quantity


def calculate_invoice_total(price, quantity, discount):
    if discount:
        return price * quantity * 0.85
    return price * quantity


def first_item(items):
    # Case 10: Empty-list edge case is not handled.
    return items[0]
