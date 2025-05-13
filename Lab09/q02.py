from typing import List, Dict, Any

def preprocess_emails(dataset: List[Dict[str, Any]], text_fields: List[str]) -> List[Dict[str, Any]]:
    
    processed = []
    for row in dataset:
        new_row = dict(row)
        for field in text_fields:
            text = str(row.get(field, ''))
            new_row[field + '_len'] = len(text)
            new_row[field + '_num_words'] = len(text.split())
            new_row[field + '_num_links'] = text.count('http')
        processed.append(new_row)
    return processed

def train_spam_classifier(dataset: List[Dict[str, Any]], features: List[str], label: str) -> Dict[str, Any]:
    
    classes = {0: [], 1: []}
    for row in dataset:
        classes[row[label]].append(row)
    model = {'means': {}, 'priors': {}}
    for c in [0, 1]:
        model['priors'][c] = len(classes[c]) / len(dataset) if dataset else 0.5
        model['means'][c] = {f: sum(r[f] for r in classes[c]) / len(classes[c]) if classes[c] else 0 for f in features}
    return model

def predict_spam(email: Dict[str, Any], model: Dict[str, Any], features: List[str]) -> int:
    
    dists = {}
    for c in [0, 1]:
        dists[c] = sum(abs(email.get(f, 0) - model['means'][c][f]) for f in features)
    return 1 if dists[1] < dists[0] else 0

def evaluate_classifier(dataset: List[Dict[str, Any]], model: Dict[str, Any], features: List[str], label: str) -> float:
    correct = 0
    for row in dataset:
        pred = predict_spam(row, model, features)
        if pred == row[label]:
            correct += 1
    return correct / len(dataset) if dataset else 0 