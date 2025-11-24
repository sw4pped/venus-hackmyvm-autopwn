import sys
import asyncio
from sophia import get_sophia_password


async def blink_cursor(stop_event):
    blink_states = ["\u2190", "\u2191", "\u2192", "\u2193"]
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r[{blink_states[i]}]")
        sys.stdout.flush()
        await asyncio.sleep(0.15)
        i = (i + 1) % len(blink_states)


async def main():
    stop = asyncio.Event()

    blink_task = asyncio.create_task(blink_cursor(stop))

    sophia_password = await asyncio.to_thread(get_sophia_password)

    stop.set()
    await blink_task
    sys.stdout.write(f"\r[+] sophia: {sophia_password}\n")


if __name__ == "__main__":
    asyncio.run(main())
