import numpy as np
import plotly.graph_objects as go
import skimage.io as sio

# https://cdn.discordapp.com/emojis/750724264264728756.png?v=1
# Det er eksamen om to dager og jeg har brukt tre timer på å plotte Ole Egg
# Det er ikke engang bra kode
# Hjelp.

n = 300
# Haha piecewise go brrrrr
phi_1 = np.linspace(-np.pi/2, 0, n)
phi_2 = np.linspace(0,  np.pi/4, n)
phi_3 = np.linspace(np.pi/4, np.pi/2, n)
theta_ = np.linspace(0, 2*np.pi, n)

phi_1, theta_1 = np.meshgrid(phi_1, theta_)
phi_2, theta_2 = np.meshgrid(phi_2, theta_)
phi_3, theta_3 = np.meshgrid(phi_3, theta_)

x_1 = np.cos(phi_1)*np.cos(theta_1)
y_1 = np.cos(phi_1)*np.sin(theta_1)
z_1 = np.sin(phi_1)

x_2 = (-1 + 2*np.cos(phi_2))*np.cos(theta_2)
y_2 = (-1 + 2*np.cos(phi_2))*np.sin(theta_2)
z_2 = 2*np.sin(phi_2)

x_3 = (2 - np.sqrt(2))*np.cos(phi_3)*np.cos(theta_3)
y_3 = (2 - np.sqrt(2))*np.cos(phi_3)*np.sin(theta_3)
z_3 = 1 + (2 - np.sqrt(2))*np.sin(phi_3)
# Det må være en bedre måte å gjøre dette på lol

# Plotly bit
top = sio.imread("eggtexture.png") # sex joke
mid = sio.imread("eggmid.png")
btm = sio.imread("eggbtm.png")

egg_top = np.fliplr(np.transpose(top[:,:,1]))
egg_mid = np.fliplr(np.transpose(mid[:,:,1]))
egg_btm = np.fliplr(np.transpose(btm[:,:,1]))

surface1 = go.Surface(x=x_1,y=y_1,z=z_1, colorscale='Brwnyl_r', surfacecolor=egg_btm, showscale=False)
surface2 = go.Surface(x=x_2,y=y_2,z=z_2, colorscale='Brwnyl_r', surfacecolor=egg_mid, showscale=False)
surface3 = go.Surface(x=x_3,y=y_3,z=z_3, colorscale='Brwnyl_r', surfacecolor=egg_top, showscale=False)

data = [surface1, surface2, surface3]

layout = go.Layout(title="EGG")
fig = go.Figure(data=data)
fig.show()

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length",
                 color_continuous_scale=[(0, "burlywood"), (1, "white")])

# fig.show()
