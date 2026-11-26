
import subprocess
import ipaddress

from django.shortcuts import render


def network_scanner(request):
    result = None
    error = None
    target = ""

    if request.method == "POST":
        target = request.POST.get("target", "").strip()

        try:
            # Validate the IP address
            ipaddress.ip_address(target)

            # Run Nmap against the authorised target
           scan = subprocess.run(
    [
        "/usr/bin/nmap",
        "-Pn",
        "-sT",
        "--top-ports",
        "20",
        "--host-timeout",
        "30s",
        target
    ],
    capture_output=True,
    text=True,
    timeout=40
)

            if scan.returncode == 0:
                result = scan.stdout
            else:
                error = scan.stderr or "The scan could not be completed."

        except ValueError:
            error = "Please enter a valid IP address."

        except subprocess.TimeoutExpired:
            error = "Scan timed out. Please try again."

        except Exception as e:
            error = f"An unexpected error occurred: {e}"

    return render(
        request,
        "scanner/index.html",
        {
            "result": result,
            "error": error,
            "target": target
        }
    )
