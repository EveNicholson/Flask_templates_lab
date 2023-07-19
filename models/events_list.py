from models.event import Event
import datetime

event1 = Event("Mob Programming", datetime.date(2023, 6, 19), 14, "The Classroom", "We are gonna try and mob this lab!!","yes")
event2 = Event("Glastonbury",datetime.date(2023, 6, 10), 1000, "The South", "Madness, Music, Mugs","yes")
event3 = Event("E3" , datetime.date(2023, 9,30),8000, "LA", "Sounds cool", "yes")


events = [event1, event2, event3]
