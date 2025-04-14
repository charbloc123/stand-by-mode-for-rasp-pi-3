# stand-by-mode-for-rasp-pi-3
# Standby Dashboard

A fullscreen Raspberry Pi dashboard that displays the current time, date, and a custom message — perfect for HDMI standby displays or smart signage setups like Google TV or Nintendo Switch.

---

## 📺 Features

- Fullscreen visual display with:
  - 🕒 Real-time clock
  - 📆 Current date
  - 📝 Custom messages (passed via terminal)
  - 📡 HDMI source/channel labels
  - 🖊️ Footer with your branding
- Lightweight and built for Raspberry Pi 3+
- Exits cleanly with ESC key

---

## 🚀 Setup Instructions

### 1. Install Python & Pygame

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install pygame
# 2. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/standby-dashboard.git
cd standby-dashboard
# 3. Run the Dashboard
bash
Copy
Edit
python3 dashboard.py "Custom Message Here"
# Example:
bash
Copy
Edit
python3 dashboard.py "Switch is offline"
Your monitor will now display:

"STAND BY MODE"

Your custom message

Date & time

Channel listings

A footer with "MADE BY CJC - POWERED BY RASPBERRY PI 3"

To exit, just press the ESC key on a connected keyboard.

🔁 Auto-Start on Boot (Optional)
To run the dashboard automatically when your Pi boots:

Open the crontab:

bash
Copy
Edit
crontab -e
Add this line at the bottom (adjust the path if different):

bash
Copy
Edit
@reboot python3 /home/pi/standby-dashboard/dashboard.py "Standby Mode"
Save and reboot your Pi:

bash
Copy
Edit
sudo reboot
Your dashboard should now launch automatically on boot.

💡 Tips
You can SSH into your Pi and run the script remotely if it's connected to an HDMI display.

You can change the fonts, colors, or layout by editing dashboard.py.

You can also schedule different messages based on time of day using a shell script or crontab jobs.
