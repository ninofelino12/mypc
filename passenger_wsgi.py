import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'Selamat, kamu berhasil deploy aplikasi python di cloud hosting IDCloudHost\n'
    version = 'Python versi %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]
