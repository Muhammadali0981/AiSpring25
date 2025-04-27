from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def create_student_network():
    model = BayesianNetwork([
        ('I', 'G'),  # Intelligence -> Grade
        ('S', 'G'),  # StudyHours -> Grade
        ('D', 'G'),  # Difficulty -> Grade
        ('G', 'P')   # Grade -> Pass
    ])
    
    # Prior probabilities
    cpd_i = TabularCPD(
        variable='I',
        variable_card=2,
        values=[[0.7], [0.3]],
        state_names={'I': ['High', 'Low']}
    )
    
    cpd_s = TabularCPD(
        variable='S',
        variable_card=2,
        values=[[0.6], [0.4]],
        state_names={'S': ['Sufficient', 'Insufficient']}
    )
    
    cpd_d = TabularCPD(
        variable='D',
        variable_card=2,
        values=[[0.4], [0.6]],
        state_names={'D': ['Hard', 'Easy']}
    )
    
    # Conditional probabilities for Grade
    cpd_g = TabularCPD(
        variable='G',
        variable_card=3,
        values=[
            [0.8, 0.6, 0.4, 0.2, 0.6, 0.4, 0.2, 0.1],  # A
            [0.15, 0.3, 0.4, 0.5, 0.3, 0.4, 0.5, 0.4],  # B
            [0.05, 0.1, 0.2, 0.3, 0.1, 0.2, 0.3, 0.5]   # C
        ],
        evidence=['I', 'S', 'D'],
        evidence_card=[2, 2, 2],
        state_names={
            'G': ['A', 'B', 'C'],
            'I': ['High', 'Low'],
            'S': ['Sufficient', 'Insufficient'],
            'D': ['Hard', 'Easy']
        }
    )
    
    # Conditional probabilities for Pass
    cpd_p = TabularCPD(
        variable='P',
        variable_card=2,
        values=[
            [0.95, 0.80, 0.50],  # Yes
            [0.05, 0.20, 0.50]   # No
        ],
        evidence=['G'],
        evidence_card=[3],
        state_names={
            'P': ['Yes', 'No'],
            'G': ['A', 'B', 'C']
        }
    )
    
    model.add_cpds(cpd_i, cpd_s, cpd_d, cpd_g, cpd_p)
    return model

def perform_inference():
    model = create_student_network()
    inference = VariableElimination(model)
    
    # Task 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)
    query1 = inference.query(
        variables=['P'],
        evidence={'S': 'Sufficient', 'D': 'Hard'}
    )
    
    # Task 2: P(Intelligence=High | Pass=Yes)
    query2 = inference.query(
        variables=['I'],
        evidence={'P': 'Yes'}
    )
    
    return query1, query2

query1, query2 = perform_inference()
print("\nTask 1: P(Pass | StudyHours=Sufficient, Difficulty=Hard)")
print(query1)
print("\nTask 2: P(Intelligence=High | Pass=Yes)")
print(query2) 