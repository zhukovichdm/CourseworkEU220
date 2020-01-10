from Protocols import AbstractClasses
from zeep import Client
import json


# python -mzeep URL


class Protocol:
    user = None
    topic = None
    content_type = None
    content = None
    subscription = None

    def __init__(self, url):
        global client
        client = Client(wsdl=url)
        self.user = self.User()
        self.topic = self.Topic()
        self.content_type = self.ContentType()
        self.content = self.Content()
        self.subscription = self.Subscription()

    class User(AbstractClasses.Services):
        def add(self, value):
            client.service.AddUser(json.dumps(value, cls=AbstractClasses.UserEncoder))

        def get_all(self):
            arr = []
            for item in str(client.service.GetAllUsers()).split('&'):
                temp = AbstractClasses.User()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            temp = client.service.GetUserById(str(value_id))
            return json.loads(temp)

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.UserEncoder)
            client.service.UpdateUser(temp)

        def delete_by_id(self, value_id):
            return client.service.DeleteUser(str(value_id))

    class Topic(AbstractClasses.Services):
        def add(self, value):
            client.service.AddTopic(json.dumps(value, cls=AbstractClasses.TopicEncoder))

        def get_all(self):
            arr = []
            for item in str(client.service.GetAllTopics()).split('&'):
                temp = AbstractClasses.Topic()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            temp = client.service.GetTopicById(str(value_id))
            return json.loads(temp)

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.TopicEncoder)
            client.service.UpdateTopic(temp)

        def delete_by_id(self, value_id):
            return client.service.DeleteTopic(str(value_id))

    class ContentType(AbstractClasses.Services):
        def add(self, value):
            client.service.AddContentType(json.dumps(value, cls=AbstractClasses.ContentTypeEncoder))

        def get_all(self):
            arr = []
            for item in str(client.service.GetAllContentTypes()).split('&'):
                temp = AbstractClasses.ContentType()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            temp = client.service.GetContentTypeById(str(value_id))
            return json.loads(temp)

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.ContentTypeEncoder)
            client.service.UpdateContentType(temp)

        def delete_by_id(self, value_id):
            return client.service.DeleteContentType(str(value_id))

    class Content(AbstractClasses.Services):
        def add(self, value):
            client.service.AddContent(json.dumps(value, cls=AbstractClasses.ContentEncoder))

        def get_all(self):
            arr = []
            for item in str(client.service.GetAllContents()).split('&'):
                temp = AbstractClasses.Content()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            temp = client.service.GetContentById(str(value_id))
            return json.loads(temp)

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.ContentEncoder)
            client.service.UpdateContent(temp)

        def delete_by_id(self, value_id):
            return client.service.DeleteContent(str(value_id))

    class Subscription(AbstractClasses.Services):
        def add(self, value):
            client.service.AddSubscription(json.dumps(value, cls=AbstractClasses.SubscriptionEncoder))

        def get_all(self):
            arr = []
            for item in str(client.service.GetAllSubscriptions()).split('&'):
                temp = AbstractClasses.Subscription()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            temp = client.service.GetSubscriptionById(str(value_id))
            return json.loads(temp)

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.SubscriptionEncoder)
            client.service.UpdateSubscription(temp)

        def delete_by_id(self, value_id):
            return client.service.DeleteSubscription(str(value_id))
