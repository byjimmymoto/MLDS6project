


train_gen, val_gen, test_gen = data_augmentation(X_train=X_train_prep, 
                                                y_train=Y_train,
                                                X_val=X_val_prep, 
                                                y_val=Y_val,
                                                X_test=X_test_prep, 
                                                y_test=Y_test,
                                                width_range=0.2,
                                                height_range=0.2, 
                                                zoom_range=0.2,
                                                h_flip=False,
                                                fill = 'constant')

model_test = pretrained_model(train_base_model=False, 
                              units=4, 
                              dropout=0.2)

def evaluate_model(model, X_test, y_ohe_test):
    acc = model.evaluate(x=X_test, y=y_ohe_test)
    return acc[1]

def one_hot_labels(y_train, y_test):
  # Ingrese su código aquí
  num_clas = len(set(y_train))
  y_train_ohe = tf.keras.utils.to_categorical((tf.constant(y_train, dtype=tf.float32)), num_classes=num_clas)
  y_test_ohe = tf.keras.utils.to_categorical((tf.constant(y_test, dtype=tf.float32)), num_classes=num_clas)
  return y_train_ohe, y_test_ohe

y_train_ohe, y_test_ohe = one_hot_labels(y_train, y_test)

acc = evaluate_model(model_tr, 
                     X_test=X_test, 
                     y_ohe_test=y_test_ohe)