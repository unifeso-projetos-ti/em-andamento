package cmds

import (
	"encoding/binary"
)

func DecodeMove(data []byte) (uint64, [3]uint64) {
	clientID := binary.LittleEndian.Uint64(data[1:])
	position := [3]uint64{
		binary.LittleEndian.Uint64(data[9:]),
		binary.LittleEndian.Uint64(data[17:]),
		binary.LittleEndian.Uint64(data[25:]),
	}
	return clientID, position
}

func EncodeMove(clientID uint64, position [3]uint64) []byte {
	data := make([]byte, 33)
	data[0] = PLAYER_MOVE
	binary.LittleEndian.PutUint64(data[1:], clientID)
	binary.LittleEndian.PutUint64(data[9:], position[0])
	binary.LittleEndian.PutUint64(data[17:], position[1])
	binary.LittleEndian.PutUint64(data[25:], position[2])
	return data
}
