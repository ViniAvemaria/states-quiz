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
    state.write(answer)


def check_state(answer):
    data = pandas.read_csv("50_states.csv")
    state = data[data["state"] == answer]
    if state.empty:
        return False
    else:
        return (state["x"].item(), state["y"].item())


def remaining_states(guesses):
    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()
    missing = [state for state in all_states if state not in guesses]
    data = pandas.DataFrame({"state": missing})
    data.to_csv("missing_states.csv")


correct_guesses = []
while len(correct_guesses) < 50:
    user_answer = turtle.textinput(f"{len(correct_guesses)}/50 States Correct", "Type a state's name").title()
    if user_answer == "Exit":
        remaining_states(correct_guesses)
        break
    coordinates = check_state(user_answer)

    if coordinates:
        if user_answer not in correct_guesses:
            write_answer(user_answer, coordinates)
            correct_guesses.append(user_answer)

screen.exitonclick()
