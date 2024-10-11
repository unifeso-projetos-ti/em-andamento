package cmds

import (
	"encoding/binary"
	"net"
)

func AckWithServer(conn net.Conn, clientID uint64) {
	packet := make([]byte, 9)
	binary.LittleEndian.PutUint64(packet[1:], clientID)
	packet[0] = REQUEST_CONNECTION

	conn.Write(packet)
}

func AckWithClient(data []byte) uint64 {
	return binary.LittleEndian.Uint64(data[1:])
}
