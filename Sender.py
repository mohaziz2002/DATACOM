import socket
import Algorithms 

HOST = '127.0.0.1'
PORT = 65432

def main():
    print("Sender App Started")
    
    while True:
        txt = input("\nEnter message (type 'exit' to stop): ")
        if txt == 'exit':
            break
            
        print("Methods: 1.Parity 2.2D-Parity 3.CRC 4.Hamming 5.Checksum")
        opt = input("Select method: ")
        
        m_name = "CRC" # default
        code = ""
        
        if opt == '1':
            m_name = "PARITY"
            code = Algorithms.get_parity(txt, 'even')
        elif opt == '2':
            m_name = "2D_PARITY"
            code = Algorithms.get_2d_parity(txt)
        elif opt == '3':
            m_name = "CRC"
            code = Algorithms.crc16(txt)
        elif opt == '4':
            m_name = "HAMMING"
            code = Algorithms.hamming_encode(txt)
        elif opt == '5':
            m_name = "CHECKSUM"
            code = Algorithms.checksum(txt)
        else:
            print("Wrong input, using CRC.")
            code = Algorithms.crc16(txt)
            
        # Prepare packet
        pkt = f"{txt}|{m_name}|{code}"
        print(f"Sending: {pkt}")
        
        # Send
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.send(pkt.encode('utf-8'))
            s.close()
        except:
            print("Server is offline.")

if __name__ == "__main__":
    main()