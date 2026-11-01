import sys, time, ollama

# Pick the model from the command line, e.g.: python bench.py qwen2.5-coder:3b
MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5-coder:7b"
PROMPT = "Write a Python function that checks whether a string is a palindrome, with 3 unit tests."
NUM_CTX = 4096
THREADS = [4, 6, 8]   # thread counts to compare

print(f"Model: {MODEL}")
for n in THREADS:
    t0 = time.time()
    r = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT}],
        options={
            "num_ctx": NUM_CTX,
            "num_thread": n,
            "num_predict": 120,   # stop after 120 tokens so each test is quick
            "temperature": 0,
        },
        keep_alive="30m",
    )
    wall = time.time() - t0
    tps = r["eval_count"] / (r["eval_duration"] / 1e9)
    load = r["load_duration"] / 1e9
    print(f"num_thread={n}: {tps:.1f} tok/s, load {load:.1f}s, total {wall:.1f}s")