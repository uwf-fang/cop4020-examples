import time
import threading
import queue

class Event:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data

class EventDispatcher:
    def __init__(self):
        self._listeners = {}

    def register(self, event_name, listener):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)

    def dispatch(self, event):
        if event.name in self._listeners:
            for listener in self._listeners[event.name]:
                listener(event)

class EventLoop:
    def __init__(self, dispatcher):
        self.event_queue = queue.Queue()
        self.dispatcher = dispatcher
        self.running = True

    def run(self):
        while self.running:
            try:
                event = self.event_queue.get(timeout=1)  # Wait for 1 second
                self.dispatcher.dispatch(event)
            except queue.Empty:
                pass  # Queue was empty, continue loop
            except Exception as e:
                print(f"Error in event loop: {e}")

    def stop(self):
        self.running = False

    def enqueue_event(self, event):
        self.event_queue.put(event)

# Listener functions
def log_event(event):
    print(f"Logging: Event '{event.name}' with data: {event.data}")

def process_data(event):
    if event.data:
        processed_data = event.data.upper()
        print(f"Processed: {processed_data}")
    else:
        print("No data to process.")

if __name__ == "__main__":
    dispatcher = EventDispatcher()
    event_loop = EventLoop(dispatcher)

    dispatcher.register("log", log_event)
    dispatcher.register("process", process_data)

    loop_thread = threading.Thread(target=event_loop.run)
    loop_thread.start()

    # Simulate event generation
    event_loop.enqueue_event(Event("log", {"message": "User login"}))
    time.sleep(0.5)
    event_loop.enqueue_event(Event("process", "test data"))
    time.sleep(0.5)
    event_loop.enqueue_event(Event("log", {"message": "Data processed"}))
    time.sleep(0.5)
    event_loop.enqueue_event(Event("process"))
    time.sleep(1.5)

    event_loop.stop()
    loop_thread.join()

    print("Event loop stopped.")
