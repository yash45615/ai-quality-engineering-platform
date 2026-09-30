from locust import (
    HttpUser,
    task,
    between
)


class StressUser(HttpUser):

    wait_time = between(
        0.2,
        1
    )

    @task
    def homepage(self):

        self.client.get(
            "/",
            name="Stress Homepage"
        )