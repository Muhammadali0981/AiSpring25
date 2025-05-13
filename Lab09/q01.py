from typing import List, Dict, Any

def clean_dataset(dataset: List[Dict[str, Any]], categorical: List[str]) -> List[Dict[str, Any]]:
    cat_maps = {cat: {} for cat in categorical}
    for row in dataset:
        for cat in categorical:
            val = row.get(cat, 'Unknown')
            if val not in cat_maps[cat]:
                cat_maps[cat][val] = len(cat_maps[cat])
    cleaned = []
    for row in dataset:
        new_row = {}
        for key, value in row.items():
            if key in categorical:
                val = value if value is not None else 'Unknown'
                new_row[key] = cat_maps[key][val]
            else:
                new_row[key] = value if value is not None else 0
        cleaned.append(new_row)
    return cleaned

def feature_importance(dataset: List[Dict[str, Any]], target: str) -> List[str]:
    def mean(values):
        return sum(values) / len(values) if values else 0
    features = [k for k in dataset[0] if k != target]
    target_vals = [row[target] for row in dataset]
    target_mean = mean(target_vals)
    importances = []
    for feat in features:
        feat_vals = [row[feat] for row in dataset]
        feat_mean = mean(feat_vals)
        cov = sum((x - feat_mean) * (y - target_mean) for x, y in zip(feat_vals, target_vals))
        var_feat = sum((x - feat_mean) ** 2 for x in feat_vals)
        var_target = sum((y - target_mean) ** 2 for y in target_vals)
        corr = abs(cov / ((var_feat ** 0.5) * (var_target ** 0.5))) if var_feat and var_target else 0
        importances.append((feat, corr))
    importances.sort(key=lambda x: -x[1])
    return [feat for feat, _ in importances]

def rmse(y_true: List[float], y_pred: List[float]) -> float:
    n = len(y_true)
    return (sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / n) ** 0.5 if n else 0

def predict_price(features: Dict[str, float], weights: Dict[str, float], bias: float = 0.0) -> float:
    return sum(features.get(f, 0) * w for f, w in weights.items()) + bias 