import csv 
import os
from datetime import date, timedelta

from flask_mail import Message
from sqlalchemy import func

from celery_app import celery
from database import db, mail

from app import app
from models import *

def send_mail(to, subject, body, html=None):
    if not to:
        return
    msg = Message(subject=subject, recipients=[to], body=body, html=html)
    mail.send(msg)

@celery.task(name="tasks.daily_reminder")
def daily_reminder():

    with app.app_context():
        tomorrow = date.today() + timedelta(days=1)

        bookings = Booking.query.filter(Booking.status == "Booked").all()

        for booking in bookings:
            if booking.trek.start_date == tomorrow:
                subject = "TrailBlaze - Trek Reminder"

                body = f"""
                        Hello {booking.user.full_name},

                        This is a reminder that your "{booking.trek.trek_name}" trek starts tomorrow.

                        Location : {booking.trek.location}
                        Start Date : {booking.trek.start_date}

                        Happy Trekking!!

                        - TrailBlaze Team
                    """
                send_mail(booking.user.email, subject, body)
        print("Daily reminders sent.")


@celery.task(name="tasks.monthly_report")
def monthly_report():
    with app.app_context():

        total_treks = Trek.query.count()
        total_bookings = Booking.query.count()

        popular = (db.session.query(Trek.trek_name, func.count(Booking.id).label("count"))
            .join(Booking)
            .group_by(Trek.id)
            .order_by(func.count(Booking.id).desc())
            .first()
        )

        popular_trek = popular[0] if popular else "No bookings"

        html = f"""
        <h2>TrailBlaze Monthly Report</h2>
        <hr>
        <p><b>Total Treks:</b> {total_treks}</p>
        <p><b>Total Participants:</b> {total_bookings}</p>
        <p><b>Most Popular Trek:</b> {popular_trek}</p>
        <br>
        <p>Generated automatically by TrailBlaze.</p>
        """

        send_mail(
            "apoorvajaiswal590@gmail.com",
            "TrailBlaze Monthly Report",
            "",
            html
        )
        print("Monthly report sent.")


@celery.task(name="tasks.export_csv")
def export_csv(user_id):

    with app.app_context():

        user = User.query.get(user_id)
        bookings = Booking.query.filter_by(user_id=user_id).all()

        filename = f"booking_history_{user_id}.csv"
        with open(filename, "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow([
                "Booking ID",
                "Trek Name",
                "Location",
                "Difficulty",
                "Duration (Days)",
                "Booking Status",
                "Payment Status",
                "Booking Date",
                "Start Date",
                "End Date"
            ])
            for booking in bookings:
                writer.writerow([
                    booking.id,
                    booking.trek.trek_name,
                    booking.trek.location,
                    booking.trek.difficulty,
                    booking.trek.duration,
                    booking.status,
                    booking.payment_status,
                    booking.booking_date,
                    booking.trek.start_date,
                    booking.trek.end_date
            ])

        msg = Message(
            subject="TrailBlaze - Booking History CSV",
            sender=app.config["MAIL_DEFAULT_SENDER"],
            recipients=[user.email]
        )

        msg.body = f"""
        Hello {user.full_name},

        Your trekking history has been exported successfully.

        Please find your booking history CSV attached.

        Happy Trekking!

        - TrailBlaze Team
        """

        with open(filename, "rb") as fp:
            msg.attach(
                "booking_history.csv",
                "text/csv",
                fp.read()
            )

        mail.send(msg)
        os.remove(filename)

        print("CSV Export Completed")