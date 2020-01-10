from Protocols import AbstractClasses
import requests
import json

global url


class Protocol:
    # url = "http://localhost:57317/RESTService.svc/"
    user = None
    topic = None
    content_type = None
    content = None
    subscription = None

    def __init__(self, _url):
        global url
        url = _url
        self.user = self.User()
        self.topic = self.Topic()
        self.content_type = self.ContentType()
        self.content = self.Content()
        self.subscription = self.Subscription()

    class User(AbstractClasses.Services):
        def add(self, value):
            data = json.dumps(value, cls=AbstractClasses.UserEncoder)
            requests.post(url + '/User/Add/%s' % str(data), json=data)

        def get_all(self):
            arr = []
            for item in str(requests.get(url + 'Users/GetAll').json()).split('&'):
                temp = AbstractClasses.User()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            return requests.get(url + 'User/' + value_id).json()

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.UserEncoder)
            requests.post(url + '/User/Update/%s' % str(temp), json=temp)
            pass

        def delete_by_id(self, value_id):
            requests.post(url + '/User/DellById/%s' % str(value_id))

    class Topic(AbstractClasses.Services):
        def add(self, value):
            data = json.dumps(value, cls=AbstractClasses.TopicEncoder)
            requests.post(url + '/Topic/Add/%s' % str(data), json=data)

        def get_all(self):
            arr = []
            for item in str(requests.get(url + 'Topics/GetAll').json()).split('&'):
                temp = AbstractClasses.Topic()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            return requests.get(url + 'Topic/' + value_id).json()

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.TopicEncoder)
            requests.post(url + '/Topic/Update/%s' % str(temp), json=temp)
            pass

        def delete_by_id(self, value_id):
            requests.post(url + '/Topic/DellById/%s' % str(value_id))

    class ContentType(AbstractClasses.Services):
        def add(self, value):
            data = json.dumps(value, cls=AbstractClasses.ContentTypeEncoder)
            requests.post(url + '/ContentType/Add/%s' % str(data), json=data)

        def get_all(self):
            arr = []
            for item in str(requests.get(url + 'ContentTypes/GetAll').json()).split('&'):
                temp = AbstractClasses.ContentType()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            return requests.get(url + 'ContentType/' + value_id).json()

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.ContentTypeEncoder)
            requests.post(url + '/ContentType/Update/%s' % str(temp), json=temp)
            pass

        def delete_by_id(self, value_id):
            requests.post(url + '/ContentType/DellById/%s' % str(value_id))

    class Content(AbstractClasses.Services):
        def add(self, value):
            data = json.dumps(value, cls=AbstractClasses.ContentEncoder)
            requests.post(url + '/Content/Add/%s' % str(data), json=data)

        def get_all(self):
            arr = []
            for item in str(requests.get(url + 'Contents/GetAll').json()).split('&'):
                temp = AbstractClasses.Content()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            return requests.get(url + 'Content/' + value_id).json()

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.ContentEncoder)
            requests.post(url + '/Content/Update/%s' % str(temp), json=temp)
            pass

        def delete_by_id(self, value_id):
            requests.post(url + '/Content/DellById/%s' % str(value_id))

    class Subscription(AbstractClasses.Services):
        def add(self, value):
            data = json.dumps(value, cls=AbstractClasses.SubscriptionEncoder)
            requests.post(url + '/Subscription/Add/%s' % str(data), json=data)

        def get_all(self):
            arr = []
            for item in str(requests.get(url + 'Subscriptions/GetAll').json()).split('&'):
                temp = AbstractClasses.Subscription()
                temp.from_json(json.loads(item))
                arr.append(temp)
            return arr

        def get_by_id(self, value_id):
            return requests.get(url + 'Subscription/' + value_id).json()

        def update_by_value(self, value):
            temp = json.dumps(value, cls=AbstractClasses.SubscriptionEncoder)
            requests.post(url + '/Subscription/Update/%s' % str(temp), json=temp)
            pass

        def delete_by_id(self, value_id):
            requests.post(url + '/Subscription/DellById/%s' % str(value_id))


# json_data = json.loads(get_all_users())
# print(json_data['Name'])


# data = {"str": "saasdsad"}
# resp = requests.get(url + 'Tutorial')
# print(resp.content)
# resp = requests.get(url + 'Tutorial/1')
# print(resp.content)
# requests.post(url + 'Tutorial', json=data)
# requests.delete(url + 'Tutorial/0')
#
# resp = requests.get(url + 'Tutorial')
# print(resp.content)
