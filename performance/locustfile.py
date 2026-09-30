from locust import (
    HttpUser,
    task,
    between
)


class WebsiteUser(HttpUser):

    wait_time = between(
        1,
        3
    )

    @task(3)
    def homepage(self):

        self.client.get(
            "/",
            name="Homepage"
        )

    @task(2)
    def inventory(self):

        self.client.get(
            "/inventory.html",
            name="Inventory"
        )