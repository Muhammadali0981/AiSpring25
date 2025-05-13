from typing import List, Dict, Any, Tuple

def clean_and_scale(dataset: List[Dict[str, Any]], features: List[str]) -> List[Dict[str, float]]:

    # Remove outliers (values > 3 std from mean)
    def mean(values):
        return sum(values) / len(values) if values else 0
    def std(values, m):
        return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5 if values else 1
    stats = {f: [row[f] for row in dataset if row[f] is not None] for f in features}
    means = {f: mean(stats[f]) for f in features}
    stds = {f: std(stats[f], means[f]) for f in features}
    filtered = []
    for row in dataset:
        keep = True
        for f in features:
            v = row.get(f, 0)
            if abs(v - means[f]) > 3 * stds[f]:
                keep = False
        if keep:
            filtered.append(row)
    # Scale to [0, 1]
    mins = {f: min([row[f] for row in filtered]) for f in features}
    maxs = {f: max([row[f] for row in filtered]) for f in features}
    scaled = []
    for row in filtered:
        new_row = dict(row)
        for f in features:
            minv, maxv = mins[f], maxs[f]
            new_row[f] = (row[f] - minv) / (maxv - minv) if maxv > minv else 0
        scaled.append(new_row)
    return scaled

def train_test_split(dataset: List[Dict[str, Any]], test_ratio: float = 0.2) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    n = len(dataset)
    split = int(n * (1 - test_ratio))
    return dataset[:split], dataset[split:]

def perceptron_train(dataset: List[Dict[str, float]], features: List[str], label: str, epochs: int = 10) -> Tuple[Dict[str, float], float]:
    weights = {f: 0.0 for f in features}
    bias = 0.0
    for _ in range(epochs):
        for row in dataset:
            x = sum(row[f] * weights[f] for f in features) + bias
            y = 1 if x >= 0 else 0
            error = row[label] - y
            for f in features:
                weights[f] += error * row[f]
            bias += error
    return weights, bias

def perceptron_predict(row: Dict[str, float], weights: Dict[str, float], bias: float, features: List[str]) -> int:
    x = sum(row[f] * weights[f] for f in features) + bias
    return 1 if x >= 0 else 0

def extract_rules(weights: Dict[str, float], bias: float, features: List[str]) -> List[str]:
    rules = []
    for f in features:
        if weights[f] > 0:
            rules.append(f"Higher {f} increases chance of high-value customer.")
        elif weights[f] < 0:
            rules.append(f"Lower {f} increases chance of high-value customer.")
    return rules

def evaluate_accuracy(dataset: List[Dict[str, float]], weights: Dict[str, float], bias: float, features: List[str], label: str) -> float:
    correct = 0
    for row in dataset:
        pred = perceptron_predict(row, weights, bias, features)
        if pred == row[label]:
            correct += 1
    return correct / len(dataset) if dataset else 0 