import turtle
import pandas

img = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape(img)
turtle.shape(img)


def write_answer(answer, coor):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(coor)
    state.write(answer, False, "center", ("Arial", 8, "normal"))


def check_state(answer):
    data = pandas.read_csv("50_states.csv")
    state = data[data["state"] == answer]
    if state.empty:
        return False
    else:
        x = state["x"].iloc[0]
        y = state["y"].iloc[0]
        return (x, y)


user_answer = turtle.textinput("Guess the state", "Type a state's name").title()
coordinates = check_state(user_answer)
if coordinates:
    write_answer(user_answer, coordinates)

screen.exitonclick()
