def get_bananas(l,i):
  if l[i] > 1000:
    l[i] -= 1000
    return 1000
  else:
    qu = l[i]
    l[i] = 0
    return qu

def drop_bananas(qu,l,i):
  if l[i-1] > 0:
    l[i] += (qu-1)
    return (1,1)
  else :
    l[i] += qu
    return (0,0)

""" distance_to_travel = int(input("quelle distance le chameau doit parcourir ? "))
init_bananas = int(input("combien de bananes initiales")) """
def simulation(dist: int, bananas: int, verbose = True):
  distance_to_travel = dist
  distance_traveled = 0
  bananas_dropped = [bananas] + [0]*distance_to_travel
  bananas_hold = 0
  nb_movements = 0
  if verbose:
    print(f'distance totale a parcourir : {distance_to_travel}')
    print(f'nombre de bananes a transporter : {bananas}')

  while distance_traveled < distance_to_travel:
    while bananas_dropped[distance_traveled] > 0:
      bananas_hold = get_bananas(bananas_dropped, distance_traveled)
      bananas_hold -= 1
      distance_traveled += 1
      nb_movements += 1
      if distance_traveled < distance_to_travel :
        bananas_hold, res = drop_bananas(bananas_hold, bananas_dropped, distance_traveled)
        if res == 1:
          distance_traveled -= 1
          nb_movements += 1
          bananas_hold = 0
      else:
        if verbose:
          print("\ntransport reussi")
          print(f'- nombre total de mouvements : {nb_movements}.')
          print(f'- nombre de bananes final : {bananas_hold+1}.\n')
        return 1
    if bananas_hold == 0:
      if verbose:
        print("\nerreur, pas assez de bananes")
        print(f'- nombre d\'etapes : {nb_movements}.')
        print(f'- distance parcourue : {distance_traveled} km.\n')
      return 0

# print("simulation 1:\n")
# simulation(1000, 3000)

# print("simulation 2:\n")
# simulation(2000, 4000)

# win = 0
# dist = 1000
# while win != 5:
#   simulation(dist, banana)

min = {1000: 1000, 2000: 7678, 3000: 56780}

dist_cur = 1000
dist_max = 10000

res = 0
bananas_cur = 1000
bananas_max = 100000
while dist_cur <= dist_max:
  while bananas_cur < bananas_max :
    print(bananas_cur)
    res = simulation(dist_cur, bananas_cur, False)
    if res == 1 :
      # print(f'{bananas_cur} est une solution pour {dist_cur}km')
      min[dist_cur] = bananas_cur
      break
    bananas_cur += 1
  dist_cur += 1000
  
print(min)