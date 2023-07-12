import pytest
from datetime import datetime
from .mocked_data import message_data


@pytest.mark.asyncio
class TestApp:
    async def test_create_message(self, app_client):
        response = app_client.post("/api/message", json=message_data)
        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "success"
        assert data["message"]["uuid"] == message_data["uuid"]
        assert data["message"]["customerId"] == message_data["customerId"]
        assert data["message"]["message_type"] == message_data["message_type"]
        assert data["message"]["amount"] == message_data["amount"]

    async def test_statistics(self, app_client):
        response = app_client.get(
            "/api/statistics",
            params={
                "start_date": "2023-07-01",
                "end_date": datetime.now().strftime("%Y-%m-%d"),
                "message_type": "A",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["results"] == 1
        assert data["data"][0]["message_type"] == message_data["message_type"]
        assert data["data"][0]["total_count"] == 1
