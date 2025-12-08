import crypto_utils
import face_auth
import os
import sys
import json
from fpdf import FPDF
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

def export_to_txt(text):
    try:
        with open("decrypted_logs.txt", "w", encoding="utf-8") as f:
            f.write(text)
        return True, "decrypted_logs.txt"
    except Exception as e:
        return False, str(e)

def export_to_json(text):
    try:
        data = {"timestamp": "Exported Log", "content": text}
        with open("decrypted_logs.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True, "decrypted_logs.json"
    except Exception as e:
        return False, str(e)

def export_to_pdf(text):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Handle encoding issues by replacing unsupported characters
        safe_text = text.encode('latin-1', 'replace').decode('latin-1')
        
        pdf.multi_cell(0, 10, txt=safe_text)
        pdf.output("decrypted_logs.pdf")
        return True, "decrypted_logs.pdf"
    except Exception as e:
        return False, str(e)

def view_logs():
    console = Console()
    
    console.print(Panel("[bold blue]Secure Log Viewer[/bold blue]", style="blue"))
    
    # 1. Load Key
    key = crypto_utils.load_key()
    if not key:
        console.print("[bold red]Error:[/bold red] Encryption key not found. Run setup first.")
        return

    # 2. Authenticate
    console.print("\n[bold yellow]Authenticating...[/bold yellow] Please look at the camera.")
    if face_auth.authenticate():
        console.print("\n[bold green]Access Granted![/bold green]")
        
        if not os.path.exists("captured_text.enc"):
            console.print("[italic]No logs found.[/italic]")
            return
            
        try:
            with open("captured_text.enc", "rb") as f:
                encrypted_data = f.read()
            
            decrypted_text = crypto_utils.decrypt_text(encrypted_data, key)
            
            while True:
                console.print("\n[bold cyan]Options:[/bold cyan]")
                console.print("1. View Logs")
                console.print("2. Export as Text (.txt)")
                console.print("3. Export as JSON (.json)")
                console.print("4. Export as PDF (.pdf)")
                console.print("5. Exit")
                
                choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5"], default="1")
                
                if choice == "1":
                    console.print("\n[bold underline]Decrypted Logs:[/bold underline]\n")
                    console.print(decrypted_text)
                    console.print("\n" + "-"*30)
                    
                elif choice == "2":
                    success, msg = export_to_txt(decrypted_text)
                    if success:
                        console.print(f"[bold green]Successfully exported to {msg}[/bold green]")
                    else:
                        console.print(f"[bold red]Export failed:[/bold red] {msg}")
                        
                elif choice == "3":
                    success, msg = export_to_json(decrypted_text)
                    if success:
                        console.print(f"[bold green]Successfully exported to {msg}[/bold green]")
                    else:
                        console.print(f"[bold red]Export failed:[/bold red] {msg}")

                elif choice == "4":
                    success, msg = export_to_pdf(decrypted_text)
                    if success:
                        console.print(f"[bold green]Successfully exported to {msg}[/bold green]")
                    else:
                        console.print(f"[bold red]Export failed:[/bold red] {msg}")
                        
                elif choice == "5":
                    console.print("[yellow]Exiting...[/yellow]")
                    break
            
        except Exception as e:
            console.print(f"[bold red]Error decrypting logs:[/bold red] {e}")
    else:
        console.print("\n[bold red]Access Denied![/bold red] Face not recognized.")

if __name__ == "__main__":
    view_logs()
