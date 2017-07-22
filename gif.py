import imageio
images = []
for filename in range(100):
    images.append(imageio.imread('./results/'+str(filename*80)+'.jpg'))
    print(filename)
imageio.mimsave('./results/yisus3.gif', images)
