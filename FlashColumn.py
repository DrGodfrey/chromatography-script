"""This program was written by Rob Godfrey to automate & simplify column prep, and achieve consistent results when changing scale
feel free to adjust 'silica density' to a value more consistent with your material"""

import math

def main():
    sample_g=float(input('TYPE: mass of sample (in grams)\n     ='))
    times_silica=float(input('TYPE: number times silica do you want to use?\n (10-50x depending on seperation)\n     x'))
    rf=float(input('TYPE: Rf of compound (if known)\n ---> otherwise type: 0\n     ='))
    column_size(sample_g, times_silica, rf)
    input("\n-----press enter to exit-----")

def column_height(radius, column_volume):
    column_height=column_volume/(math.pi*radius**2)
    diameter=2*radius
    if 6<column_height<25:
        print('FOR: column diameter =', diameter, 'cm')
        print('     column height =', round(column_height), 'cm')
        print(' ')
    else:
        return

def column_size(sample_g, times_silica, rf):
    silica_density=1/2.5
    silica_mass=sample_g*times_silica
    column_volume=silica_mass/silica_density
    print(' ')
    print('silica mass =', silica_mass, 'grams')
    print('"column volume" ~', column_volume, 'mL of silica')
    print(' ')
    radius=0.5
    for i in range(14):
        column_height(radius, column_volume)
        radius=radius+0.5

    if 1>rf>0:
        elute_column_volume=1/rf
        elute_volume=elute_column_volume*column_volume
        number_fractions=0.8*(13+int(75*rf**2)+int(7*rf))
        fraction_volume=elute_volume/number_fractions
        print('Suggested:\n     fraction volume ~',round(fraction_volume), 'mL')
        print('     fractions untill cmpd. starts eluting ~',int(number_fractions))
        print('    (total volume untill cmpd. starts eluting ~',round(elute_volume), 'mL)')


if __name__ == '__main__':
    main()
