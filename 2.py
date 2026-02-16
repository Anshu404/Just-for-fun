import hashlib
import base64
import pyotp
import requests
import json
import sys

# ==========================
# CONFIGURATION
# ==========================
GIST_URL = "https://gist.github.com/Anshu404/a31532498b2d8335f5c1b3e5ffc6ec4c"
EMAIL = "anshukumarmandal346@gmail.com"
# Challenge 004 constant (Ensure this matches your specific challenge instructions)
CHALLENGE_CONSTANT = "HENNGECHALLENGE004" 
API_ENDPOINT = "https://api.challenge.hennge.com/challenges/backend-recursion/004"

def main():
    print(f"--- Starting Mission 3 for {EMAIL} ---")

    # 1. Build shared secret (email + constant)
    raw_secret = (EMAIL + CHALLENGE_CONSTANT).encode()

    # 2. Convert to base32 (Required by TOTP libraries as the seed)
    secret = base64.b32encode(raw_secret)

    # 3. Generate TOTP (10 digits, HMAC-SHA512, 30s step)
    # Note: HENNGE usually uses SHA512 for the hash
    totp = pyotp.TOTP(secret, digits=10, digest=hashlib.sha512)
    otp = totp.now()

    print(f"[+] Generated TOTP: {otp}")

    # 4. Build Basic Auth token (email:TOTP -> base64 encoding)
    auth_string = f"{EMAIL}:{otp}"
    auth_b64 = base64.b64encode(auth_string.encode()).decode()

    print(f"[+] Base64 Auth Header: {auth_b64}")

    # 5. Construct JSON body
    payload = {
        "github_url": GIST_URL,
        "contact_email": EMAIL,
        "solution_language": "python"
    }

    print("[+] Sending POST request to HENNGE...")

    # 6. Send POST request
    try:
        response = requests.post(
            API_ENDPOINT,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Basic {auth_b64}"
            },
            data=json.dumps(payload)
        )

        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Response Body: {response.text}")
        
        if response.status_code == 200:
            print("\nSUCCESS! Check your email.")
        else:
            print("\nFAILED. Check your Gist URL, Email, or TOTP logic.")

    except Exception as e:
        print(f"[-] Error occurred: {e}")

if __name__ == "__main__":
    main()
