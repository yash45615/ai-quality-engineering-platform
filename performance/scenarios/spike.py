from locust import (
    HttpUser,
    task
)


class SpikeUser(HttpUser):

    wait_time = lambda self: 0.1

    @task
    def homepage(self):

        self.client.get(
            "/",
            name="Spike Homepage"
        )