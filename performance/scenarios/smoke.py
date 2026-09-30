from locust import (
    HttpUser,
    task,
    between
)


class SmokeUser(HttpUser):

    wait_time = between(
        1,
        2
    )

    @task
    def homepage(self):

        self.client.get(
            "/",
            name="Smoke Homepage"
        )