from abc import ABC, abstractmethod
from typing import Dict, Type

# ============================================
# STEP 1: COMMON INTERFACE FOR ALL PRODUCTS
# ============================================


class Notification(ABC):
    """Common interface for all notification types"""

    @abstractmethod
    def send(self, message: str, recipient: str) -> bool:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass

# ============================================
# STEP 2: CONCRETE NOTIFICATION CLASSES
# ============================================


class EmailNotification(Notification):
    def __init__(self, smtp_server: str = "smtp.gmail.com"):
        self.smtp_server = smtp_server
        self.subject = "Notification"

    def send(self, message: str, recipient: str) -> bool:
        print(f"📧 EMAIL via {self.smtp_server}")
        print(f"   To: {recipient}")
        print(f"   Subject: {self.subject}")
        print(f"   Message: {message}")
        print("   ✅ Email sent successfully")
        return True

    def get_type(self) -> str:
        return "email"

    def set_subject(self, subject: str):
        self.subject = subject


class SMSNotification(Notification):
    def __init__(self, api_key: str = "twilio_default"):
        self.api_key = api_key

    def send(self, message: str, recipient: str) -> bool:
        print(f"📱 SMS via Twilio API ({self.api_key[:8]}...)")
        print(f"   To: {recipient}")
        print(f"   Message: {message}")
        print("   ✅ SMS sent successfully")
        return True

    def get_type(self) -> str:
        return "sms"


class PushNotification(Notification):
    def __init__(self, service: str = "firebase"):
        self.service = service
        self.title = "Alert"

    def send(self, message: str, recipient: str) -> bool:
        print(f"🔔 PUSH via {self.service}")
        print(f"   To: {recipient}")
        print(f"   Title: {self.title}")
        print(f"   Content: {message}")
        print("   ✅ Push notification sent successfully")
        return True

    def get_type(self) -> str:
        return "push"

    def set_title(self, title: str):
        self.title = title


class SlackNotification(Notification):
    def __init__(self, webhook_url: str = "https://hooks.slack.com/..."):
        self.webhook_url = webhook_url
        self.channel = "#general"

    def send(self, message: str, recipient: str) -> bool:
        print(f"💬 SLACK via webhook")
        print(f"   Channel: {self.channel}")
        print(f"   Mention: @{recipient}")
        print(f"   Message: {message}")
        print("   ✅ Slack message sent successfully")
        return True

    def get_type(self) -> str:
        return "slack"

    def set_channel(self, channel: str):
        self.channel = channel

# ============================================
# STEP 3: SIMPLE FACTORY (Basic Version)
# ============================================


class NotificationFactory:
    """Simple Factory - creates notifications based on type"""

    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        """Factory method - the magic happens here!"""

        if notification_type.lower() == "email":
            return EmailNotification()
        elif notification_type.lower() == "sms":
            return SMSNotification()
        elif notification_type.lower() == "push":
            return PushNotification()
        elif notification_type.lower() == "slack":
            return SlackNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# ============================================
# STEP 4: ENHANCED FACTORY (Registry Pattern)
# ============================================


class NotificationRegistry:
    """Enhanced Factory using registry pattern - more flexible!"""

    def __init__(self):
        self._creators: Dict[str, Type[Notification]] = {}

    def register(self, notification_type: str, creator_class: Type[Notification]):
        """Register a new notification type - no code changes needed!"""
        self._creators[notification_type.lower()] = creator_class
        print(f"📝 Registered notification type: '{notification_type}'")

    def unregister(self, notification_type: str):
        """Remove a notification type"""
        if notification_type.lower() in self._creators:
            del self._creators[notification_type.lower()]
            print(f"🗑️ Unregistered notification type: '{notification_type}'")

    def create_notification(self, notification_type: str, **kwargs) -> Notification:
        """Create notification with optional parameters"""
        creator_class = self._creators.get(notification_type.lower())
        if not creator_class:
            available_types = list(self._creators.keys())
            raise ValueError(
                f"Unknown notification type: '{notification_type}'. Available: {available_types}")

        # Create instance with optional parameters
        return creator_class(**kwargs)

    def get_available_types(self) -> list:
        """Get list of available notification types"""
        return list(self._creators.keys())

# ============================================
# STEP 5: NOTIFICATION MANAGER (CLEAN VERSION)
# ============================================


