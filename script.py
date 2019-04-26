import inquirer, random

your_health = 75
zombi_health = 15
while True:
    questions = [
      inquirer.List('choise',
                message="Try to stay alive! Guess a number between [1-5]",
                choices=[1, 2, 3, 4, 5],
        ), 
    ] 
    answers = inquirer.prompt(questions)
    your_choise = int(answers['choise'])
    print(your_choise)
    zombie_choise = random.randint(1,5)
    print("Zombi choise",zombie_choise)
    if your_choise == zombie_choise:
        zombi_health-=random.randint(1,15)
        print(your_health ,"and", zombi_health )
    else:
        your_health-=random.randint(1,15) 
        print(your_health,"and", zombi_health)
    if your_health <=0 or zombi_health <=0:
        break