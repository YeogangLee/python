import socket 
from _thread import *

def threaded(client_socket, addr): 

    print('Connected by :', addr[0], ':', addr[1]) 

    while True: 

        try:
            data = client_socket.recv(1024)

            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('Received from ' + addr[0],':',addr[1] , data.decode())
            
            for cs in client_sockets :
                cs.send(data) 

            # client_socket.send(data) 
            # client_socket.sendall(data) 

        except :

            for idx, cs in enumerate(client_sockets) :
                if cs == client_socket:
                    client_sockets.pop(idx)
                    print("idx", idx)
            
            print('Disconnected by ' + addr[0],':',addr[1])
            print("현재 접속자 수 : ",len(client_sockets))
            break
             
    client_socket.close() 


HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

client_sockets = []


print('server start')

while True: 
    print('wait')
    client_socket, addr = server_socket.accept()
    client_sockets.append(client_socket) # 추가, 얘를 없애면 에코서버가 아니다, 곧 죽어. 
    start_new_thread(threaded, (client_socket, addr))
    # addr 청주에서 왔어, 몇 포트로 왔어, 너네가 알아서 해라하고 보내버리기
    # 일종의 명부, 어디에서 온 손님 몇번방으로 갔다. 작성
    # sendall()은 붙어있는애들 다 보내버리는 거 같아요
    # 이게 자바에는 없어
    # 자바는 
    # 랜선이 뽑히면, QOS, 인식을 해야 한다.
    # 소켓 통신이 뭐라고 했어요?
    # 이렇게이렇게이렇게 이어져서 3핸드셰이크 한다고 했지?
    # 가상적으로 연결된 것처럼 구현시켜놨다
    
    

server_socket.close() 