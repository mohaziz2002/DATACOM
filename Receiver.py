import socket
import Algorithms

HOST = '127.0.0.1'
PORT = 65433

def main():
    print("Receiver App Waiting...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    
    while True:
        try:
            raw = conn.recv(4096).decode('utf-8')
            if not raw:
                break
                
            print("\nNew Packet Received:")
            print(f"Raw: {raw}")
            
            parts = raw.split('|')
            if len(parts) < 3:
                continue
                
            data_str = parts[0]
            met = parts[1]
            old_code = parts[2]
            
            # Check for errors
            res, new_code = Algorithms.check_data(data_str, met, old_code)
            
            print(f"Data: {data_str}")
            print(f"Method: {met}")
            print(f"Received Code: {old_code}")
            print(f"Calculated Code: {new_code}")
            print(f"RESULT: {res}")
            
        except Exception as e:
            print(e)
            break
            
    conn.close()
    s.close()

if __name__ == "__main__":
    main()