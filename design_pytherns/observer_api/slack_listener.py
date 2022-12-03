from observer_lib.slack import post_slack_message
from .event import subscribe
# having a dot in front of the module name says it is in the same directory

def handle_user_registered_event(user):
    post_slack_message("sales",
        f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.")

def handle_user_upgrade_plan_event(user):
    post_slack_message("sales",
        f"{user.name} has upgraded their plan.")

def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)