from PIL import Image

for frame in range(170):

   image1 = Image.open("mass_spring/initial4/"+str(frame)+".png")
   image2 = Image.open("mass_spring/final4/"+str(frame)+".png")

   width  = image1.width + image2.width
   height = max(image1.height, image2.height)

   combined_image = Image.new('RGBA', (width, height))

   combined_image.paste(image1, (0, 0))
   combined_image.paste(image2, (image1.width, 0))

   combined_image.save("mass_spring/merged4/"+str(frame)+".png")
   #combined_image.show()
