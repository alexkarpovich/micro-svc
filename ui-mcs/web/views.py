import grpc
from django.http import HttpResponse
from proto.snip_pb2 import SnipRequest
from proto.snip_pb2_grpc import UrlSnipServiceStub

def homePageView(request):
	channel = grpc.insecure_channel('golang:50052')
	stub = UrlSnipServiceStub(channel)
	request = SnipRequest(url="Alex")
	response = stub.snip_it(request)

	return HttpResponse(response.url)

def telegramView(request):
	channel = grpc.insecure_channel('telegram:50053')
	stub = UrlSnipServiceStub(channel)
	request = SnipRequest(url="Telega")
	response = stub.snip_it(request)

	return HttpResponse(response.url)
