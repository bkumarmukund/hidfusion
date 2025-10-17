# Beauty-R1 Linux Key Mapper

This project provides a **Python-based key mapping tool** for the **Beauty-R1 Bluetooth remote** (or similar devices).  
It allows you to map device buttons to custom keyboard actions on Linux.

---

## ⚙️ Features
- Automatically detects the input device path (e.g., `/dev/input/event*`).
- Maps button inputs to customizable keyboard actions.
- Easily extendable for different profiles or applications (e.g., Chrome, VSCode).
- Works without root privileges when granted input permissions.

---

## 🧩 Prerequisites
Make sure you have Python 3 installed, and install the following dependencies:

```bash
sudo apt install python3-evdev
```

You may also need permission to access the input device:
```bash
sudo chmod a+rw /dev/input/event*
```

---

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/beauty-r1-linux.git
   cd beauty-r1-linux
   ```

2. Run the script:
   ```bash
   python3 main.py
   ```

3. Press buttons on the Beauty-R1 remote — you should see mapped actions in the terminal.

---

## 🧠 How it works
- The script scans connected devices for one matching the name `"Beauty-R1"`.
- Each button press sends an event with a **relative value**, which is translated into an action using a dictionary (`REL_TO_KEY`).
- Actions are linked to functions like `press_enter()` or `press_f9()`.

---

## 🛠️ Example Output
```
✅ Found device: Beauty-R1 at /dev/input/event23
LEFT pressed
RIGHT pressed
MIDDLE pressed
```

---

## 🧩 Future Enhancements
- Profile-based key mapping using environment variables (e.g., `BEAUTY_PROFILE=chrome`).
- Configurable key mappings via JSON or YAML.
- GUI for easy mapping customization.

---

## 🪪 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Developed by **Balmukund Kumar**
