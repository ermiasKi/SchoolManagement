from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import Notification
from academics.models import Grade
from attendance.models import Attendance
from announcements.models import Announcement

# Helper Function to Create Notifications
def create_notification(sender, recipient, message, obj=None):
    notification = Notification.objects.create(
        sender=sender,
        recipient=recipient,
        message=message,
        timestamp=timezone.now()
    )

    # Link the notification to the related object using ContentType (optional)
    if obj:
        notification.content_type = ContentType.objects.get_for_model(obj)
        notification.object_id = obj.id
        notification.save()

    return notification


# --- Signal 1: When a teacher updates a student's grade ---
# notifications/utils.py
@receiver(post_save, sender=Grade)
def notify_grade_update(sender, instance, created, **kwargs):
    print(f"Signal triggered for Grade: {instance.id}, Created: {created}")  # Debug
    
    try:
        teacher = instance.teacher.user
        student = instance.student.user

        if created:
            message = f"Your new grade for {instance.subject.name} has been recorded: {instance.score}"
        else:
            message = f"Your grade for {instance.subject.name} has been updated to {instance.score}"

        notification = create_notification(sender=teacher, recipient=student, message=message, obj=instance)
        print(f"Notification created: {notification.id}")  # Debug
    except Exception as e:
        print(f"Error in notify_grade_update: {e}")  # Debug


# --- Signal 2: When a teacher updates student attendance ---
@receiver(post_save, sender=Attendance)
def notify_attendance_update(sender, instance, created, **kwargs):
    teacher = instance.teacher.user if instance.teacher else None
    student = instance.student.user
    status = instance.status.capitalize()

    message = f"Your attendance for {instance.date.strftime('%Y-%m-%d')} is marked as {status}."
    if teacher:
        create_notification(sender=teacher, recipient=student, message=message, obj=instance)
    else:
        create_notification(sender=student, recipient=student, message=message, obj=instance)


# --- Signal 3: When an admin or teacher makes an announcement ---
@receiver(post_save, sender=Announcement)
def notify_announcement(sender, instance, created, **kwargs):
    if created:
        # Decide who receives the announcement
        from accounts.models import User
        sender_user = instance.sender

        if instance.target_role == 'student':
            recipients = User.objects.filter(role='student')
        elif instance.target_role == 'teacher':
            recipients = User.objects.filter(role='teacher')
        else:  # 'all'
            recipients = User.objects.all()

        for recipient in recipients:
            if recipient != sender_user:  # don’t notify the sender
                message = f"New announcement: {instance.title}"
                create_notification(sender=sender_user, recipient=recipient, message=message, obj=instance)
