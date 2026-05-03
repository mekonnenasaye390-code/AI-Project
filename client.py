import requests

print("🧠 Mekonnen AI Reasoning Chatbot (Upgraded Brain)\n")

# ================== WIKIPEDIA ==================
def wiki_search(query):
    try:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "opensearch",
            "search": query,
            "limit": 1,
            "namespace": 0,
            "format": "json"
        }

        res = requests.get(url, params=params).json()

        if res[1]:
            title = res[1][0]
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
            summary = requests.get(summary_url).json()
            return summary.get("extract", None)

        return None

    except:
        return None


# ================== WEB SEARCH ==================
def web_search(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
        res = requests.get(url).json()

        results = []

        if res.get("AbstractText"):
            results.append(res["AbstractText"])

        if res.get("RelatedTopics"):
            for item in res["RelatedTopics"][:5]:
                if "Text" in item:
                    results.append(item["Text"])

        return "\n\n".join(results) if results else None

    except:
        return None


# ================== 🧠 AI REASONING ENGINE ==================
def reasoning_engine(query, wiki, web):

    q = query.lower()

    # 1. Definition-style question
    if "what is" in q or "define" in q:
        return f"📘 Definition Answer:\n{wiki or web}"

    # 2. How / process questions
    if "how" in q:
        return f"⚙️ Step-by-step explanation:\n{web or wiki}"

    # 3. Why questions (causal reasoning)
    if "why" in q:
        return f"🧠 Reasoning Explanation:\n{web or wiki}"

    # 4. Who / where (factual lookup)
    if "who" in q or "where" in q:
        return f"📍 Factual Information:\n{wiki or web}"

    # 5. List-based queries
    if "list" in q or "types" in q or "examples" in q:
        return f"📋 Structured Information:\n{web or wiki}"

    # 6. Yes/No or simple questions
    if q.endswith("?"):
        return f"💬 Direct Answer:\n{wiki or web}"

    # 7. General reasoning (ChatGPT-like style)
    if wiki and web:
        return (
            "🧠 Combined Knowledge Answer:\n\n"
            f"{wiki}\n\n"
            "🌐 Additional Context:\n"
            f"{web}"
        )

    # fallback
    return wiki or web or "❌ No good answer found."


# ================== LINKS ==================
def google_link(q):
    return f"https://www.google.com/search?q={q}"

def youtube_link(q):
    return f"https://www.youtube.com/results?search_query={q}"


# ================== MAIN PROCESS ==================
def process_query(user):

    print("\n🧠 Thinking...\n")

    # STEP 1: Collect knowledge
    wiki = wiki_search(user)
    web = web_search(user)

    # STEP 2: AI reasoning layer
    answer = reasoning_engine(user, wiki, web)

    # STEP 3: Output
    print(answer)

    # STEP 4: fallback if weak
    if not wiki and not web:
        print("\n⚠️ No strong result found.")
        print("🌐 Google:", google_link(user))
        print("▶️ YouTube:", youtube_link(user))


# ================== CHAT LOOP ==================
while True:
    user = input("Mekonnen AI: ")

    if user.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    process_query(user)

    print("\n" + "-" * 80 + "\n")