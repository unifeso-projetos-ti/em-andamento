package cmds

import (
	"net"

	"github.com/gustaxz/arrax/internal/server"
)

func ParseCommand(server *server.Server, data []byte, conn net.Conn) {
	switch data[0] {
	case REQUEST_CONNECTION:
		clientID := AckWithClient(data)
		server.AddClient(clientID, conn)
	case PLAYER_MOVE:
		clientID, position := DecodeMove(data)
		server.UpdatePlayerPosition(clientID, position)
	}
}
