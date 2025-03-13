import socket

def servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    #Bin 0.0.0.0 significa que acepta cualquier IP
    server_socket.listen(5)

    print("[SERVIDOR] Esperando conexiones...")

    conn, addr = server_socket.accept()
    print(f"[SERVIDOR] Conectado a {addr}")

    while True:
        mensaje = conn.recv(1024).decode()
        if mensaje.lower() == "salir":
            print("[SERVIDOR] Cliente desconectado.")
            break
        print(f"[CLIENTE] {mensaje}")

        respuesta = input("[SERVIDOR] Escribe tu respuesta: ")
        conn.send(respuesta.encode())

    conn.close()

if __name__ == "__main__":
    servidor()
