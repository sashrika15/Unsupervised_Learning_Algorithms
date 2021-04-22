import matplotlib.pyplot as plt

def output(clf, colors, centroids):
    for classification in clf.classifications:
        color = colors[classification]
        for featureset in clf.classifications[classification]:
            plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=150, linewidths=5, zorder=10)

    for c in centroids:
        plt.scatter(centroids[c][0], centroids[c][1], color='k', marker="*", s=50, linewidths=0.5)







