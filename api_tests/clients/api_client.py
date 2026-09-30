import requests


class APIClient:

    def __init__(
        self,
        base_url: str,
        timeout: int = 10
    ):

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

    def get(
        self,
        endpoint: str,
        **kwargs
    ):

        return self.session.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def post(
        self,
        endpoint: str,
        **kwargs
    ):

        return self.session.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def put(
        self,
        endpoint: str,
        **kwargs
    ):

        return self.session.put(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def patch(
        self,
        endpoint: str,
        **kwargs
    ):

        return self.session.patch(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def delete(
        self,
        endpoint: str,
        **kwargs
    ):

        return self.session.delete(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            timeout=self.timeout,
            **kwargs
        )

    def close(self):

        self.session.close()