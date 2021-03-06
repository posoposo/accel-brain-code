if __name__ == "__main__":
    from deeplearning.nn.builders.nn_multi_layer_builder import NNMultiLayerBuilder
    from deeplearning.activation.logistic_function import LogisticFunction
    import numpy as np
    import random
    import pandas as pd
    from pprint import pprint
    from sklearn.datasets import make_classification
    from sklearn.cross_validation import train_test_split

    data_tuple = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=2,
        n_classes=2,
        class_sep=1.0
    )
    data_tuple_x, data_tuple_y = data_tuple
    traning_x, test_x, traning_y, test_y = train_test_split(
        data_tuple_x,
        data_tuple_y,
        test_size=0.3,
        random_state=888
    )
    traning_data_matrix = traning_x
    class_data_list = traning_y
    test_data_matrix = test_x
    test_class_data_list = test_y

    class_data_matrix = [[class_data] for class_data in class_data_list]
    test_class_data_matrix = [[class_data] for class_data in test_class_data_list]

    evaluate_data_list = []

    nn = NeuralNetwork(
        NNMultiLayerBuilder(),
        [len(traning_data_matrix[0]), 9, 3, 1],
        [SigmoidFunction(), SigmoidFunction(), SigmoidFunction(), SigmoidFunction()]
    )

    nn.learn(
        traning_data_matrix,
        class_data_matrix,
        traning_count=1,
        learning_rate=0.01,
        momentum_factor=0.01
    )
    evaluate_result_dict = nn.evaluate_bool(
        test_data_matrix,
        test_class_data_matrix
    )
    evaluate_data_list.append(evaluate_result_dict)

    nn = NeuralNetwork(
        NNMultiLayerBuilder(),
        [len(traning_data_matrix[0]), 4, 3, 1],
        [SigmoidFunction(), SigmoidFunction(), SigmoidFunction(), SigmoidFunction()]
    )

    nn.learn(
        traning_data_matrix,
        class_data_matrix,
        traning_count=1,
        learning_rate=0.00000001,
        momentum_factor=0.000000001
    )
    evaluate_result_dict = nn.evaluate_bool(
        test_data_matrix,
        test_class_data_matrix
    )
    evaluate_data_list.append(evaluate_result_dict)

    evaluate_data = pd.DataFrame(evaluate_data_list)
    evaluate_data = evaluate_data.sort_values(by=["f", "precision", "recall"], ascending=False)

    data_columns = [
        "neuron_assign_list",
        "learning_rate",
        "momentum_factor",
        "traning_count",
        "tp", "tn", "fp", "fn",
        "precision",
        "recall",
        "f"
    ]

    print(evaluate_data[data_columns])

    '''
  neuron_assign_list  learning_rate  momentum_factor  traning_count  tp   tn  \
1      [10, 4, 3, 1]   1.000000e-08     1.000000e-09              1  91   50
0      [10, 9, 3, 1]   1.000000e-02     1.000000e-02              1   9  143

   fp   fn  precision    recall         f
1  97   62   0.484043  0.594771  0.533724
0   4  144   0.692308  0.058824  0.108434
    '''
