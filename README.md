# Blender-Combiner
For combining materials in blender for Roughness, Occlusion, Metallic, Alpha
![Image description](https://i.imgur.com/lXyT4sV.gif)


To install please use Edit, Preferences then click the Install button in Blender. Choose the ".py" file. Then click the check box to enable.


To use it, you will need to install PIL first. To do this, I have created a python script you can use called installPIL.py.
1. Open Blender as Administrator.
2. Head to the "Scripting Tab" along the top bar.
3. Click "+ New"
4. Paste the code in from the installPIL.py file
5. Press "ALT + P" OR click the run button at the top. 

![Image description](https://i.imgur.com/pmM5F3D.png)


That's it.

Onto Usage:
1. If you head into the "Shader Editor" you should see on the Right hand side an option called "RGBA Combiner". If not, press "N" on your keyboard. 
2. After clicking it, you should see an area to choose your images from your project. 
3. Choose the images you want to use for Roughness/Occlusion/Metallic/Alpha and then click "Combine Textures". It will create a new image file with the values of those you chose.
4. If you are missing or not using one of those just set it to one of the images you ARE using. As it will be taking the values from it anyway, it wont cause any interference.


If none of your images are showing up, you will need to make sure you have "Packed" them into your current blend file. To do this, head to the "UV Editor" and choose your images there, then under the "Image" tab drop down at the top of that module, you will see "Pack" at the bottom.
After this, they will now appear in the "RGBA Combiner" menu.

![Image description](https://i.imgur.com/EXiUZfN.png)
