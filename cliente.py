import socket

def cliente():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    while True:
        mensaje = input("[CLIENTE] Escribe un mensaje: ")
        client_socket.send(mensaje.encode())

        if mensaje.lower() == "salir":
            break

        respuesta = client_socket.recv(1024).decode()
        print(f"[SERVIDOR] {respuesta}")

    client_socket.close()

if __name__ == "__main__":
    cliente()
