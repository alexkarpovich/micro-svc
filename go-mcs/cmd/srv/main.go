package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	pb "github.com/alexkarpovich/micro-svc/service"
)

const (
	port = "0.0.0.0:50052"
)

type server struct{}

func (s *server) SnipIt(ctx context.Context, in *pb.SnipRequest) (*pb.SnipResponse, error) {
	log.Printf("Received: %v", in.Url)
	return &pb.SnipResponse{Url: "Hello " + in.Url}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterUrlSnipServiceServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}