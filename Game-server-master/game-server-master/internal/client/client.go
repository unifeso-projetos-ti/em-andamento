package client

import (
	"math/rand/v2"
	"net"

	"github.com/gustaxz/arrax/pkg/cmds"
)

type Client struct {
	Conn net.Conn
	ID   uint64
}

func NewClient(conn net.Conn) *Client {
	clientID := rand.Uint64()
	return &Client{Conn: conn, ID: clientID}
}

func (c *Client) Ack() {
	cmds.AckWithServer(c.Conn, c.ID)
}
