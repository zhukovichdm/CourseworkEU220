using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using CookComputing.XmlRpc;
using REST_XMLRPC.EntityFramework;

namespace REST_XMLRPC
{
    /// <summary>
    /// Сводное описание для XMLRPCHandler
    /// </summary>
    public class XMLRPCHandler : XmlRpcService
    {
        #region Users

        [XmlRpcMethod("GetAllUsers")]
        public string GetAllUsers() => MyServices.GetAllUsers();

        [XmlRpcMethod("GetUserById")]
        public string GetUserById(string userId) => MyServices.GetUserById(userId);

        [XmlRpcMethod("AddUser")]
        public void AddUser(string json) => MyServices.AddUser(json);

        [XmlRpcMethod("DeleteUser")]
        public void DeleteUser(string userId) => MyServices.DeleteUser(userId);

        [XmlRpcMethod("UpdateUser")]
        public void UpdateUser(string json) => MyServices.UpdateUser(json);

        #endregion

        #region Topics

        [XmlRpcMethod("GetAllTopics")]
        public string GetAllTopics() => MyServices.GetAllTopics();

        [XmlRpcMethod("GetTopicById")]
        public string GetTopicById(string userId) => MyServices.GetTopicById(userId);

        [XmlRpcMethod("AddTopic")]
        public void AddTopic(string json) => MyServices.AddTopic(json);

        [XmlRpcMethod("DeleteTopic")]
        public void DeleteTopic(string userId) => MyServices.DeleteTopic(userId);

        [XmlRpcMethod("UpdateTopic")]
        public void UpdateTopic(string json) => MyServices.UpdateTopic(json);

        #endregion

        #region ContentTypes

        [XmlRpcMethod("GetAllContentTypes")]
        public string GetAllContentTypes() => MyServices.GetAllContentTypes();

        [XmlRpcMethod("GetContentTypeById")]
        public string GetContentTypeById(string userId) => MyServices.GetContentTypeById(userId);

        [XmlRpcMethod("AddContentType")]
        public void AddContentType(string json) => MyServices.AddContentType(json);

        [XmlRpcMethod("DeleteContentType")]
        public void DeleteContentType(string userId) => MyServices.DeleteContentType(userId);

        [XmlRpcMethod("UpdateContentType")]
        public void UpdateContentType(string json) => MyServices.UpdateContentType(json);

        #endregion

        #region Contents

        [XmlRpcMethod("GetAllContents")]
        public string GetAllContents() => MyServices.GetAllContents();

        [XmlRpcMethod("GetContentById")]
        public string GetContentById(string userId) => MyServices.GetContentById(userId);

        [XmlRpcMethod("AddContent")]
        public void AddContent(string json) => MyServices.AddContent(json);

        [XmlRpcMethod("DeleteContent")]
        public void DeleteContent(string userId) => MyServices.DeleteContent(userId);

        [XmlRpcMethod("UpdateContent")]
        public void UpdateContent(string json) => MyServices.UpdateContent(json);

        #endregion

        #region Subscriptions

        [XmlRpcMethod("GetAllSubscriptions")]
        public string GetAllSubscriptions() => MyServices.GetAllSubscriptions();

        [XmlRpcMethod("GetSubscriptionById")]
        public string GetSubscriptionById(string userId) => MyServices.GetSubscriptionById(userId);

        [XmlRpcMethod("AddSubscription")]
        public void AddSubscription(string json) => MyServices.AddSubscription(json);

        [XmlRpcMethod("DeleteSubscription")]
        public void DeleteSubscription(string userId) => MyServices.DeleteSubscription(userId);

        [XmlRpcMethod("UpdateSubscription")]
        public void UpdateSubscription(string json) => MyServices.UpdateSubscription(json);

        #endregion
    }
}