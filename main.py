import turtle
import pandas


screen = turtle.Screen()

screen.title("Pakistan Cities")
image = "image_without_cities.gif"
screen.addshape(image)
turtle.shape(image)

# to check coordinates on map
# def read_mouseClick_coordinate(x,y):
#     print(x,y)
#
# turtle.onscreenclick(read_mouseClick_coordinate)
# turtle.mainloop()

data = pandas.read_csv("cities.csv")
all_cities = data.cities.to_list()
guessed_cities = []

while len(guessed_cities) < 29:
    guess = screen.textinput(title=f"{len(guessed_cities)}/29 Correct Cities", prompt="What's another city's "
                                                                                      "name?").title()
    if guess == "Exit":
        # missing_cities = []
        # for cities in all_cities:
        #     if cities not in guessed_cities:
        #         missing_cities.append(cities)
        missing_cities = [cities for cities in all_cities if cities not in guessed_cities]
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("Learn_city_names.csv")
        break
    if guess in all_cities:
        guessed_cities.append(guess)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        city_data = data[data.cities == guess]
        tim.goto(int(city_data.x), int(city_data.y))
        if guess == "Islamabad":
            tim.write(guess, font=("Arial", 11, "bold"))
        else:
            tim.write(guess, font=("Arial", 8, "bold"))
