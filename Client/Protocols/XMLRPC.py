from Protocols import AbstractClasses
import xmlrpc.client
import json

global server


class Protocol:
    user = None
    topic = None
    content_type = None
    content = None
    subscription = None

    def __init__(self, url):
        global server
        server = xmlrpc.client.ServerProxy(url)
        self.user = self.User()
        self.topic = self.Topic()
        self.content_type = self.ContentType()
        self.content = self.Content()
        self.subscription = self.Subscription()

    class User(AbstractClasses.Services):
        def add(self, value=AbstractClasses.User):
            server.AddUser(json.dumps(value, cls=AbstractClasses.UserEncoder))

        def get_all(self):
            users = []
            for item in str(server.GetAllUsers()).split('&'):
                user = AbstractClasses.User()
                user.from_json(json.loads(item))
                users.append(user)
            return users

        def get_by_id(self, value_id):
            user = server.GetUserById(str(value_id))
            return json.loads(user)

        def update_by_value(self, value=AbstractClasses.User):
            temp = json.dumps(value, cls=AbstractClasses.UserEncoder)
            server.UpdateUser(temp)

        def delete_by_id(self, value_id):
            return server.DeleteUser(str(value_id))

    class Topic(AbstractClasses.Services):
        def add(self, value=AbstractClasses.Topic):
            server.AddTopic(json.dumps(value, cls=AbstractClasses.TopicEncoder))

        def get_all(self):
            tutorials = []
            for item in str(server.GetAllTopics()).split('&'):
                tutorial = AbstractClasses.Topic()
                tutorial.from_json(json.loads(item))
                tutorials.append(tutorial)
            return tutorials

        def get_by_id(self, value_id):
            tutorial = server.GetTopicById(str(value_id))
            return json.loads(tutorial)

        def update_by_value(self, value=AbstractClasses.Topic):
            temp = json.dumps(value, cls=AbstractClasses.TopicEncoder)
            server.UpdateTopic(temp)

        def delete_by_id(self, value_id):
            return server.DeleteTopic(str(value_id))

    class ContentType(AbstractClasses.Services):
        def add(self, value=AbstractClasses.ContentType):
            server.AddContentType(json.dumps(value, cls=AbstractClasses.ContentTypeEncoder))

        def get_all(self):
            contentTypes = []
            for item in str(server.GetAllContentTypes()).split('&'):
                content_type = AbstractClasses.ContentType()
                content_type.from_json(json.loads(item))
                contentTypes.append(content_type)
            return contentTypes

        def get_by_id(self, value_id):
            content_type = server.GetContentTypeById(str(value_id))
            return json.loads(content_type)

        def update_by_value(self, value=AbstractClasses.ContentType):
            temp = json.dumps(value, cls=AbstractClasses.ContentTypeEncoder)
            server.UpdateContentType(temp)

        def delete_by_id(self, value_id):
            return server.DeleteContentType(str(value_id))

    class Content(AbstractClasses.Services):
        def add(self, value=AbstractClasses.Content):
            server.AddContent(json.dumps(value, cls=AbstractClasses.ContentEncoder))

        def get_all(self):
            contents = []
            for item in str(server.GetAllContents()).split('&'):
                content = AbstractClasses.Content()
                content.from_json(json.loads(item))
                contents.append(content)
            return contents

        def get_by_id(self, value_id):
            content = server.GetContentById(str(value_id))
            return json.loads(content)

        def update_by_value(self, value=AbstractClasses.Content):
            temp = json.dumps(value, cls=AbstractClasses.ContentEncoder)
            server.UpdateContent(temp)

        def delete_by_id(self, value_id):
            return server.DeleteContent(str(value_id))

    class Subscription(AbstractClasses.Services):
        def add(self, value=AbstractClasses.Subscription):
            server.AddSubscription(json.dumps(value, cls=AbstractClasses.SubscriptionEncoder))

        def get_all(self):
            subscriptions = []
            print(server.GetAllSubscriptions())
            for item in str(server.GetAllSubscriptions()).split('&'):
                subscription = AbstractClasses.Subscription()
                subscription.from_json(json.loads(item))
                subscriptions.append(subscription)
            return subscriptions

        def get_by_id(self, value_id):
            subscription = server.GetSubscriptionById(str(value_id))
            return json.loads(subscription)

        def update_by_value(self, value=AbstractClasses.Subscription):
            temp = json.dumps(value, cls=AbstractClasses.SubscriptionEncoder)
            server.UpdateSubscription(temp)

        def delete_by_id(self, value_id):
            return server.DeleteSubscription(str(value_id))

# def get_list_methods(self):
#     return self.server.system.listMethods()
