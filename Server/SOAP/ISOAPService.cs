using System.Runtime.Serialization;
using System.ServiceModel;


namespace SOAP
{
    // ПРИМЕЧАНИЕ. Команду "Переименовать" в меню "Рефакторинг" можно использовать для одновременного изменения имени интерфейса "ISOAPService" в коде и файле конфигурации.
    [ServiceContract]
    public interface ISOAPService
    {
        #region Users

        [OperationContract]
        string GetAllUsers();

        [OperationContract]
        string GetUserById(string userId);

        [OperationContract]
        void AddUser(string json);

        [OperationContract]
        void DeleteUser(string userId);

        [OperationContract]
        void UpdateUser(string json);

        #endregion

        #region Topics

        [OperationContract]
        string GetAllTopics();

        [OperationContract]
        string GetTopicById(string userId);

        [OperationContract]
        void AddTopic(string json);

        [OperationContract]
        void DeleteTopic(string userId);

        [OperationContract]
        void UpdateTopic(string json);

        #endregion

        #region ContentType

        [OperationContract]
        string GetAllContentTypes();

        [OperationContract]
        string GetContentTypeById(string userId);

        [OperationContract]
        void AddContentType(string json);

        [OperationContract]
        void DeleteContentType(string userId);

        [OperationContract]
        void UpdateContentType(string json);

        #endregion

        #region Contents

        [OperationContract]
        string GetAllContents();

        [OperationContract]
        string GetContentById(string userId);

        [OperationContract]
        void AddContent(string json);

        [OperationContract]
        void DeleteContent(string userId);

        [OperationContract]
        void UpdateContent(string json);

        #endregion

        #region Subscriptions

        [OperationContract]
        string GetAllSubscriptions();

        [OperationContract]
        string GetSubscriptionById(string userId);

        [OperationContract]
        void AddSubscription(string json);

        [OperationContract]
        void DeleteSubscription(string userId);

        [OperationContract]
        void UpdateSubscription(string json);

        #endregion
    }


    // Используйте контракт данных, как показано в примере ниже, чтобы добавить составные типы к операциям служб.
    [DataContract]
    public class CompositeType
    {
        bool boolValue = true;
        string stringValue = "Hello ";

        [DataMember]
        public bool BoolValue
        {
            get { return boolValue; }
            set { boolValue = value; }
        }

        [DataMember]
        public string StringValue
        {
            get { return stringValue; }
            set { stringValue = value; }
        }
    }
}