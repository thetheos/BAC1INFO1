class SMSStore:
    def __init__(self):
        self.sms_list = []
        pass

    def new_arrival(self, from_nbr, time_arrived, text):
        self.sms_list.append((False, from_nbr, time_arrived, text))
        return True

    def message_count(self):
        return len(self.sms_list)

    
    def get_unread_indexes(self):
        unread_index = []
        for pos,sms in enumerate(self.sms_list):
            if sms[0] == False:
                unread_index.append(pos)
        return unread_index

    def get_message(self,i):
        try:
            sms = self.sms_list[i]
            sms = (True, sms[1], sms[2], sms[3])
            self.sms_list[i] = sms
            return sms
        except:
            return None
    

    def delete(self,i):
        del self.sms_list[i]

    def clear(self):
        self.sms_list = []


my_inbox = SMSStore()

my_inbox.new_arrival(210, 1242, "salut")

my_inbox.new_arrival(210,1242,"Caca")
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(0))
print(my_inbox.get_unread_indexes())
