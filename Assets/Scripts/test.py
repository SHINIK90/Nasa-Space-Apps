# Provided string to turn into an array and print without quotes
star_string = '"Betelgeuse","Rigel","Bellatrix","Alnilam","Mintaka","Alnitak","Saiph","Meissa","Hatsya","Tabit","Dubhe","Merak","Phecda","Megrez","Alioth","Mizar","Alkaid","Talitha","Tania Borealis","Polaris","Kochab","Pherkad","Yildun","Epsilon Ursae Minoris","Caph","Schedar","Ruchbah","Gamma Cassiopeiae","Epsilon_Cassiopeiae","Achird","Mu_Cassiopeiae","Gamma_Cassiopeiae","Antares","Shaula","Sargas","Dschubba","Beta_Scorpii","Pi Scorpii","Kappa Scorpii","Epsilon Scorpii","Girtab","Regulus","Denebola","Algieba","Zosma","Theta_Leonis","Subra","Rasalas","Al Jabhah","Aldebaran","Elnath","Alcyone","Atlas","Maia","Electra","Taygeta","Celaeno","Merope","Deneb","Albireo","Sadr","Epsilon_Cygni","Delta Cygni","Sirius","Adhara","Wezen","Eta Canis Majoris","Mirzam","Muliphein","Furud","Procyon","Beta Canis Minoris","Castor","Pollux","Alhena","Delta Geminorum","Mebsuta","Tejat Posterior","Mekbuda","Epsilon_Sagittarii","Nunki","Zeta Sagittarii","Kaus Media","Gamma2_Sagittarii","Arkab Posterior","Terebellum","Vega","Sheliak","Sulafat","Delta2 Lyrae","Epsilon Lyrae","Beta Persei","Alpha Persei","Omicron Persei","Gorgonea Tertia","Xi Persei","Zeta Persei","Psi Persei","Acrux","Mimosa","Gacrux","Delta Crucis","Epsilon Crucis","Alphard","Ashlesha","Sigma Hydrae","Xi Hydrae","Gamma Hydrae","Alpheratz","Mirach","Almach","Delta Andromedae","Pi_Andromedae","Mu Andromedae","Alpha Centauri","Beta Centauri","Theta Centauri","Epsilon Centauri"'

# Removing the quotes and turning it into a Python list
star_list = star_string.replace('"', '').split(',')

# Joining the array elements into a single string without quotes
result_string = ','.join(star_list)

# Displaying the result
print(result_string)