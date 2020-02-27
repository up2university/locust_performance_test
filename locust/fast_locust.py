from locust import HttpLocust, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust


class UserTasks(TaskSet):

    def on_start(self):
       self.register()
    def register(self):
       self.client.post("/register",
                        {"roomname":"up2u"})

    @task
    def index(self):
        self.client.get("/")



    """
    FastHttpLocust uses gevenhttpclient for high concurrency
    """
class WebsiteUser(FastHttpLocust):

    host = "https://meetings.test.up2university.eu/"
    wait_time = between(2, 5)
    task_set = UserTasks
