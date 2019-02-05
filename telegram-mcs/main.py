import grpc
import logging
import threading
from concurrent import futures

from bot import bot
from proto.snip_pb2_grpc import add_UrlSnipServiceServicer_to_server, UrlSnipServiceServicer


def run_telegram_bot():
    bot.polling(none_stop=True)

def run_grpc_server():
    logging.info('Start grpc server')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UrlSnipServiceServicer_to_server(
      UrlSnipServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()

if __name__=='__main__':
    telegram_thread = threading.Thread(target=run_telegram_bot)
    grpc_thread = threading.Thread(target=run_grpc_server)
    telegram_thread.start()
    grpc_thread.start()
