using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace REST_XMLRPC.EntityFramework
{
    public static class MyServices
    {
        private static readonly List<string> AllUsers = new List<string>();
        private static readonly List<string> AllTopics = new List<string>();
        private static readonly List<string> AllContentTypes = new List<string>();

        private static readonly List<string> AllContents = new List<string>();
        private static readonly List<string> AllSubscriptions = new List<string>();

        //private static CourseworkContext db = new CourseworkContext();
        private static CourseworkDBContext db = new CourseworkDBContext();

        // Первое заполнение таблиц
        private static void CreateDB()
        {
            Subscriptions receivedSubscription = new Subscriptions();
            receivedSubscription.UserId = 0;
            foreach (var user in db.Users)
                receivedSubscription.Users = user;
            receivedSubscription.ContentId = 0;
            foreach (var content in db.Contents)
                receivedSubscription.Contents = content;
            db.Subscriptions.Add(receivedSubscription);
            /////
            Contents contents = new Contents();
            contents.TopicsId = 0;
            contents.ContentTypeId = 0;
            contents.Price = 100;
            contents.Data = "Test";
            foreach (var temp in db.Topics)
                contents.Topics = temp;

            foreach (var temp in db.ContentTypes)
                contents.ContentTypes = temp;

            db.Contents.Add(contents);

            db.SaveChanges();
        }


        #region Users

        private static void LoadAllUsers()
        {
            AllUsers.Clear();
            foreach (var user in db.Users)
            {
                string str = $"{{\"Id\":{user.Id}," +
                             $"\"Name\":\"{user.Name}\"," +
                             $"\"Age\":{user.Age}}}";
                AllUsers.Add(str);
            }
        }

        public static string GetAllUsers()
        {
            LoadAllUsers();
            return string.Join("&", AllUsers);
        }

        public static string GetUserById(string userId)
        {
            int.TryParse(userId, out int id);
            foreach (var user in db.Users)
                if (user.Id == id)
                    return JsonConvert.SerializeObject(user);

            return "ERROR: ID NOT FOUND";
        }

        public static void AddUser(string json)
        {
            try
            {
                var receivedUser = JsonConvert.DeserializeObject<Users>(json);
                db.Users.Add(receivedUser);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void DeleteUser(string userId)
        {
            try
            {
                int.TryParse(userId, out int id);
                foreach (var user in db.Users)
                    if (user.Id == id)
                        db.Users.Remove(user);
                db.SaveChanges();
            }
            catch (Exception e)
            {
            }
        }

        public static void UpdateUser(string json)
        {
            try
            {
                var receivedUser = JsonConvert.DeserializeObject<Users>(json);
                foreach (var user in db.Users)
                    if (user.Id == receivedUser.Id)
                    {
                        user.Age = receivedUser.Age;
                        user.Name = receivedUser.Name;
                    }

                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        #endregion


        #region Topics

        private static void LoadAllTopics()
        {
            AllTopics.Clear();
            foreach (var topic in db.Topics)
            {
                string str = $"{{\"Id\":{topic.Id}," +
                             $"\"Name\":\"{topic.Name}\"," +
                             $"\"Contents\":{0}}}";
                AllTopics.Add(str);
            }
        }

        public static string GetAllTopics()
        {
            LoadAllTopics();
            return string.Join("&", AllTopics);
        }

        public static string GetTopicById(string topicId)
        {
            int.TryParse(topicId, out int id);
            foreach (var topic in db.Topics)
                if (topic.Id == id)
                    return JsonConvert.SerializeObject(topic);

            return "ERROR: ID NOT FOUND";
        }

        public static void AddTopic(string json)
        {
            try
            {
                var topic = JsonConvert.DeserializeObject<Topics>(json);
                db.Topics.Add(topic);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void DeleteTopic(string topicId)
        {
            try
            {
                int.TryParse(topicId, out int id);
                foreach (var topic in db.Topics)
                    if (topic.Id == id)
                        db.Topics.Remove(topic);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void UpdateTopic(string json)
        {
            try
            {
                var topic = JsonConvert.DeserializeObject<Topics>(json);
                foreach (var user in db.Topics)
                    if (user.Id == topic.Id)
                    {
                        user.Name = topic.Name;
                    }

                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        #endregion


        #region ContentTypes

        private static void LoadAllContentTypes()
        {
            AllContentTypes.Clear();
            foreach (var contentType in db.ContentTypes)
            {
                string str = $"{{\"Id\":{contentType.Id}," +
                             $"\"Name\":\"{contentType.Name}\"}}";
                AllContentTypes.Add(str);
            }
        }

        public static string GetAllContentTypes()
        {
            LoadAllContentTypes();
            return string.Join("&", AllContentTypes);
        }

        public static string GetContentTypeById(string contentTypeId)
        {
            int.TryParse(contentTypeId, out int id);
            foreach (var contentType in db.ContentTypes)
                if (contentType.Id == id)
                    return JsonConvert.SerializeObject(contentType);

            return "ERROR: ID NOT FOUND";
        }

        public static void AddContentType(string json)
        {
            try
            {
                var contentType = JsonConvert.DeserializeObject<ContentTypes>(json);
                db.ContentTypes.Add(contentType);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void DeleteContentType(string contentTypeId)
        {
            try
            {
                int.TryParse(contentTypeId, out int id);
                foreach (var contentType in db.ContentTypes)
                    if (contentType.Id == id)
                        db.ContentTypes.Remove(contentType);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void UpdateContentType(string json)
        {
            try
            {
                var contentType = JsonConvert.DeserializeObject<ContentTypes>(json);
                foreach (var user in db.ContentTypes)
                    if (user.Id == contentType.Id)
                    {
                        user.Name = contentType.Name;
                    }

                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        #endregion


        #region Contents

        private static void LoadAllContents()
        {
            AllContents.Clear();
            foreach (var content in db.Contents)
            {
                string str = $"{{\"Id\":{content.Id}," +
                             $"\"TopicsId\":{content.TopicsId}," +
                             $"\"ContentTypeId\":{content.ContentTypeId}," +
                             $"\"Price\":{content.Price}," +
                             $"\"Data\":\"{content.Data}\"}}";
                AllContents.Add(str);
            }
        }

        public static string GetAllContents()
        {
            LoadAllContents();
            return string.Join("&", AllContents);
        }

        public static string GetContentById(string contentId)
        {
            int.TryParse(contentId, out int id);
            foreach (var content in db.Contents)
                if (content.Id == id)
                    return JsonConvert.SerializeObject(content);

            return "ERROR: ID NOT FOUND";
        }

        public static void AddContent(string json)
        {
            try
            {
                var content = JsonConvert.DeserializeObject<Contents>(json);
                db.Contents.Add(content);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void DeleteContent(string contentId)
        {
            try
            {
                int.TryParse(contentId, out int id);
                foreach (var content in db.Contents)
                    if (content.Id == id)
                        db.Contents.Remove(content);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void UpdateContent(string json)
        {
            try
            {
                var content = JsonConvert.DeserializeObject<Contents>(json);
                foreach (var user in db.Contents)
                    if (user.Id == content.Id)
                    {
                        user.TopicsId = content.TopicsId;
                        user.ContentTypeId = content.ContentTypeId;
                        user.Price = content.Price;
                        user.Data = content.Data;
                    }

                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        #endregion

        #region Subscriptions

        private static void LoadAllSubscriptions()
        {
            AllSubscriptions.Clear();
            foreach (var subscription in db.Subscriptions)
            {
                string str = $"{{\"Id\":{subscription.Id}," +
                             $"\"UserId\":{subscription.UserId}," +
                             $"\"ContentId\":{subscription.ContentId}}}";
                AllSubscriptions.Add(str);
            }
        }

        public static string GetAllSubscriptions()
        {
            LoadAllSubscriptions();
            return string.Join("&", AllSubscriptions);
        }

        public static string GetSubscriptionById(string subscriptionId)
        {
            int.TryParse(subscriptionId, out int id);
            foreach (var subscription in db.Subscriptions)
                if (subscription.Id == id)
                    return JsonConvert.SerializeObject(subscription);

            return "ERROR: ID NOT FOUND";
        }

        public static void AddSubscription(string json)
        {
            try
            {
                var receivedSubscription = JsonConvert.DeserializeObject<Subscriptions>(json);
                db.Subscriptions.Add(receivedSubscription);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void DeleteSubscription(string subscriptionId)
        {
            try
            {
                int.TryParse(subscriptionId, out int id);
                foreach (var subscription in db.Subscriptions)
                    if (subscription.Id == id)
                        db.Subscriptions.Remove(subscription);
                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        public static void UpdateSubscription(string json)
        {
            try
            {
                var receivedSubscription = JsonConvert.DeserializeObject<Subscriptions>(json);
                foreach (var subscription in db.Subscriptions)
                    if (subscription.Id == receivedSubscription.Id)
                    {
                        subscription.UserId = receivedSubscription.UserId;
                        subscription.ContentId = receivedSubscription.ContentId;
                    }

                db.SaveChanges();
            }
            catch (Exception)
            {
            }
        }

        #endregion
    }
}