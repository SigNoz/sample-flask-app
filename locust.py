import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_list(self):
        self.client.get("/list")
    
    @task
    def create_task(self):
        self.client.post("/action", json={ "name":"ankit", "desc":"description", "date":"05/01/2021", "pr":"high", "done":"no"})

    @task(3)
    def completed_tasks(self):
        self.client.get("/completed")

    @task(4)
    def uncompleted_tasks(self):
        self.client.get("/uncompleted")

    def on_start(self):
        self.client.get("/list")