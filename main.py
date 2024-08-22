import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed = []
x_c = data["x"].to_list()
y_c = data["y"].to_list()

correct = 0
game_on = True

while game_on:
    answer = screen.textinput(title=f"{correct}/50 States Correct", prompt="Enter a U.S. State name").title()
    if answer == "Exit":
        '''missing_states = []
        for n in states:
            if n not in guessed:
                missing_states.append(n)
!!!!  IF GAME DOES NOT WORK, DELETE LINE BELOW AND UNCOMMENT THIS STUFF!!!!'''
        missing_states = [n for n in states if n not in guessed]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if correct == 50:
        game_on = False
    for n in states:
        if answer == n:
            if n not in guessed:
                x_cor = x_c[states.index(n)]
                y_cor = y_c[states.index(n)]
                state = turtle.Turtle()
                state.hideturtle()
                state.penup()
                state.goto(x_cor, y_cor)
                state.write(n)
                guessed.append(n)
                correct += 1

screen.exitonclick()
