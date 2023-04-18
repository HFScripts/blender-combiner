# Blender-Combiner

Combine materials in Blender for Roughness, Occlusion, Metallic, Alpha.

![Blender-Combiner Demo](https://i.imgur.com/lXyT4sV.gif)

## Installation

1. In Blender, go to Edit > Preferences.
2. Click on the "Install" button and select the ".py" file.
3. Check the box next to the add-on to enable it.

To use the add-on, you will need to install PIL first. Use the following steps to install it:

1. Open Blender as Administrator.
2. Go to the "Scripting" tab in the top bar.
3. Click the "+ New" button to create a new script.
4. Paste the code from the "installPIL.py" file.
5. Press "ALT + P" or click the "Run Script" button.

![PIL Installation](https://i.imgur.com/pmM5F3D.png)

## Usage

1. Open the "Shader Editor" in Blender.
2. On the right-hand side, you should see an option called "RGBA Combiner". If not, press "N" on your keyboard to open the side panel.
3. Choose the images you want to use for Roughness/Occlusion/Metallic/Alpha and click "Combine Textures". A new image file with the combined values will be created.
4. If you are missing or not using one of the image types, set it to one of the images you ARE using. The add-on will take the values from it anyway and won't cause any interference.

If your images are not showing up, make sure you have "Packed" them into your current blend file. Follow these steps to pack your images:

1. Go to the "UV Editor" in Blender.
2. Choose your images there.
3. Under the "Image" tab, select "Pack" at the bottom.

After packing your images, they will now appear in the "RGBA Combiner" menu.

![Packed Images](https://i.imgur.com/EXiUZfN.png)
