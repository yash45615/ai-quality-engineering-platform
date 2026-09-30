from locust import (
    HttpUser,
    task,
    between
)


class SoakUser(HttpUser):

    wait_time = between(
        2,
        5
    )

    @task
    def homepage(self):

        self.client.get(
            "/",
            name="Soak Homepage"
        )