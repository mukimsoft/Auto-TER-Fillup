import pyautogui
import pyperclip
import time


START_DELAY      = 3       # সেকেন্ড — স্ক্রিপ্ট শুরুর আগে প্রস্তুতির সময়
FIELD_DELAY      = 0.6     # প্রতিটি ফিল্ডের মাঝে বিরতি (সেকেন্ড)
TYPE_DELAY       = 0.05    # প্রতিটি কী-প্রেসের মাঝে বিরতি (সেকেন্ড)

# ✏️ TER ফর্মের উত্তরগুলো এখানে কাস্টমাইজ করো
POSITIVE_RESPONSE  = "Everything is good about this course."
NEGATIVE_RESPONSE  = "Nothing to complain about."
SUGGESTION_RESPONSE = "Keep up the great teaching!"


pyautogui.FAILSAFE = True   # মাউস কোণায় নিলে স্ক্রিপ্ট বন্ধ হবে
pyautogui.PAUSE    = 0.1    # প্রতিটি pyautogui কমান্ডের পরে সামান্য বিরতি



def countdown(seconds: int):
    """কাউন্টডাউন দেখায় যাতে ফর্ম প্রস্তুত করার সময় পাও।"""
    print("\n⏳ স্ক্রিপ্ট শুরু হচ্ছে...")
    for i in range(seconds, 0, -1):
        print(f"   ➡️  {i} সেকেন্ড বাকি — TER ফর্ম সামনে রাখো!")
        time.sleep(1)
    print("🚀 শুরু হচ্ছে!\n")


def paste_text(text: str):
    """ক্লিপবোর্ডে টেক্সট কপি করে Ctrl+V দিয়ে পেস্ট করে।"""
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(FIELD_DELAY)


def go_to_next_field():
    """Tab চেপে পরের ফিল্ডে যায়।"""
    pyautogui.press('tab')
    time.sleep(FIELD_DELAY)


def select_radio_or_checkbox(option: int = 1):
    """
    রেডিও বাটন বা চেকবক্সে ক্লিক করার জন্য।
    Tab দিয়ে যাওয়ার পর Space/Enter দিয়ে সিলেক্ট করে।
    option: 1-5 (রেটিং স্কেলের জন্য, যেমন 5 = Excellent)
    """
    for _ in range(option - 1):
        pyautogui.press('right')
        time.sleep(0.2)
    pyautogui.press('space')
    time.sleep(FIELD_DELAY)


def fill_rating(rating: int = 5):
    """
    রেটিং ফিল্ড পূরণ করে (সাধারণত 1-5 স্কেল)।
    ডিফল্ট: 5 (সর্বোচ্চ রেটিং)
    """
    pyautogui.press('tab')
    time.sleep(0.3)
    select_radio_or_checkbox(rating)



def fill_ter_form():
    """
    TER ফর্মের প্রতিটি ধাপ স্বয়ংক্রিয়ভাবে পূরণ করে।

    ⚠️ তোমার ফর্মের গঠন অনুযায়ী নিচের ধাপগুলো সাজিয়ে নাও।
    প্রতিটি section comment দেওয়া আছে — প্রয়োজনে বাদ দাও বা যোগ করো।
    """

    print("=" * 45)
    print("🧠  AUTO TER FILLUP — শুরু হচ্ছে")
    print("=" * 45)

    # ── Section 1: রেটিং প্রশ্নগুলো (সাধারণত 5-10টি) ──
    print("\n📊 রেটিং প্রশ্ন পূরণ করছি...")

    total_rating_questions = 10  # তোমার ফর্মে যতটি রেটিং প্রশ্ন আছে
    for q_num in range(1, total_rating_questions + 1):
        print(f"   ✅ প্রশ্ন {q_num}/{total_rating_questions} — রেটিং: 5 (Excellent)")
        fill_rating(rating=5)

    # ── Section 2: "ভালো দিক" / Positive টেক্সট বক্স ──
    print("\n✍️  ইতিবাচক মন্তব্য লিখছি...")
    go_to_next_field()
    paste_text(POSITIVE_RESPONSE)
    print(f"   ✅ পেস্ট করা হয়েছে: \"{POSITIVE_RESPONSE}\"")

    # ── Section 3: "খারাপ দিক" / Negative টেক্সট বক্স ──
    print("\n✍️  নেতিবাচক মন্তব্য লিখছি...")
    go_to_next_field()
    paste_text(NEGATIVE_RESPONSE)
    print(f"   ✅ পেস্ট করা হয়েছে: \"{NEGATIVE_RESPONSE}\"")

    # ── Section 4: পরামর্শ / Suggestion টেক্সট বক্স ──
    print("\n✍️  পরামর্শ লিখছি...")
    go_to_next_field()
    paste_text(SUGGESTION_RESPONSE)
    print(f"   ✅ পেস্ট করা হয়েছে: \"{SUGGESTION_RESPONSE}\"")

    # ── Section 5: Submit বাটনে ক্লিক ──
    print("\n📤 ফর্ম সাবমিট করছি...")
    go_to_next_field()
    pyautogui.press('enter')
    time.sleep(1)

    print("\n" + "=" * 45)
    print("🎉  TER ফর্ম সফলভাবে পূরণ হয়েছে!")
    print("=" * 45)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#              🚀 ENTRY POINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════╗
║        🧠 AUTO TER FILLUP           ║
║  Teacher Evaluation Report Automator ║
╚══════════════════════════════════════╝
⚠️  সাবধান: মাউস স্ক্রিনের যেকোনো কোণায় নিলে
    স্ক্রিপ্ট বন্ধ হয়ে যাবে (Failsafe)।
""")

    try:
        countdown(START_DELAY)
        fill_ter_form()

    except pyautogui.FailSafeException:
        print("\n🛑 Failsafe চালু হয়েছে — স্ক্রিপ্ট বন্ধ!")

    except KeyboardInterrupt:
        print("\n🛑 ব্যবহারকারী বন্ধ করেছেন (Ctrl+C)।")

    except Exception as e:
        print(f"\n❌ অপ্রত্যাশিত সমস্যা: {e}")

