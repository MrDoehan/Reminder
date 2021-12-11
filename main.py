Remimport time
game = True
while game == True:
  reminder = input("What is occurng? ")
  form = input("minutes/hours/seconds/days?")
  if form == "minutes":
    local_time = int(input("In how many minutes/hours/seconds? "))
    local_time = local_time * 60
    time.sleep(local_time)

  elif form == "seconds":
    local_time = int(input("In how many minutes/hours/seconds? "))
    local_time = local_time 
    time.sleep(local_time)

  elif form == "hours":
    local_time = int(input("In how many minutes/hours/seconds? "))  
    local_time = local_time * 60 * 60
    time.sleep(local_time)
  elif form == "days":
    local_time = int(input("In how many minutes/hours/seconds? "))  
    local_time = local_time * 60 * 60 * 24    
    time.sleep(local_time)
  else:
    print("That option is unavailable.")

  print(reminder)
  cont = input("Do you want to restart? y/n: ")
  if cont == "y":
    game = True
  else:
    game = False  