from room import Room
# file           class

kitchen= Room("kitchen")
kitchen.set_description("A desk and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_descrpition("A large roo, with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_descrpition("A vast room with a shiny floor, Huge candlesticks guard the entrance.")

kitchen.link_room(dining-hall, "south")


dining_hall.link_room(kitchen, "north")
dining_hall.link_room(hallroom, "west")
ballroom.link_room(dining_hall, "east")
