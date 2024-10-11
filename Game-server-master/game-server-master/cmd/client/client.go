package main

import (
	"bufio"
	"fmt"
	"net"
	"os"

	"github.com/gustaxz/arrax/internal/client"
)

func terminalClient(cli *client.Client, conn net.Conn) {
	for {
		fmt.Print("Enter text: ")
		data, err := bufio.NewReader(os.Stdin).ReadString('\n')
		if err != nil {
			fmt.Println(err)
			return
		}

		packet, err := client.ParseCommands(cli, data)
		if err != nil {
			fmt.Println(err)
			continue
		}
		conn.Write(packet)
	}
}

func main() {
	debug := false

	if len(os.Args) > 1 {
		if os.Args[1] == "-d" {
			debug = true
		}
	}

	// Resolve the string address to a TCP address
	tcpAddr, err := net.ResolveTCPAddr("tcp4", ":5678")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Connect to the address with tcp
	conn, err := net.DialTCP("tcp", nil, tcpAddr)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println("Connected to server: ", conn.RemoteAddr())
	clientStruct := client.NewClient(conn)
	clientStruct.Ack()

	go terminalClient(clientStruct, conn)

	for {
		// Read from the connection untill a new line is send
		data := make([]byte, 1024)
		_, err := bufio.NewReader(conn).Read(data[:])
		if err != nil {
			if err.Error() == "EOF" {
				fmt.Println("Connection closed")
				return
			}
			fmt.Println(err)
			return
		}

		if debug {
			client.ParseServerResponse(data)
		}
	}
}
