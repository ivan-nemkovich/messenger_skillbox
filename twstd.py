from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataRecived(self, data):
        self.transport.wriite(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()