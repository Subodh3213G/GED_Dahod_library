from locust import HttpUser, task, between

class LibraryUser(HttpUser):
    # Wait between 1 and 5 seconds between tasks
    wait_time = between(1, 5)

    @task
    def view_kiosk(self):
        # Access the root page which redirects to kiosk, or access kiosk directly
        self.client.get("/kiosk/")

    @task
    def view_dashboard(self):
        # Access the dashboard page
        self.client.get("/dashboard/")