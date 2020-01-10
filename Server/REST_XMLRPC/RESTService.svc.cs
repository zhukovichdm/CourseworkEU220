using System;
using System.Collections.Generic;
using System.ServiceModel;
using System.ServiceModel.Activation;
using System.ServiceModel.Web;
using REST_XMLRPC.EntityFramework;

namespace REST_XMLRPC
{
    [ServiceContract(Namespace = "")]
    [AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
    public class RESTService
    {
        #region Users

        [WebGet(UriTemplate = "/Users/GetAll", ResponseFormat = WebMessageFormat.Json)]
        public string GetAllUsers() => MyServices.GetAllUsers();

        [WebGet(UriTemplate = "/User/GetById/{userId}")]
        public string GetUserById(string userId) => MyServices.GetUserById(userId);

        //[WebGet(UriTemplate = "/User/Add/{json}")]
        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/User/Add/{json}",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddUser(string json) => MyServices.AddUser(json);

        [WebGet(UriTemplate = "/User/DellById/{userId}")]
        public void DeleteUser(string userId) => MyServices.DeleteUser(userId);

        [WebGet(UriTemplate = "/User/Update/{json}")]
        public void UpdateUser(string json) => MyServices.UpdateUser(json);

        #endregion

        #region Topics

        [WebGet(UriTemplate = "/Topics/GetAll", ResponseFormat = WebMessageFormat.Json)]
        public string GetAllTopics() => MyServices.GetAllTopics();

        [WebGet(UriTemplate = "/Topic/GetById/{userId}")]
        public string GetTopicById(string userId) => MyServices.GetTopicById(userId);

        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/Topic/Add/{json}",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddTopic(string json) => MyServices.AddTopic(json);

        [WebGet(UriTemplate = "/Topic/DellById/{userId}")]
        public void DeleteTopic(string userId) => MyServices.DeleteTopic(userId);

        [WebGet(UriTemplate = "/Topic/Update/{json}")]
        public void UpdateTopic(string json) => MyServices.UpdateTopic(json);

        #endregion

        #region ContentTypes

        [WebGet(UriTemplate = "/ContentTypes/GetAll", ResponseFormat = WebMessageFormat.Json)]
        public string GetAllContentTypes() => MyServices.GetAllContentTypes();

        [WebGet(UriTemplate = "/ContentType/GetById/{userId}")]
        public string GetContentTypeById(string userId) => MyServices.GetContentTypeById(userId);

        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/ContentType/Add/{json}",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddContentType(string json) => MyServices.AddContentType(json);

        [WebGet(UriTemplate = "/ContentType/DellById/{userId}")]
        public void DeleteContentType(string userId) => MyServices.DeleteContentType(userId);

        [WebGet(UriTemplate = "/ContentType/Update/{json}")]
        public void UpdateContentType(string json) => MyServices.UpdateContentType(json);

        #endregion

        #region Contents

        [WebGet(UriTemplate = "/Contents/GetAll", ResponseFormat = WebMessageFormat.Json)]
        public string GetAllContents() => MyServices.GetAllContents();

        [WebGet(UriTemplate = "/Content/GetById/{userId}")]
        public string GetContentById(string userId) => MyServices.GetContentById(userId);

        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/Content/Add/{json}",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddContent(string json) => MyServices.AddContent(json);

        [WebGet(UriTemplate = "/Content/DellById/{userId}")]
        public void DeleteContent(string userId) => MyServices.DeleteContent(userId);

        [WebGet(UriTemplate = "/Content/Update/{json}")]
        public void UpdateContent(string json) => MyServices.UpdateContent(json);

        #endregion

        #region Subscriptions

        [WebGet(UriTemplate = "/Subscriptions/GetAll", ResponseFormat = WebMessageFormat.Json)]
        public string GetAllSubscriptions() => MyServices.GetAllSubscriptions();

        [WebGet(UriTemplate = "/Subscription/GetById/{userId}")]
        public string GetSubscriptionById(string userId) => MyServices.GetSubscriptionById(userId);

        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/Subscription/Add/{json}",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddSubscription(string json) => MyServices.AddSubscription(json);

        [WebGet(UriTemplate = "/Subscription/DellById/{userId}")]
        public void DeleteSubscription(string userId) => MyServices.DeleteSubscription(userId);

        [WebGet(UriTemplate = "/Subscription/Update/{json}")]
        public void UpdateSubscription(string json) => MyServices.UpdateSubscription(json);

        #endregion

        //****************************************//

        #region TEST

        private static List<string> lst = new List<string>
        {
            "Arrays",
            "Queues",
            "Stacks"
        };

        [WebGet(UriTemplate = "/Tutorial")]
        public string GetAllTutorials()
        {
            //using (UserContext db = new UserContext())
            //{
            //    // создаем два объекта User
            //    User user1 = new User { Name = "Tom", Age = 33 };
            //    User user2 = new User { Name = "Sam", Age = 26 };

            //    // добавляем их в бд
            //    db.Users.Add(user1);
            //    db.Users.Add(user2);
            //    db.SaveChanges();
            //    Console.WriteLine("Объекты успешно сохранены");

            //    // получаем объекты из бд и выводим на консоль
            //    var users = db.Users;
            //    Console.WriteLine("Список объектов:");
            //    foreach (User u in users)
            //    {
            //        Console.WriteLine("{0}.{1} - {2}", u.Id, u.Name, u.Age);
            //    }
            //}
            return String.Join(",", lst);
        }


        [WebGet(UriTemplate = "/Tutorial/{TutorialId}")]
        public string GetTutorialByID(string TutorialId)
        {
            var id = StringToInt(TutorialId);
            if (id >= 0 && id < lst.Count)
                return lst[StringToInt(TutorialId)];
            return "ERROR";
        }

        [WebInvoke(Method = "POST", RequestFormat = WebMessageFormat.Json, UriTemplate = "/Tutorial",
            ResponseFormat = WebMessageFormat.Json, BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void AddTutorial(string str)
        {
            lst.Add(str);
            Console.WriteLine(str);
        }

        [WebInvoke(Method = "DELETE", RequestFormat = WebMessageFormat.Json,
            UriTemplate = "/Tutorial/{TutorialId}", ResponseFormat = WebMessageFormat.Json,
            BodyStyle = WebMessageBodyStyle.Wrapped)]
        public void DeleteTutorial(string TutorialId)
        {
            int id = StringToInt(TutorialId);
            if (id >= 0 && id < lst.Count)
                lst.RemoveAt(id);
        }


        [OperationContract]
        public void DoWork()
        {
            // Добавьте здесь реализацию операции
            return;
        }

// Добавьте здесь дополнительные операции и отметьте их атрибутом [OperationContract]


        private int StringToInt(string value)
        {
            int result;
            try

            {
                result = Convert.ToInt32(value);
            }
            catch (Exception e)
            {
                result = -1;
            }

            return result;
        }

        #endregion
    }
}