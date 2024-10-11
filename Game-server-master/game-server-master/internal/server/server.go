package server

import (
	"fmt"
	"net"
)

type Server struct {
	ClientsIDs       []uint64
	PlayersPositions map[uint64][3]uint64
	ClientsConn      map[uint64]net.Conn
}

func NewServer() *Server {
	return &Server{
		PlayersPositions: make(map[uint64][3]uint64),
		ClientsConn:      make(map[uint64]net.Conn),
	}
}

func (s *Server) AddClient(clientID uint64, conn net.Conn) {
	s.ClientsIDs = append(s.ClientsIDs, clientID)
	s.PlayersPositions[clientID] = [3]uint64{0, 0, 0}
	s.ClientsConn[clientID] = conn
	fmt.Println("Client added: ", clientID)
}

func (s *Server) RemoveClient(clientID uint64) {
	for i, id := range s.ClientsIDs {
		if id == clientID {
			s.ClientsIDs = append(s.ClientsIDs[:i], s.ClientsIDs[i+1:]...)
			delete(s.PlayersPositions, clientID)
			fmt.Println("Client removed: ", clientID)
			return
		}
	}
}

func (s *Server) UpdatePlayerPosition(clientID uint64, position [3]uint64) {
	s.PlayersPositions[clientID] = position
	fmt.Println("Player position updated: ", clientID, position)
}

func (s *Server) Broadcast(data []byte) {
	for _, client := range s.ClientsIDs {
		s.ClientsConn[client].Write(data)
	}
}
