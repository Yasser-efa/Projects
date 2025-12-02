liste = []

def suprTodo():
  global liste
  for i in range(len(liste)):
    print(f"{i}: {liste[i]}")
    print()
  todoSupr = input("Quelle tâche voulez-vous supprimer ? ")
  while True:
    try:
      todoSupr = int(todoSupr)
      break
    except:
      print("Ce n'est pas un chiffre !")
  liste.remove(liste[todoSupr])
  # si il y a r dans la liste print qlq qui dit ca et aussi demande a luser s'il veut pas rajt qlq chose dautre avant de dmd de supr
  print(liste)

def ajtTodo():
  global liste
  for i in range(len(liste)):
    print(f"{i}: {liste[i]}")
    print()
  todoUsr = input("Que voulez-vous ajouter comme tâche ? ")
  liste.append(todoUsr)

ajtTodo()

suprTodo()

