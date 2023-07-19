from flask import Blueprint, render_template, request

from models.event import Event
from models.events_list import events

# index, display all events
# GET events
events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/events")
def index():
    return render_template("index.jinja", title="Events page", event_list=events)
  
# create, create a new event
# POST events
@events_blueprint.route("/events" ,methods=["POST"])
def create_event():
# get the fields from the form
    name = request.form["name"]
    date = request.form["date"]
    location = request.form["location"]
    number_of_guests = request.form["number_of_guests"]
    description = request.form["description"]
    reccuring = request.form["reccuring"]
    # cerate the new event using fields

    new_event=Event(name, date, number_of_guests,location,description,reccuring)

    # add the new event to the list of events

    events.append(new_event)

    # return render_template
    return render_template("index.jinja", title="Events page", event_list=events)
