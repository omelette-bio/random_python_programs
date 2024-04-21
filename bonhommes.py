from random import choice
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-r", "--random", action="store", default = 0, help="affiche n bonhommes aleatoirement")
parser.add_argument("-n", "--nohead", action="store_true", help="genere des bonhommes sans tete")
args = parser.parse_args()

tete = [ 'o', 'O', '°', '•', '○', '●', '□', '■']
corps = [ '|', 'P', 'i', 'I', 'D', '0', 'V']
bras_gauche = [ '/', '~', '-' , ' ' ]
bras_droit = [ '\\', '~', '-', ' ' ]
jambe_gauche = [ '/', '(', '!', '1', 'L' ]
jambe_droite = [ '\\', ')', '!', '1', 'L' ]

bodies = []

def body_gen():
  for corps_elem in corps:
    for bras_gauche_elem in bras_gauche:
      for bras_droit_elem in bras_droit:
        for jambe_gauche_elem in jambe_gauche:
          for jambe_droite_elem in jambe_droite:
            
            if args.nohead == False:   
              for tete_elem in tete:
                cur_body = list()
                cur_body.append(' ' + tete_elem + ' ')
                cur_body.append(bras_gauche_elem + corps_elem + bras_droit_elem)
                cur_body.append(' ' + jambe_gauche_elem + jambe_droite_elem)
                bodies.append(cur_body)
            
            else:
              cur_body = list()
              cur_body.append(bras_gauche_elem + corps_elem + bras_droit_elem)
              cur_body.append(' ' + jambe_gauche_elem + jambe_droite_elem)
              bodies.append(cur_body)
              
  return bodies

def display_bodies(bodies: list):
  i = 1
  for body in bodies:
    print(f'corps n° {i}')
    i += 1
    for parts in body:
      print(parts)

if __name__ == "__main__":
  bodies_list = body_gen()
  if int(args.random) > 0:
    bodies_list_out = list()
    for i in range(int(args.random)):
      bodies_list_out.append(choice(bodies_list))
    display_bodies(bodies_list_out)
  else:
    display_bodies(bodies_list)