class NotificationManager:
    """Clean notification manager using Factory pattern"""

    def __init__(self, factory: NotificationRegistry):
        self.factory = factory

    def send_notification(self, message: str, notification_type: str, recipient: str, **options) -> bool:
        """Send notification - no knowledge of specific classes!"""
        try:
            # Separate constructor args from configuration options
            constructor_args = {}
            config_options = {}

            # Define which options are constructor parameters vs configuration
            constructor_params = {
                "email": ["smtp_server"],
                "sms": ["api_key"],
                "push": ["service"],
                "slack": ["webhook_url"]
            }

            # Split options into constructor args and config options
            if notification_type.lower() in constructor_params:
                for param in constructor_params[notification_type.lower()]:
                    if param in options:
                        constructor_args[param] = options[param]

            # Everything else is configuration
            for key, value in options.items():
                if key not in constructor_args:
                    config_options[key] = value

            # Factory handles object creation with constructor args only
            notification = self.factory.create_notification(
                notification_type, **constructor_args)

            # Configure notification with remaining options
            if notification_type.lower() == "email" and "subject" in config_options:
                notification.set_subject(config_options["subject"])
            elif notification_type.lower() == "push" and "title" in config_options:
                notification.set_title(config_options["title"])
            elif notification_type.lower() == "slack" and "channel" in config_options:
                notification.set_channel(config_options["channel"])

            # Send the notification
            return notification.send(message, recipient)

        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
        except TypeError as e:
            print(f"❌ Constructor Error: {e}")
            print(
                f"   Check constructor parameters for '{notification_type}' type")
            return False

    def get_supported_types(self) -> list:
        """Get all supported notification types"""
        return self.factory.get_available_types()

# ============================================
# STEP 6: USAGE EXAMPLE
# ============================================


if __name__ == "__main__":
    print("=" * 60)
    print("FACTORY PATTERN DEMONSTRATION")
    print("=" * 60)

    # ============================================
    # Simple Factory Usage
    # ============================================

    print("\n🏭 SIMPLE FACTORY EXAMPLE:")
    print("-" * 30)

    # Create notifications using simple factory
    email = NotificationFactory.create_notification("email")
    sms = NotificationFactory.create_notification("sms")
    push = NotificationFactory.create_notification("push")

    # Use them
    email.send("Your order is ready!", "customer@example.com")
    print()
    sms.send("OTP: 123456", "+1234567890")
    print()
    push.send("New message received", "user123")

    # ============================================
    # Registry Factory Usage
    # ============================================

    print("\n\n🗂️ REGISTRY FACTORY EXAMPLE:")
    print("-" * 30)

    # Create factory and register notification types
    factory = NotificationRegistry()
    factory.register("email", EmailNotification)
    factory.register("sms", SMSNotification)
    factory.register("push", PushNotification)
    factory.register("slack", SlackNotification)

    # Create notification manager
    manager = NotificationManager(factory)

    print(f"\n📋 Supported types: {manager.get_supported_types()}")

    print("\n📤 Sending notifications:")

    # Send different types of notifications
    manager.send_notification(
        "Your payment was successful!",
        "email",
        "customer@example.com",
        subject="Payment Confirmation"
    )

    print()
    manager.send_notification(
        "Security alert: New login detected",
        "sms",
        "+1234567890"
    )

    print()
    manager.send_notification(
        "Your order has shipped!",
        "push",
        "user123",
        title="Shipping Update"
    )

    print()
    manager.send_notification(
        "Server is down! All hands on deck!",
        "slack",
        "devteam",
        channel="#alerts"
    )

    # ============================================
    # Adding New Notification Type at Runtime
    # ============================================

    print("\n\n🔧 ADDING NEW TYPE AT RUNTIME:")
    print("-" * 30)

    # Create a new notification type
    class WhatsAppNotification(Notification):
        def __init__(self, api_key: str = "whatsapp_api"):
            self.api_key = api_key

        def send(self, message: str, recipient: str) -> bool:
            print(f"💚 WHATSAPP via API ({self.api_key})")
            print(f"   To: {recipient}")
            print(f"   Message: {message}")
            print("   ✅ WhatsApp message sent successfully")
            return True

        def get_type(self) -> str:
            return "whatsapp"

    # Register new type - NO changes to existing code!
    factory.register("whatsapp", WhatsAppNotification)

    print(f"\n📋 Updated supported types: {manager.get_supported_types()}")

    # Use new notification type immediately
    print("\n📤 Using new WhatsApp notification:")
    manager.send_notification(
        "Hi! Your appointment is tomorrow at 2 PM",
        "whatsapp",
        "+1987654321"
    )

    # ============================================
    # Error Handling
    # ============================================

    print("\n\n❌ ERROR HANDLING:")
    print("-" * 30)

    # Try to use unsupported type
    manager.send_notification(
        "This should fail",
        "telegram",  # Not registered
        "user123"
    )

    print("\n✅ Factory Pattern Benefits:")
    print("- Clean separation of object creation")
    print("- Easy to add new notification types")
    print("- NotificationManager doesn't know about specific classes")
    print("- Centralized object creation logic")
    print("- Runtime type registration possible")
