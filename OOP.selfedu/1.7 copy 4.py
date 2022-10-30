class Viber:
    msg_lst = []
    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        cls.msg_lst.append(msg)

    def remove_message(msg):
        """удаление сообщения из списка;
        """
        del Viber.msg_lst[Viber.msg_lst.index(msg)]
   
    def set_like(msg):
        """поставить/убрать лайк для сообщения msg 
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if Viber.msg_lst[Viber.msg_lst.index(msg)].fl_like == False:
            Viber.msg_lst[Viber.msg_lst.index(msg)].fl_like = True
        else:
            Viber.msg_lst[Viber.msg_lst.index(msg)].fl_like = False

    def show_last_message(numb):
        """отображение последних сообщений;
        """
        print(Viber.msg_lst[numb:])

    def total_messages():
        """звращает общее число сообщений.
        """
        return len(Viber.msg_lst)


class Message:
    """позволяет создавать объекты-сообщения со следующим 
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения 
    (булево значение True - если лайк есть и False - в противном 
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """
    def __init__(self, msg, fl_like = False):
        self.msg = msg
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
print(Viber.total_messages())