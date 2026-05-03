from ddgs import DDGS
import requests
from bs4 import BeautifulSoup

print("🤖 REAL CODE FETCH AI STARTED\n")


# -------------------------
# 🌐 SEARCH INTERNET
# -------------------------
def search(query):
    links = []
    with DDGS() as ddgs:
        for r in ddgs.text(query + " python code github stackoverflow", max_results=5):
            links.append(r["href"])
    return links


# -------------------------
# 📄 EXTRACT ONLY REAL CODE
# -------------------------
def extract_code(url):
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")

        code_blocks = soup.find_all(["code", "pre"])

        codes = []

        for c in code_blocks:
            text = c.get_text()

            # only keep LONG code blocks (important fix)
            if len(text.split("\n")) > 20:
                codes.append(text)

        return codes

    except:
        return []


# -------------------------
# 🧠 PICK BEST (LONGEST CODE)
# -------------------------
def pick_best(codes):
    if not codes:
        return None

    # choose longest real code block
    best = max(codes, key=lambda x: len(x))
    return best


# -------------------------
# 🤖 MAIN AI
# -------------------------
def get_real_code(question):
    print("\n🔎 Searching real coding websites...\n")

    links = search(question)

    all_codes = []

    print("📚 Sources:\n")
    for url in links:
        print(url)
        codes = extract_code(url)
        all_codes.extend(codes)

    best = pick_best(all_codes)

    if not best:
        return "❌ No real code found on internet."

    return f"""
==============================
🤖 REAL CODE FROM INTERNET
==============================

{best}

==============================
📌 Source-based result (no fake code generated)
==============================
"""


# -------------------------
# 💬 CHAT LOOP
# -------------------------
while True:
    user = input("\nMekonnenAI code writer: ")

    if user.lower() == "exit":
        break

    result = get_real_code(user)
    print("\n" + result + "\n")