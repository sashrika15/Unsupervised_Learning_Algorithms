import matplotlib.pyplot as plt

def plot(img, red_img, starting_wts, trained_wts):
    plt.figure(figsize=(14,8))
    
    plt.subplot(2,2,1)
    plt.title("Original Image")
    plt.imshow(img)
    
    plt.subplot(2,2,2)
    plt.title("Reduced Image")
    plt.imshow(red_img)

    plt.subplot(2,2,3)
    plt.title("Initial Colours Matrix")
    plt.imshow(starting_wts)
    
    plt.subplot(2,2,4)
    plt.title("Learnt Colours Matrix")
    plt.imshow(trained_wts)

    plt.tight_layout()
    plt.show()
