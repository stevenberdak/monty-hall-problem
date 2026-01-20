import random

VERBOSE = False
DEBUG = False

def experiment(switch_door: bool, verbose: bool = False, debug: bool = False) -> bool:
  doors = ['A', 'B', 'C']

  # The door the prize is behind
  prize_door = random.choice(doors)
  if verbose:
    print("Prize door = " + prize_door)

  # The contestant chosen door
  chosen_door = random.choice(doors)
  if verbose:
    print("Chosen door = " + chosen_door)

  # Candidate for eliminations after contestant selection
  elimination_candidates = list(
      filter(lambda door: door != prize_door and door != chosen_door, doors)
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
    print("prize door = " + prize_door)
    print(chosen_door == prize_door)

  # Return whether the chosen door equals the prize door
  return chosen_door == prize_door

def do_experiment(iters: int, switch_door: bool):
  did_win_prize_arr = []

  for i in range(iters):
    did_win_prize_arr.append(experiment(switch_door = switch_door, verbose = VERBOSE, debug = DEBUG))

  print("Win ratio = " + str((100 * did_win_prize_arr.count(True) / len(did_win_prize_arr))) + "%")

ITERS = 1000

print(f"Non-switching doors case ({ITERS} iterations):")
do_experiment(iters = ITERS, switch_door = False)
print()
print(f"Switching doors case ({ITERS} iterations):")
do_experiment(iters = ITERS, switch_door = True)