from sklearn.metrics import log_loss

true_0 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

pred_1 = [0, 0, 0, 0, 0, 0, 0.9, 0.1, 0, 0, 0]
pred_n90 = [0.9, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(log_loss(true_0, pred_1))
print(log_loss(true_0, pred_n90))

