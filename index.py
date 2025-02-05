import random

VERBOSE = False
DEBUG = False

def experiment(switch_door: bool, verbose: bool = False, debug: bool = False) -> bool:
  doors = ['A', 'B', 'C']

  # The door the car is behind
  car_door = random.choice(doors)
  if verbose:
    print("Car door = " + car_door)

  # The contestant chosen door
  chosen_door = random.choice(doors)
  if verbose:
    print("Chosen door = " + chosen_door)

  # Candidate for eliminations after contestant selection
  elimination_candidates = list(
      filter(lambda door: door != car_door and door != chosen_door, doors)
  )

  # The door to eliminate
  elimination_door = random.choice(elimination_candidates)

  # The updated list of doors
  doors = list(
      filter(lambda door: door != elimination_door, doors)
  )

  if debug:
    print("Remaining doors post-elimination" + str(doors))

  # If switch_door is true then change the door, else keep original door
  if switch_door == True:
      chosen_door = doors[1] if chosen_door == doors[0] else doors[0]

  if debug:
    print("chosen door = " + chosen_door)
    print("car door = " + car_door)
    print(chosen_door == car_door)

  # Return whether the chosen door equals the car door
  return chosen_door == car_door

def do_experiment(iters: int, switch_door: bool):
  won_car = []

  for i in range(iters):
    won_car.append(experiment(switch_door = switch_door, verbose = VERBOSE, debug = DEBUG))

  print("Won car % = " + str((won_car.count(True) / len(won_car))))

ITERS = 1000

print(f"Non-switching doors case ({ITERS} iterations):")
do_experiment(iters = ITERS, switch_door = False)
print()
print(f"Switching doors case ({ITERS} iterations):")
do_experiment(iters = ITERS, switch_door = True)