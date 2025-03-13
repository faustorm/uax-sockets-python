# Ejecutar el servidor en un terminal:
python servidor.py

# Ejecutar el cliente en otra terminal o en otra máquina:
python cliente.py

# Para conectar con el servidor de otro compañero:
Cambia la IP "localhost" por la de tu compañero:

        client_socket.connect(("127.0.0.1", 12345))

Para que esto funcione debéis estar en la misma red

Con ipconfig/ifconfig podéis saber vuestra IP, usarás la IP local v4, que empieza por 192.168.x.x

## Comprobar que el puerto está abierto
### Windows
netstat -an | find "12345"

### Mac/Linux
sudo netstat -tulnp | grep 12345
