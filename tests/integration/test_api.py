

def test_health_check2(sget):
    response = sget("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"health check": "ok"}


def test_db_connection(sget):
    response = sget("/api/v1/test-db")
    assert response.status_code == 200
    assert response.json() == {"status": "Connected", "result": 1}
    # redundant just to try
    assert response.json()["status"] =='Connected'
    assert response.json()["result"] == 1


def test_send_email_through_celery_queue(sget):
        for i in range(45):
            response = sget("/api/v1/send-email")
        assert response.status_code == 200
        assert response.json() == {"email": "sent"}
