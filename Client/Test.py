from Protocols import XMLRPC, REST, SOAP


class Connection:
    # xmlrpc = XMLRPC.Protocol('http://localhost:57317/XMLRPCHandler.ashx')
    # rest = REST.Protocol('http://localhost:57317/RESTService.svc/')
    # soap = SOAP.Protocol('http://localhost:57320/SOAPService.svc?wsdl')

    protocols = {
        0: "XMLRPC",
        1: "REST",
        2: "SOAP"
    }

    def get(self, protocol_name):
        print("Used protocol:" + protocol_name)

        if protocol_name == "XMLRPC":
            return XMLRPC.Protocol('http://localhost:57317/XMLRPCHandler.ashx')
        if protocol_name == "REST":
            return XMLRPC.Protocol('http://localhost:57317/XMLRPCHandler.ashx')
        if protocol_name == "SOAP":
            return SOAP.Protocol('http://localhost:57320/SOAPService.svc?wsdl')


if __name__ == "__main__":
    connection = Connection()
    # xmlrpcConnection = connection.get("XMLRPC")
    restConnection = connection.get("REST")
    # soapConnection = connection.get("SOAP")

    # TODO: Все пользователи
    temp = restConnection.user.get_all()
    print(temp[0].Name)
    # TODO: Добавление
    # newUser = User(0, "New", 12)
    # jsonUser = json.dumps(newUser, cls=UserEncoder)
    # xmlrpcConnection.user.add(jsonUser)

    # TODO: Удаление по Id
    # xmlrpcConnection.user.delete_by_id(1002)

    # TODO: Пользователь по Id
    # tempUser = AbstractClasses.User()
    # tempUser.from_json(xmlrpcConnection.user.get_by_id(1))
    # print(tempUser.Name)

    # TODO: Обновить пользователя
    # tempUser.Name = "Tom"
    # xmlrpcConnection.user.update_by_value(tempUser)

    # TODO: Обновление по значению
    # xmlrpcConnection.user.update_by_value()

    # TODO: Все пользователи
    # temp = xmlrpcConnection.user.get_all()
    # print(temp)
