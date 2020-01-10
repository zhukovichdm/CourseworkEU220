from abc import abstractmethod
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Protocols import AbstractClasses
import Test


class Tab:
    @abstractmethod
    def init_tab(self, tab):
        pass

    @abstractmethod
    def fill_tree(self):
        pass

    @abstractmethod
    def focus_item(self):
        pass

    @abstractmethod
    def btn_clear_event(self):
        pass

    @abstractmethod
    def btn_save_event(self):
        pass

    @abstractmethod
    def btn_delete_event(self):
        pass

    @abstractmethod
    def reset_focus_text(self):
        pass


connection = Test.Connection()
protocol = connection.get("XMLRPC")
# protocol = connection.get("REST")
# protocol = connection.get("SOAP")

users = []
users_name = []
topics = []
topics_name = []
content_types = []
content_types_name = []
contents = []
contents_names = []


class MainForm(Frame):

    def __init__(self, root):
        super().__init__(root)
        toolbar = Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=TOP, fill=X)

        # Выбор протокола
        self.my_var = StringVar()
        rad1 = ttk.Radiobutton(toolbar, text="XMLRPC", value="XMLRPC", variable=self.my_var, command=self.set_protocol)
        rad2 = ttk.Radiobutton(toolbar, text="REST", value="REST", variable=self.my_var, command=self.set_protocol)
        rad3 = ttk.Radiobutton(toolbar, text="SOAP", value="SOAP", variable=self.my_var, command=self.set_protocol)
        rad1.grid(column=0, row=0)
        rad2.grid(column=1, row=0)
        rad3.grid(column=2, row=0)
        # Вкладки таблиц
        tab_control = ttk.Notebook(root)
        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)
        self.tab3 = ttk.Frame(tab_control)
        self.tab4 = ttk.Frame(tab_control)
        self.tab5 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text='Пользователи')
        tab_control.add(self.tab2, text='Темы')
        tab_control.add(self.tab3, text='Тип контента')
        tab_control.add(self.tab4, text='Контент')
        tab_control.add(self.tab5, text='Подписки')
        tab_control.pack(expand=1, fill='both')

        # Данные полученые с базы

        # Создание вкладки 1
        user_tab = self.UserTab()
        user_tab.init_tab(self.tab1)
        user_tab.fill_tree()
        # Создание вкладки 2
        topic_tab = self.TopicTab()
        topic_tab.init_tab(self.tab2)
        topic_tab.fill_tree()
        # Создание вкладки 3
        content_tab = self.ContentTypeTab()
        content_tab.init_tab(self.tab3)
        content_tab.fill_tree()
        # Создание вкладки 4
        content_type_tab = self.ContentTab()
        content_type_tab.init_tab(self.tab4)
        content_type_tab.fill_tree()
        # Создание вкладки 5
        content_type_tab = self.SubscriptionTab()
        content_type_tab.init_tab(self.tab5)
        content_type_tab.fill_tree()

    def set_protocol(self):
        global protocol
        protocol = Test.Connection().get(self.my_var.get())

    class UserTab(Tab):
        focus_user = AbstractClasses.User

        def init_tab(self, tab):
            # Таблица
            self.tree = ttk.Treeview(tab, columns=('Id', 'Name', 'Age'), height=15, show='headings')
            self.tree.column('Id', width=40, anchor=CENTER)
            self.tree.column('Name', width=350, anchor=CENTER)
            self.tree.column('Age', width=100, anchor=CENTER)
            self.tree.heading('Id', text='id')
            self.tree.heading('Name', text='Имя')
            self.tree.heading('Age', text='Возраст')
            self.tree.bind('<<TreeviewSelect>>', lambda event: self.focus_item())
            # self.tree.bind('<Double-1>', lambda event: self.focus_item())  # Double-1
            # self.tree.pack()
            self.tree.grid(column=0, row=0)

            # Поля ввода
            label_name = Label(tab, text='Имя')
            label_name.place(x=10, y=340)
            label_age = Label(tab, text='Возраст')
            label_age.place(x=10, y=370)
            self.entry_name = ttk.Entry(tab)
            self.entry_name.place(x=70, y=340)
            self.entry_age = ttk.Entry(tab)
            self.entry_age.place(x=70, y=370)

            # Кнопки изменения данных
            btn_add = ttk.Button(tab, text='Очистить')
            btn_add.place(x=250, y=335)
            btn_add.bind('<Button-1>', lambda event: self.btn_clear_event())

            btn_update = ttk.Button(tab, text='Сохранить')
            btn_update.place(x=330, y=335)
            btn_update.bind('<Button-1>', lambda event: self.btn_save_event())

            btn_delete = ttk.Button(tab, text='Удалить')
            btn_delete.place(x=410, y=335)
            btn_delete.bind('<Button-1>', lambda event: self.btn_delete_event())

        def fill_tree(self):
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            global users
            global users_name
            users_name = []
            users = protocol.user.get_all()
            for user in users:
                self.tree.insert('', 0, values=(user.Id, user.Name, user.Age))
                users_name.append(user.Name)

        def focus_item(self):
            focus = self.tree.focus()
            if len(focus) != 0:
                self.reset_focus_text()
                self.focus_user = AbstractClasses.User(self.tree.item(focus).get('values')[0],
                                                       self.tree.item(focus).get('values')[1],
                                                       self.tree.item(focus).get('values')[2])
                self.entry_name.insert(0, str(self.focus_user.Name))
                self.entry_age.insert(0, str(self.focus_user.Age))

        def btn_clear_event(self):
            self.fill_tree()
            self.tree.selection_set()
            self.reset_focus_text()

        def btn_save_event(self):
            if messagebox.askyesno('Сохранение', 'Сохранить запись?'):
                if self.tree.focus():
                    if self.focus_user:
                        self.focus_user.Name = self.entry_name.get()
                        self.focus_user.Age = self.entry_age.get()
                        protocol.user.update_by_value(self.focus_user)
                        self.fill_tree()
                        self.reset_focus_text()
                else:
                    self.focus_user = AbstractClasses.User(0, self.entry_name.get(), int(self.entry_age.get()))
                    protocol.user.add(self.focus_user)
                    self.fill_tree()
                    self.reset_focus_text()

        def btn_delete_event(self):
            if self.focus_user and messagebox.askyesno('Удаление', 'Удалить запись?'):
                protocol.user.delete_by_id(self.focus_user.Id)
                self.fill_tree()
                self.reset_focus_text()

        def reset_focus_text(self):
            self.entry_name.delete(0, 'end')
            self.entry_age.delete(0, 'end')

    class TopicTab(Tab):
        focus_topic = AbstractClasses.Topic

        def init_tab(self, tab):
            # Таблица
            self.tree = ttk.Treeview(tab, columns=('Id', 'Name'), height=15, show='headings')
            self.tree.column('Id', width=40, anchor=CENTER)
            self.tree.column('Name', width=450, anchor=CENTER)
            self.tree.heading('Id', text='id')
            self.tree.heading('Name', text='Название')
            self.tree.bind('<<TreeviewSelect>>', lambda event: self.focus_item())
            # self.tree.bind('<Double-1>', lambda event: self.focus_item())  # Double-1
            # self.tree.pack()
            self.tree.grid(column=0, row=0)

            # Поля ввода
            label_name = Label(tab, text='Название')
            label_name.place(x=10, y=340)
            self.entry_name = ttk.Entry(tab)
            self.entry_name.place(x=70, y=340)

            # Кнопки изменения данных
            btn_add = ttk.Button(tab, text='Очистить')
            btn_add.place(x=250, y=335)
            btn_add.bind('<Button-1>', lambda event: self.btn_clear_event())

            btn_update = ttk.Button(tab, text='Сохранить')
            btn_update.place(x=330, y=335)
            btn_update.bind('<Button-1>', lambda event: self.btn_save_event())

            btn_delete = ttk.Button(tab, text='Удалить')
            btn_delete.place(x=410, y=335)
            btn_delete.bind('<Button-1>', lambda event: self.btn_delete_event())

        def fill_tree(self):
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            global topics
            global topics_name
            topics_name = []
            topics = protocol.topic.get_all()
            for topic in topics:
                self.tree.insert('', 0, values=(topic.Id, topic.Name))
                topics_name.append(topic.Name)

        def focus_item(self):
            focus = self.tree.focus()
            if len(focus) != 0:
                self.reset_focus_text()
                self.focus_topic = AbstractClasses.Topic(self.tree.item(focus).get('values')[0],
                                                         self.tree.item(focus).get('values')[1])
                self.entry_name.insert(0, str(self.focus_topic.Name))

        def btn_clear_event(self):
            self.fill_tree()
            self.tree.selection_set()
            self.reset_focus_text()

        def btn_save_event(self):
            if messagebox.askyesno('Сохранение', 'Сохранить запись?'):
                if self.tree.focus():
                    if self.focus_topic:
                        self.focus_topic.Name = self.entry_name.get()
                        protocol.topic.update_by_value(self.focus_topic)
                        self.fill_tree()
                        self.reset_focus_text()
                else:
                    self.focus_topic = AbstractClasses.Topic(0, self.entry_name.get())
                    protocol.topic.add(self.focus_topic)
                    self.fill_tree()
                    self.reset_focus_text()

        def btn_delete_event(self):
            if self.focus_topic and messagebox.askyesno('Удаление', 'Удалить запись?'):
                protocol.topic.delete_by_id(self.focus_topic.Id)
                self.fill_tree()
                self.reset_focus_text()

        def reset_focus_text(self):
            self.entry_name.delete(0, 'end')

    class ContentTypeTab(Tab):
        focus_content_type = AbstractClasses.ContentType

        def init_tab(self, tab):
            # Таблица
            self.tree = ttk.Treeview(tab, columns=('Id', 'Name'), height=15, show='headings')
            self.tree.column('Id', width=40, anchor=CENTER)
            self.tree.column('Name', width=450, anchor=CENTER)
            self.tree.heading('Id', text='id')
            self.tree.heading('Name', text='Название')
            self.tree.bind('<<TreeviewSelect>>', lambda event: self.focus_item())
            # self.tree.bind('<Double-1>', lambda event: self.focus_item())  # Double-1
            # self.tree.pack()
            self.tree.grid(column=0, row=0)

            # Поля ввода
            label_name = Label(tab, text='Название')
            label_name.place(x=10, y=340)
            self.entry_name = ttk.Entry(tab)
            self.entry_name.place(x=70, y=340)

            # Кнопки изменения данных
            btn_add = ttk.Button(tab, text='Очистить')
            btn_add.place(x=250, y=335)
            btn_add.bind('<Button-1>', lambda event: self.btn_clear_event())

            btn_update = ttk.Button(tab, text='Сохранить')
            btn_update.place(x=330, y=335)
            btn_update.bind('<Button-1>', lambda event: self.btn_save_event())

            btn_delete = ttk.Button(tab, text='Удалить')
            btn_delete.place(x=410, y=335)
            btn_delete.bind('<Button-1>', lambda event: self.btn_delete_event())

        def fill_tree(self):
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            global content_types
            global content_types_name
            content_types_name = []
            content_types = protocol.content_type.get_all()
            for content_type in content_types:
                self.tree.insert('', 0, values=(content_type.Id, content_type.Name))
                content_types_name.append(content_type.Name)

        def focus_item(self):
            focus = self.tree.focus()
            if len(focus) != 0:
                self.reset_focus_text()
                self.focus_content_type = AbstractClasses.ContentType(self.tree.item(focus).get('values')[0],
                                                                      self.tree.item(focus).get('values')[1])
                self.entry_name.insert(0, str(self.focus_content_type.Name))

        def btn_clear_event(self):
            self.fill_tree()
            self.tree.selection_set()
            self.reset_focus_text()

        def btn_save_event(self):
            if messagebox.askyesno('Сохранение', 'Сохранить запись?'):
                if self.tree.focus():
                    if self.focus_content_type:
                        self.focus_content_type.Name = self.entry_name.get()
                        protocol.content_type.update_by_value(self.focus_content_type)
                        self.fill_tree()
                        self.reset_focus_text()
                else:
                    self.focus_content_type = AbstractClasses.ContentType(0, self.entry_name.get())
                    protocol.content_type.add(self.focus_content_type)
                    self.fill_tree()
                    self.reset_focus_text()

        def btn_delete_event(self):
            if self.focus_content_type and messagebox.askyesno('Удаление', 'Удалить запись?'):
                protocol.content_type.delete_by_id(self.focus_content_type.Id)
                self.fill_tree()
                self.reset_focus_text()

        def reset_focus_text(self):
            self.entry_name.delete(0, 'end')

    class ContentTab(Tab):
        focus_content = AbstractClasses.Content

        def init_tab(self, tab):
            # Таблица
            self.tree = ttk.Treeview(tab, columns=('Id', 'Topic', 'ContentType', 'Price', 'Name'), height=15,
                                     show='headings')
            self.tree.column('Id', width=40, anchor=CENTER)
            self.tree.column('Topic', width=150, anchor=CENTER)
            self.tree.column('ContentType', width=150, anchor=CENTER)
            self.tree.column('Price', width=50, anchor=CENTER)
            self.tree.column('Name', width=100, anchor=CENTER)
            self.tree.heading('Id', text='id')
            self.tree.heading('Topic', text='Тема')
            self.tree.heading('ContentType', text='Тип')
            self.tree.heading('Price', text='Цена')
            self.tree.heading('Name', text='Название')
            self.tree.bind('<<TreeviewSelect>>', lambda event: self.focus_item())
            # self.tree.bind('<Double-1>', lambda event: self.focus_item())  # Double-1
            # self.tree.pack()
            self.tree.grid(column=0, row=0)

            # Поля ввода
            label_topic = Label(tab, text='Тема')
            label_topic.place(x=10, y=340)
            label_type = Label(tab, text='Тип')
            label_type.place(x=10, y=370)
            label_price = Label(tab, text='Цена')
            label_price.place(x=10, y=400)
            label_name = Label(tab, text='Название')
            label_name.place(x=10, y=430)
            self.combobox_topics = ttk.Combobox(tab, values=topics_name)
            self.combobox_topics.place(x=70, y=340)
            self.combobox_content_type = ttk.Combobox(tab, values=content_types_name)
            self.combobox_content_type.place(x=70, y=370)
            self.entry_price = ttk.Entry(tab)
            self.entry_price.place(x=70, y=400)
            self.entry_name = ttk.Entry(tab)
            self.entry_name.place(x=70, y=430)

            # Кнопки изменения данных
            btn_add = ttk.Button(tab, text='Очистить')
            btn_add.place(x=250, y=335)
            btn_add.bind('<Button-1>', lambda event: self.btn_clear_event())

            btn_update = ttk.Button(tab, text='Сохранить')
            btn_update.place(x=330, y=335)
            btn_update.bind('<Button-1>', lambda event: self.btn_save_event())

            btn_delete = ttk.Button(tab, text='Удалить')
            btn_delete.place(x=410, y=335)
            btn_delete.bind('<Button-1>', lambda event: self.btn_delete_event())

        def fill_tree(self):
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            global contents
            contents = protocol.content.get_all()
            for content in contents:
                global topics
                topic_name = None
                for topic in topics:
                    if topic.Id == content.TopicsId:
                        topic_name = topic.Name

                global content_types
                content_type_name = None
                for content_type in content_types:
                    if content_type.Id == content.ContentTypeId:
                        content_type_name = content_type.Name

                contents_names.append(content.Data)
                # contents_names.append(topic_name + "/" + content_type_name)

                self.tree.insert('', 0, values=(content.Id, topic_name, content_type_name, content.Price, content.Data))

        def focus_item(self):
            focus = self.tree.focus()
            if len(focus) != 0:
                self.reset_focus_text()
                self.focus_content = AbstractClasses.Content(self.tree.item(focus).get('values')[0],
                                                             self.tree.item(focus).get('values')[1],
                                                             self.tree.item(focus).get('values')[2],
                                                             self.tree.item(focus).get('values')[3],
                                                             self.tree.item(focus).get('values')[4])
                self.combobox_content_type.insert(0, str(self.focus_content.ContentTypeId))
                self.combobox_topics.insert(0, str(self.focus_content.TopicsId))
                self.entry_price.insert(0, str(self.focus_content.Price))
                self.entry_name.insert(0, str(self.focus_content.Data))

        def btn_clear_event(self):
            self.fill_tree()
            self.tree.selection_set()
            self.reset_focus_text()

        def btn_save_event(self):
            if messagebox.askyesno('Сохранение', 'Сохранить запись?'):
                global topics
                if self.tree.focus():
                    if self.focus_content:
                        self.focus_content.TopicsId = topics[self.combobox_topics.current()].Id
                        self.focus_content.ContentTypeId = content_types[self.combobox_content_type.current()].Id
                        self.focus_content.Price = self.entry_price.get()
                        self.focus_content.Data = self.entry_name.get()
                        protocol.content.update_by_value(self.focus_content)
                        self.fill_tree()
                        self.reset_focus_text()
                else:
                    self.focus_content = AbstractClasses.Content(0, topics[self.combobox_topics.current()].Id,
                                                                 content_types[self.combobox_content_type.current()].Id,
                                                                 self.entry_price.get(), self.entry_name.get())
                    protocol.content.add(self.focus_content)
                    self.fill_tree()
                    self.reset_focus_text()

        def btn_delete_event(self):
            if self.focus_content and messagebox.askyesno('Удаление', 'Удалить запись?'):
                protocol.content.delete_by_id(self.focus_content.Id)
                self.fill_tree()
                self.reset_focus_text()

        def reset_focus_text(self):
            self.combobox_content_type.delete(0, 'end')
            self.combobox_topics.delete(0, 'end')
            self.entry_price.delete(0, 'end')
            self.entry_name.delete(0, 'end')

    class SubscriptionTab(Tab):
        focus_subscription = AbstractClasses.Subscription

        def init_tab(self, tab):
            # Таблица
            self.tree = ttk.Treeview(tab, columns=('Id', 'UserId', 'ContentId'), height=15, show='headings')
            # self.tree = ttk.Treeview(tab, columns=('Id', 'UserId', 'ContentId', 'Date'), height=15, show='headings')
            self.tree.column('Id', width=40, anchor=CENTER)
            self.tree.column('UserId', width=225, anchor=CENTER)
            self.tree.column('ContentId', width=225, anchor=CENTER)
            # self.tree.column('Date', width=100, anchor=CENTER)
            self.tree.heading('Id', text='id')
            self.tree.heading('UserId', text='Пользователь')
            self.tree.heading('ContentId', text='Контент')
            # self.tree.heading('Date', text='Дата')
            self.tree.bind('<<TreeviewSelect>>', lambda event: self.focus_item())
            # self.tree.bind('<Double-1>', lambda event: self.focus_item())  # Double-1
            # self.tree.pack()
            self.tree.grid(column=0, row=0)

            # Поля ввода
            label_user = Label(tab, text='Пользователь')
            label_user.place(x=10, y=340)
            label_content = Label(tab, text='Контент')
            label_content.place(x=10, y=370)
            self.combobox_user = ttk.Combobox(tab, values=users_name)
            self.combobox_user.place(x=70, y=340)
            self.combobox_content = ttk.Combobox(tab, values=contents_names)
            self.combobox_content.place(x=70, y=370)

            # Кнопки изменения данных
            btn_add = ttk.Button(tab, text='Очистить')
            btn_add.place(x=250, y=335)
            btn_add.bind('<Button-1>', lambda event: self.btn_clear_event())

            btn_update = ttk.Button(tab, text='Сохранить')
            btn_update.place(x=330, y=335)
            btn_update.bind('<Button-1>', lambda event: self.btn_save_event())

            btn_delete = ttk.Button(tab, text='Удалить')
            btn_delete.place(x=410, y=335)
            btn_delete.bind('<Button-1>', lambda event: self.btn_delete_event())

        def fill_tree(self):
            x = self.tree.get_children()
            for item in x:
                self.tree.delete(item)

            subscriptions = protocol.subscription.get_all()
            for subscription in subscriptions:
                user_name = None
                for user in users:
                    if user.Id == subscription.UserId:
                        user_name = user.Name

                global topics
                # topic_name = None
                # content_type_name = None
                content_name = None
                for content in contents:
                    if content.Id == subscription.ContentId:
                        content_name = content.Data
                        # for topic in topics:
                        #     if topic.Id == content.TopicsId:
                        #         topic_name = topic.Name
                        #
                        # for content_type in content_types:
                        #     if content_type.Id == content.ContentTypeId:
                        #         content_type_name = content_type.Name

                self.tree.insert('', 0, values=(
                    subscription.Id, user_name, content_name))
                # subscription.Id, user_name, topic_name + "/" + content_type_name))

        def focus_item(self):
            focus = self.tree.focus()
            if len(focus) != 0:
                self.reset_focus_text()
                self.focus_subscription = AbstractClasses.Subscription(self.tree.item(focus).get('values')[0],
                                                                       self.tree.item(focus).get('values')[1],
                                                                       self.tree.item(focus).get('values')[2])
                self.combobox_content.insert(0, self.focus_subscription.ContentId)
                self.combobox_user.insert(0, self.focus_subscription.UserId)

        def btn_clear_event(self):
            self.fill_tree()
            self.tree.selection_set()
            self.reset_focus_text()

        def btn_save_event(self):
            if messagebox.askyesno('Сохранение', 'Сохранить запись?'):
                if self.tree.focus():
                    if self.focus_subscription:
                        self.focus_subscription.UserId = users[self.combobox_user.current()].Id
                        self.focus_subscription.ContentId = contents[self.combobox_content.current()].Id
                        protocol.subscription.update_by_value(self.focus_subscription)
                        self.fill_tree()
                        self.reset_focus_text()
                else:
                    self.focus_subscription = AbstractClasses.Subscription(0, users[self.combobox_user.current()].Id,
                                                                           contents[self.combobox_content.current()].Id)
                    protocol.subscription.add(self.focus_subscription)
                    self.fill_tree()
                    self.reset_focus_text()

        def btn_delete_event(self):
            if self.focus_subscription and messagebox.askyesno('Удаление', 'Удалить запись?'):
                protocol.subscription.delete_by_id(self.focus_subscription.Id)
                self.fill_tree()
                self.reset_focus_text()

        def reset_focus_text(self):
            self.combobox_content.delete(0, 'end')
            self.combobox_user.delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    app = MainForm(root)
    app.pack()
    root.title("PyClient")
    root.geometry("650x550+300+200")
    root.resizable(False, False)
    root.mainloop()
