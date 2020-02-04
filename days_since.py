import datetime

class Data:
    def __init__(self):
        print("init data")

    def get_last_occurrence(self):
        Date = datetime.datetime(2011,4,2)
        return Date

    def get_days_since_last_world_cup_won(self):
        today = datetime.datetime.today()
        days = abs(today-self.get_last_occurrence()).days
        return days

    def get_string(self):
        return '{}'.format(self.get_days_since_last_world_cup_won())

# # Test
# if __name__ == "__main__":
#     d = data()
#     print d.get_string_to_tweet()