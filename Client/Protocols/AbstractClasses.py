from abc import ABCMeta, abstractmethod
import json


class Services:
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, value_id):
        pass

    @abstractmethod
    def update_by_value(self, value):
        pass

    @abstractmethod
    def delete_by_id(self, value_id):
        pass


class User:
    def __init__(self, _id=0, name="", age=0):
        self.Id = _id
        self.Name = name
        self.Age = age

    def from_json(self, json_str):
        self.Id = json_str["Id"]
        self.Name = json_str["Name"]
        self.Age = json_str["Age"]


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Topic:
    def __init__(self, _id=0, name=""):
        self.Id = _id
        self.Name = name

    def from_json(self, json_str):
        self.Id = json_str["Id"]
        self.Name = json_str["Name"]


class TopicEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Topic):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class ContentType:
    def __init__(self, _id=0, name=""):
        self.Id = _id
        self.Name = name

    def from_json(self, json_str):
        self.Id = json_str["Id"]
        self.Name = json_str["Name"]


class ContentTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ContentType):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Content:
    def __init__(self, _id=0, _tutorial_id=0, _tutorial_type_id=0, _price=0, _data=""):
        self.Id = _id
        self.TopicsId = _tutorial_id
        self.ContentTypeId = _tutorial_type_id
        self.Price = _price
        self.Data = _data

    def from_json(self, json_str):
        self.Id = json_str["Id"]
        self.TopicsId = json_str["TopicsId"]
        self.ContentTypeId = json_str["ContentTypeId"]
        self.Price = json_str["Price"]
        self.Data = json_str["Data"]


class ContentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Content):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Subscription:
    def __init__(self, _id=0, _user_id=0, _content_id=0):
        self.Id = _id
        self.UserId = _user_id
        self.ContentId = _content_id

    def from_json(self, json_str):
        self.Id = json_str["Id"]
        self.UserId = json_str["UserId"]
        self.ContentId = json_str["ContentId"]


class SubscriptionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Subscription):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
