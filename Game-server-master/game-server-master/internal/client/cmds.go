package client

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gustaxz/arrax/pkg/cmds"
)

func ParseCommands(client *Client, data string) ([]byte, error) {
	clearCmd := strings.Replace(data, "\n", "", -1)
	clearCmd = strings.Replace(clearCmd, "\r", "", -1)
	cmd := strings.Split(clearCmd, " ")

	switch cmd[0] {
	case "move":
		if len(cmd) != 4 {
			return nil, fmt.Errorf("comando inválido. Use: move <x> <y> <z>")
		}

		fmt.Println("Movendo para:", cmd[1], cmd[2], cmd[3])
		x, _ := strconv.ParseUint(cmd[1], 10, 64)
		y, _ := strconv.ParseUint(cmd[2], 10, 64)
		z, _ := strconv.ParseUint(cmd[3], 10, 64)
		return cmds.EncodeMove(client.ID, [3]uint64{x, y, z}), nil
	}

	return nil, nil
}

func ParseServerResponse(data []byte) {
	switch data[0] {
	case cmds.PLAYER_MOVE:
		clientID, position := cmds.DecodeMove(data)
		fmt.Println("Player moved: ", clientID, position)
	}
}
