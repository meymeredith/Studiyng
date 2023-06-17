W = [0.75, 0.5, 1]
lr = 0.2

training = [[1, 1, -1], [9.4, 6.4, -1], [2.5, 2.7, 1], [8.5, 0.2, 1], [0.5, 9.6, 1], [9.2, 8.9, -1], [7.7, 6.3, -1], [2.8, 0.8, 1], [1.2, 3.0, 1], [7.2, 9.2, -1]]

for epoch in range(20):
    print("Эпоха:", epoch+1)
    for d in training:
        x = d[:2]
        y = d[2]
        output = sum([W[i]*x[i] for i in range(len(x))])
        if output > 0:
            output = 1
        else:
            output = -1
        error = y - output
        for i in range(len(W)):
            if i < len(x):
                W[i] = W[i] + lr * error * x[i]
    print("Веса:", W)

test_data = [[5.2, 7.9, -1], [3.1, 4.7, -1], [8.7, 6.1, 1], [4.4, 4.5, 1]]