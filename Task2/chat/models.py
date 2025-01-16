import json
from django.utils import timezone  # To get the current timestamp
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=255, default="Unknown")
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=255, default="Unknown")
    content = models.TextField()  # Store the message content (with timestamp added)

    def save(self, *args, **kwargs):
        # Automatically fill in the sender's and recipient's names when saving the message
        self.sender_name = self.sender.username
        self.recipient_name = self.recipient.username
        
        # Prepare message content with only the message text and timestamp
        message_data = {
            "message": self.content,
            "timestamp": str(timezone.now())  # Add the timestamp here
        }
        self.content = json.dumps(message_data)  # Store the message content as a JSON string
        
        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return f"Message from {self.sender_name} to {self.recipient_name}"
