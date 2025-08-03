import os
from datetime import datetime 
from langchain_core.tools import tool

def schedule_event(event: str, time: str): 
    return f"Scheduled event: '(event)' at (time)"

def reschedule_event(event: str, old_time: str, new_time: str): 
    return f"Rescheduled '(event)' from {old_time} to {new_time}"

def cancel_event(event: str, time: str): 
    return f"Canceled event '(event)' at (time)"

def read_emails():

    return" 3 unread emails:\n1. From HR -Offer Letter\n2. From Rahul - Meeting agenda\n3. Promo Amazon Deals"

def draft_email(recipient: str, subject: str, body: str):
    os.makedirs("drafts", exist_ok=True)

    filename = f"drafts/{recipient.replace('@','')}{datetime.now().strftime('%Y%m%d%H%M')}.txt"

    with open(filename, "w", encoding="utf-8") as f: f.write(f"Subject: (subject)\n\n{body}")

    return f"Draft saved: {filename}"

tools = [tool(name="schedule_event", func=schedule_event, description="Schedul e a calendar event"),

    tool(name="reschedule_event", func=reschedule_event, description="Resc hedule a calendar event"),

    tool(name="cancel_event", func=cancel_event, description="Cancel a caleandar event"),

    tool(name="read_emails", func=read_emails, description="Read and summ rize unread emails"),

    tool(name="draft_email", func=draft_email, description="Create and save an email draft")]



