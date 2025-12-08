import crypto_utils
import face_auth
import os

def setup():
    print("=== Security Setup ===")
    
    # 1. Generate Encryption Key
    if os.path.exists(crypto_utils.KEY_FILE):
        print("[*] Encryption key already exists.")
    else:
        print("[*] Generating new encryption key...")
        crypto_utils.generate_key()
        print("[+] Key generated and saved to 'secret.key'.")

    # 2. Enroll Face
    print("\n[*] Starting Face Enrollment...")
    print("    Please ensure you are in a well-lit area.")
    input("    Press Enter to start camera...")
    
    if face_auth.train_model():
        print("[+] Face model trained and saved.")
        print("\n=== Setup Complete ===")
        print("You can now run 'main.py' to log securely.")
        print("Use 'view_logs.py' to decrypt and view logs.")
    else:
        print("[-] Face enrollment failed.")

if __name__ == "__main__":
    setup()
