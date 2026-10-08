import time
from celery import shared_task


@shared_task
def send_order_notification_task(order_id, user_email, service_title):
    # Asinxron jarayonni simulyatsiya qilish (masalan, Email yuborish)
    print(f"[CELERY] Buyurtma #{order_id} uchun xabarnoma yuborish boshlandi...")
    time.sleep(5)  # 5 sekundlik og'ir vazifa simulyatsiyasi
    print(f"[CELERY SUCCESS] Xabarnoma {user_email} ga yuborildi! Buyurtma qilingan xizmat: {service_title}")
    return f"Notification sent for Order #{order_id}"