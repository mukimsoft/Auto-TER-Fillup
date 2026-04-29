# 🧠 Auto TER Fillup
A lightweight Python script to automatically fill out Teacher Evaluation Reports (TER) using keyboard simulation and clipboard automation.

> ⚠️ Make sure the TER form is open and active before running the script.

---

## ✨ Features
- ⏱️ Start delay to prepare before automation begins
- 🔄 Auto navigation through form fields
- 📝 Auto fill with pre-set text responses
- ⭐ Auto rating for all rating questions
- 🛡️ Failsafe — move mouse to any corner to stop

---

## 🛠️ Installation

```bash
pip install pyautogui pyperclip
```

---

## 🚀 Usage

1. Open your TER form in the browser
2. Place your cursor on the first field
3. Run the script:

```bash
python main.py
```

---

## ⚙️ Configuration

Edit the top of `main.py` to customize:

```python
START_DELAY         = 5      # seconds before script starts
FIELD_DELAY         = 0.6    # delay between each field
POSITIVE_RESPONSE   = "Everything is good about this course."
NEGATIVE_RESPONSE   = "Nothing to complain about."
SUGGESTION_RESPONSE = "Keep up the great teaching!"
```

---

## 🛑 How to Stop
- Move mouse to any **screen corner** (Failsafe)
- Or press `Ctrl + C`
