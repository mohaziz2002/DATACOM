import socket
import random
import time

# Config
IP = '127.0.0.1'
PORT_IN = 65432
PORT_OUT = 65433

def make_error(packet):
    try:
        arr = packet.split('|')
        if len(arr) < 3:
            return packet
            
        txt = arr[0]
        chars = list(txt)
        
        # Random choice 1 to 7
        e = random.randint(1, 7)
        print(f"Server: Error Type {e} applied on '{txt}'")

        if len(chars) < 2:
            return packet

        # 1. Bit Flip
        if e == 1:
            i = random.randint(0, len(chars) - 1)
            val = ord(chars[i])
            chars[i] = chr(val ^ 1) 
            print(" -> Bit flipped")

        # 2. Substitution
        elif e == 2:
            i = random.randint(0, len(chars) - 1)
            chars[i] = 'X' 
            print(" -> Char replaced")

        # 3. Deletion
        elif e == 3:
            i = random.randint(0, len(chars) - 1)
            del chars[i]
            print(" -> Char deleted")

        # 4. Insertion
        elif e == 4:
            i = random.randint(0, len(chars))
            chars.insert(i, 'Z')
            print(" -> Char inserted")

        # 5. Swap
        elif e == 5:
            i = random.randint(0, len(chars) - 2)
            chars[i], chars[i+1] = chars[i+1], chars[i]
            print(" -> Swapped two chars")

        # 6. Multi Bit Flip
        elif e == 6:
            for _ in range(2):
                i = random.randint(0, len(chars) - 1)
                chars[i] = chr(ord(chars[i]) ^ 1)
            print(" -> Multiple bits flipped")

        # 7. Burst
        elif e == 7:
            length = min(len(chars), random.randint(3, 8))
            start = random.randint(0, len(chars) - length)
            for k in range(start, start + length):
                chars[k] = '*'
            print(" -> Burst error applied")

        arr[0] = "".join(chars)
        return "|".join(arr)

    except:
        return packet

def run():
    print("Server running...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT_IN))
    s.listen(1)
    print(f"Listening on {PORT_IN}")
    
    conn, addr = s.accept()
    print(f"Sender connected: {addr}")

    # Connect to Receiver
    print("Connecting to Receiver...")
    out_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    connected = False
    while not connected:
        try:
            out_sock.connect((IP, PORT_OUT))
            connected = True
            print("Connected to Receiver.")
        except:
            print("Receiver not ready, retrying...")
            time.sleep(2)

    while True:
        try:
            msg = conn.recv(4096).decode('utf-8')
            if not msg:
                break
            
            print(f"Got: {msg}")
            
            bad_msg = make_error(msg)
            print(f"Forwarding: {bad_msg}")
            out_sock.send(bad_msg.encode('utf-8'))
            print("-----------------")
            
        except Exception as x:
            print(x)
            break

    conn.close()
    out_sock.close()
    s.close()

if __name__ == "__main__":
    run()