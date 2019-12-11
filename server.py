from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)
        self.factory.logins.remove(self.login)

    def lineReceived(self, line: bytes):
        content = line.decode()

        if self.login is not None:
            content = f"Message from {self.login}: {content}"
            # Save history
            if len(self.factory.history) == 10:
                del self.factory.history[0]
                self.factory.history.append(content)
            else:
                self.factory.history.append(content)

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(content.encode())
        else:
            # login:admin -> admin
            if content.startswith("login:"):
                if content.replace("login:", "") not in self.factory.logins:
                    self.login = content.replace("login:", "")
                    self.factory.logins.append(self.login)
                    self.sendLine("Welcome!".encode())
                    self.send_history()
                else:
                    self.sendLine("Try another login!\nBye :)".encode())
                    self.transport.loseConnection()
            else:
                self.sendLine("Invalid login".encode())

    # Send history function
    def send_history(self):
        for msg in self.factory.history:
            self.sendLine(msg.encode())


class Server(ServerFactory):
    protocol = ServerProtocol
    clients: list
    logins: list
    history: list

    def startFactory(self):
        self.clients = []
        self.logins = []
        self.history = []
        print("Server started")

    def stopFactory(self):
        print("Server closed")


reactor.listenTCP(1234, Server())
reactor.run()
