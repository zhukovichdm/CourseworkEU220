using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using REST_XMLRPC.EntityFramework;

namespace SOAP
{
    // ПРИМЕЧАНИЕ. Команду "Переименовать" в меню "Рефакторинг" можно использовать для одновременного изменения имени класса "SOAPService" в коде, SVC-файле и файле конфигурации.
    // ПРИМЕЧАНИЕ. Чтобы запустить клиент проверки WCF для тестирования службы, выберите элементы SOAPService.svc или SOAPService.svc.cs в обозревателе решений и начните отладку.
    public class SOAPService : ISOAPService
    {
        #region Users

        public string GetAllUsers() => MyServices.GetAllUsers();

        public string GetUserById(string userId) => MyServices.GetUserById(userId);

        public void AddUser(string json) => MyServices.AddUser(json);

        public void DeleteUser(string userId) => MyServices.DeleteUser(userId);

        public void UpdateUser(string json) => MyServices.UpdateUser(json);

        #endregion

        #region Topics

        public string GetAllTopics() => MyServices.GetAllTopics();

        public string GetTopicById(string userId) => MyServices.GetTopicById(userId);

        public void AddTopic(string json) => MyServices.AddTopic(json);

        public void DeleteTopic(string userId) => MyServices.DeleteTopic(userId);

        public void UpdateTopic(string json) => MyServices.UpdateTopic(json);

        #endregion

        #region ContentTypes

        public string GetAllContentTypes() => MyServices.GetAllContentTypes();

        public string GetContentTypeById(string userId) => MyServices.GetContentTypeById(userId);

        public void AddContentType(string json) => MyServices.AddContentType(json);

        public void DeleteContentType(string userId) => MyServices.DeleteContentType(userId);

        public void UpdateContentType(string json) => MyServices.UpdateContentType(json);

        #endregion

        #region Contents

        public string GetAllContents() => MyServices.GetAllContents();

        public string GetContentById(string userId) => MyServices.GetContentById(userId);

        public void AddContent(string json) => MyServices.AddContent(json);

        public void DeleteContent(string userId) => MyServices.DeleteContent(userId);

        public void UpdateContent(string json) => MyServices.UpdateContent(json);

        #endregion

        #region Subscriptions

        public string GetAllSubscriptions() => MyServices.GetAllSubscriptions();

        public string GetSubscriptionById(string userId) => MyServices.GetSubscriptionById(userId);

        public void AddSubscription(string json) => MyServices.AddSubscription(json);

        public void DeleteSubscription(string userId) => MyServices.DeleteSubscription(userId);

        public void UpdateSubscription(string json) => MyServices.UpdateSubscription(json);

        #endregion
    }
}