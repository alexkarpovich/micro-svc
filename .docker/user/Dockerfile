FROM golang:1.11

COPY ./user /go/src/github.com/alexkarpovich/quiqstee-user
WORKDIR /go/src/github.com/alexkarpovich/quiqstee-user

RUN apt-get update && apt-get install -y unzip

RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.7.0rc1/protoc-3.7.0-rc1-linux-x86_64.zip
RUN unzip -o protoc-3.7.0-rc1-linux-x86_64.zip -d /usr/local
RUN rm -f protoc-3.7.0-rc1-linux-x86_64.zip

RUN go get -u \
  github.com/canthefason/go-watcher \
  github.com/golang/protobuf/protoc-gen-go \
  github.com/golang/protobuf/proto \
  google.golang.org/grpc \
  github.com/pressly/goose/cmd/goose

RUN go install github.com/canthefason/go-watcher/cmd/watcher
RUN go install github.com/golang/protobuf/protoc-gen-go
RUN go build -tags='no_mysql no_sqlite no_psql' -i -o goose github.com/pressly/goose/cmd/goose

RUN go get ./...

CMD watcher -run github.com/alexkarpovich/quiqstee-user/cmd -watch github.com/alexkarpovich/quiqstee-user
