import time

def countdown(signal, seconds):
    for i in range(seconds, 0, -1):
        print(f"{signal}: {i} seconds remaining")
        time.sleep(1)

while True:
    print("\n🚦 Traffic Signal Simulation 🚦")

    countdown("🔴 RED", 5)
    countdown("🟢 GREEN", 5)
    countdown("🟡 YELLOW", 2)