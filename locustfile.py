import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    # @task
    # def index_page(self):
    #     self.client.get("/admin/")

    @task(3)
    def view_item(self):
        item_id = random.randint(1, 10000)
        self.client.get(f"/exam/info/3f82c1c9-0f17-4b7c-b0f6-88d291d5c6c2/")