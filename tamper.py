import os
import sys
import signal
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify the files you want to protect
protected_files = ['file1.txt', 'file2.txt', 'file3.txt']

# Define a custom event handler class
class FileProtectionHandler(FileSystemEventHandler):
    def __init__(self):
        self.observer = Observer()

    def on_any_event(self, event):
        filename = os.path.basename(event.src_path)
        if filename in protected_files:
            print(f"Attempted action on protected file: {event.event_type} - {filename}")
            if event.event_type in ('deleted', 'moved', 'renamed'):
                # Prevent the action by restoring the file
                print(f"Restoring {filename}...")
                time.sleep(0.1)  # Add a small delay to avoid conflicts with the event loop
                os.rename(event.src_path, event.src_path)

# Register a signal handler to prevent termination
def signal_handler(signal, frame):
    print("Process termination is not allowed.")
    signal.signal(signal.SIGINT, signal_handler)

# Create an instance of the event handler
event_handler = FileProtectionHandler()

# Start the observer
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)
observer.start()

# Run indefinitely until terminated
print("File protection script is running...")
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        break

# Clean up and exit
observer.join()
import os
import sys
import signal
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify the files you want to protect
protected_files = ['file1.txt', 'file2.txt', 'file3.txt']

# Define a custom event handler class
class FileProtectionHandler(FileSystemEventHandler):
    def __init__(self):
        self.observer = Observer()

    def on_any_event(self, event):
        filename = os.path.basename(event.src_path)
        if filename in protected_files:
            print(f"Attempted action on protected file: {event.event_type} - {filename}")
            if event.event_type in ('deleted', 'moved', 'renamed'):
                # Prevent the action by restoring the file
                print(f"Restoring {filename}...")
                time.sleep(0.1)  # Add a small delay to avoid conflicts with the event loop
                os.rename(event.src_path, event.src_path)

# Register a signal handler to prevent termination
def signal_handler(signal, frame):
    print("Process termination is not allowed.")
    signal.signal(signal.SIGINT, signal_handler)

# Create an instance of the event handler
event_handler = FileProtectionHandler()

# Start the observer
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)
observer.start()

# Run indefinitely until terminated
print("File protection script is running...")
while True:
    try:
        time.sleep(1)
   
# Clean up and exit
observer.join()
