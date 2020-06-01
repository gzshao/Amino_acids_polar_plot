import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Seaborn style
sns.set(style='darkgrid', font_scale=1)

table=pd.read_csv('amino_acid.csv')

# import amino acid names, normal concentrations and post-hemodialysis concentrations
name = table['name']
normal = table['control']
post_HD = table['hd']

# a total of 19 amino acids are listed, thus the circle is divided into 19 equal parts
x = np.arange(0,np.pi*2,np.pi*2/19)
width = np.pi*2/19

#The normal concentrations are too close to be used for color values
# sqrt and divided by 19 are used to differentiate these values, so they won't all end up being the same color
colors = plt.cm.viridis(np.sqrt(normal)/19)

plt.rcParams['axes.axisbelow'] = False

plt.figure(figsize=(8,8))
ax = plt.subplot(111, projection='polar')
ax.grid(color = 'black', alpha=0.35)
fig = plt.gcf()
fig.set_size_inches(8, 8)
fig.set_tight_layout("rect")

# set y-axis log scale
ax.set_ylim(0.01,1000)
ax.set_rscale('log')

# ensure labels for every single amino acid
ax.set_xticks(np.pi*2/19*np.arange(19))
ax.set_xticklabels([])

# plot the data here
ax.bar(x, normal, bottom =0.01, width=width, color=colors, alpha=0.5, zorder=1)
ax.bar(x, post_HD, bottom =0.01, width=width/2, color=colors, alpha=0.7, zorder=2)

# draw the dashline pointing to labels
for i, j in enumerate(normal):
    r_dashline = np.arange(j, 1000, 19)
    ax.plot([np.pi*2/19*i for k in r_dashline], r_dashline, color ='black', linewidth = 1, linestyle='--', alpha=0.5)

ax.set_yticks([0.1, 1, 10, 100, 1000])
ax.axes.get_yaxis().set_visible(True)

######### Start of adding labels section
# Adding the x labels for the 19 amino acids
# fine tuning the positions and rotations of these labels
# adjusting the text according to its left edge or right edge
# tuning the spacing according to the lengh of the text
for i in range(5):
    plt.text(x[i], 1100, name[i], ha='left', size=10, rotation =360/19.0*i)

plt.text(x[5]+0.5*np.pi*2/19/4, 1200, name[5], ha='left', size=10, rotation =360/19.0*5)

for i in range(6,10):
    plt.text(x[i], 1100, name[i], size=10, ha="right", rotation =360/19.0*(i)+180)
    #plt.text(x[i], 1100, name[i], size=10, ha="center", rotation =360/19*(i)+180)

#Lysine
plt.text(x[10]+0.25*np.pi*2/19/4, 1200+len(name[10])/2*500, name[10], size=10, ha="center", rotation =360/19.0*10+180)
#Methionine
plt.text(x[11]+0.5*np.pi*2/19/4, 1200+len(name[11])/2*800, name[11], size=10, ha="center", rotation =360/19.0*11+180)
#Phenylalanine
plt.text(x[12]+0.75*np.pi*2/19/4, 1200+len(name[12])/2*1700, name[12], size=10, ha="center", rotation =360/19*12+180)

for i in range(13,15):
    plt.text(x[i]+0.3*np.pi*2/19/4, 1200+len(name[i])/2*900, name[i], size=10, ha="center", rotation =360/19*(i-0.25)+180)

#Threonine
for i in range(15,17):
    plt.text(x[i]-0.5*np.pi*2/19/4, 1200+len(name[i])/2*1700, name[i], size=10, ha="center", rotation =360/19*(i))

#
plt.text(x[17]-0.5*np.pi*2/19/4, 1200+len(name[17])/2*800, name[17], size=10, ha="center", rotation =360/19*(17))
plt.text(x[18]-0.5*np.pi*2/19/4, 1200+len(name[18])/2*500, name[18], size=10, ha="center", rotation =360/19*(18))

# add unit for y-axis
plt.text(x[1]+np.pi*2/19/3, 3000, "[µM]", size=10)
######### End of adding labels section

plt.title("Concentrations of Amino Acids under Normal and Hemodialysis (HD) Conditions", size =15)


plt.show()