from locust import HttpLocust, TaskSet, task
import resource
import resource
import socket




class UserBehavior(TaskSet):
    def on_start(self):
       self.login()
    def login(self):
       self.client.post("/login",
                        {"username":"up2u",
                     "password":"education"})
    @task(2)
    def index(self):
        self.client.get("/")

    @task(3)
    def post_number(self):
        self.client.post("/",
                            {"room no":"123"})


    @task(4)
    def category(self):
        self.client.get("/course/index.php?categoryid/")


class WebsiteUser(HttpLocust):
    host="https://learn.test.up2university.eu"
    task_set = UserBehavior
    min_wait = 100
    max_wait = 1500
