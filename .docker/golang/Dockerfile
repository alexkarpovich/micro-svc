FROM golang:1.11

COPY ./go-mcs /go/src/github.com/alexkarpovich/micro-svc
WORKDIR /go/src/github.com/alexkarpovich/micro-svc

RUN apt-get update && apt-get install -y unzip

RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.7.0rc1/protoc-3.7.0-rc1-linux-x86_64.zip
RUN unzip -o protoc-3.7.0-rc1-linux-x86_64.zip -d /usr/local
RUN rm -f protoc-3.7.0-rc1-linux-x86_64.zip

RUN go get -u \
  github.com/canthefason/go-watcher \
  github.com/golang/protobuf/protoc-gen-go \
  github.com/golang/protobuf/proto \
  google.golang.org/grpc

RUN go install github.com/canthefason/go-watcher/cmd/watcher
RUN go install github.com/golang/protobuf/protoc-gen-go

EXPOSE 80

CMD watcher -run github.com/alexkarpovich/micro-svc/cmd/srv -watch github.com/alexkarpovich/micro-svc
