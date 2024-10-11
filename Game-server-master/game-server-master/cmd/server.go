package main

import (
	"fmt"
	"io"
	"net"
	"os"
	"strconv"
	"time"

	"github.com/gustaxz/arrax/internal/server"
	"github.com/gustaxz/arrax/pkg/cmds"
)

func handleConnection(conn net.Conn, server *server.Server) {
	for {
		buf := make([]byte, 1024)
		_, err := conn.Read(buf)
		if err != nil {
			if err == io.EOF {
				fmt.Println("Connection closed")
				return
			}
			fmt.Println("Error reading: ", err.Error(), err)
			return
		}
		defer conn.Close()

		cmds.ParseCommand(server, buf, conn)
	}
}

func broadcastInfos(server *server.Server, tick time.Duration) {
	fmt.Println("Broadcasting player positions")
	for {
		for _, client := range server.ClientsIDs {
			packet := cmds.EncodeMove(client, server.PlayersPositions[client])
			server.Broadcast(packet)
		}
		time.Sleep(tick)
	}
}

func main() {
	tickServer := 1000 * time.Millisecond

	if len(os.Args) > 1 {
		tick, err := strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Println("Invalid tick value")
			return
		}
		tickServer = time.Duration(tick) * time.Millisecond
	}

	tcpServer, err := net.Listen("tcp", ":5678")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer tcpServer.Close()
	fmt.Println("server started on: ", tcpServer.Addr())

	server := server.NewServer()

	go broadcastInfos(server, tickServer)

	for {
		conn, err := tcpServer.Accept()
		if err != nil {
			fmt.Println("Error accepting connection: ", err.Error())
			return
		}
		fmt.Println("Accepted connection from: ", conn.RemoteAddr())
		go handleConnection(conn, server)

	}
}
