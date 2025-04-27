from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def create_disease_network():
    model = BayesianNetwork([
        ('D', 'F'),  # Disease -> Fever
        ('D', 'C'),  # Disease -> Cough
        ('D', 'Fa'), # Disease -> Fatigue
        ('D', 'Ch')  # Disease -> Chills
    ])
    
    # Prior probabilities for Disease
    cpd_d = TabularCPD(
        variable='D',
        variable_card=2,
        values=[[0.3], [0.7]],  # [Flu, Cold]
        state_names={'D': ['Flu', 'Cold']}
    )
    
    # Conditional probabilities for Fever
    cpd_f = TabularCPD(
        variable='F',
        variable_card=2,
        values=[
            [0.9, 0.5],  # Yes
            [0.1, 0.5]   # No
        ],
        evidence=['D'],
        evidence_card=[2],
        state_names={
            'F': ['Yes', 'No'],
            'D': ['Flu', 'Cold']
        }
    )
    
    # Conditional probabilities for Cough
    cpd_c = TabularCPD(
        variable='C',
        variable_card=2,
        values=[
            [0.8, 0.6],  # Yes
            [0.2, 0.4]   # No
        ],
        evidence=['D'],
        evidence_card=[2],
        state_names={
            'C': ['Yes', 'No'],
            'D': ['Flu', 'Cold']
        }
    )
    
    # Conditional probabilities for Fatigue
    cpd_fa = TabularCPD(
        variable='Fa',
        variable_card=2,
        values=[
            [0.7, 0.3],  # Yes
            [0.3, 0.7]   # No
        ],
        evidence=['D'],
        evidence_card=[2],
        state_names={
            'Fa': ['Yes', 'No'],
            'D': ['Flu', 'Cold']
        }
    )
    
    # Conditional probabilities for Chills
    cpd_ch = TabularCPD(
        variable='Ch',
        variable_card=2,
        values=[
            [0.6, 0.4],  # Yes
            [0.4, 0.6]   # No
        ],
        evidence=['D'],
        evidence_card=[2],
        state_names={
            'Ch': ['Yes', 'No'],
            'D': ['Flu', 'Cold']
        }
    )
    
    model.add_cpds(cpd_d, cpd_f, cpd_c, cpd_fa, cpd_ch)
    return model

def perform_inference():
    model = create_disease_network()
    inference = VariableElimination(model)
    
    # Task 1: P(Disease | Fever=Yes, Cough=Yes)
    query1 = inference.query(
        variables=['D'],
        evidence={'F': 'Yes', 'C': 'Yes'}
    )
    
    # Task 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)
    query2 = inference.query(
        variables=['D'],
        evidence={'F': 'Yes', 'C': 'Yes', 'Ch': 'Yes'}
    )
    
    # Task 3: P(Fatigue=Yes | Disease=Flu)
    query3 = inference.query(
        variables=['Fa'],
        evidence={'D': 'Flu'}
    )
    
    return query1, query2, query3

query1, query2, query3 = perform_inference()
print("\nTask 1: P(Disease | Fever=Yes, Cough=Yes)")
print(query1)
print("\nTask 2: P(Disease | Fever=Yes, Cough=Yes, Chills=Yes)")
print(query2)
print("\nTask 3: P(Fatigue=Yes | Disease=Flu)")
print(query3) 