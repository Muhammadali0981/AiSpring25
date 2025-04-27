import numpy as np
import random

def create_weather_model():
    # Transition matrix
    # [Sunny, Cloudy, Rainy]
    transition_matrix = np.array([
        [0.6, 0.3, 0.1],  # Sunny -> [Sunny, Cloudy, Rainy]
        [0.3, 0.4, 0.3],  # Cloudy -> [Sunny, Cloudy, Rainy]
        [0.2, 0.3, 0.5]   # Rainy -> [Sunny, Cloudy, Rainy]
    ])
    return transition_matrix

def simulate_weather(days, start_state=0):
    states = ['Sunny', 'Cloudy', 'Rainy']
    transition_matrix = create_weather_model()
    
    current_state = start_state
    weather_sequence = [states[current_state]]
    rainy_days = 1 if current_state == 2 else 0
    
    for _ in range(days - 1):
        # Get next state probabilities
        next_state_probs = transition_matrix[current_state]
        # Choose next state based on probabilities
        current_state = random.choices(range(3), weights=next_state_probs)[0]
        weather_sequence.append(states[current_state])
        if current_state == 2:  # Rainy
            rainy_days += 1
    
    return weather_sequence, rainy_days

def calculate_probability_at_least_3_rainy_days(n_simulations=10000):
    rainy_days_count = 0
    for _ in range(n_simulations):
        _, rainy_days = simulate_weather(10)
        if rainy_days >= 3:
            rainy_days_count += 1
    
    return rainy_days_count / n_simulations

# Simulate weather for 10 days
weather_sequence, rainy_days = simulate_weather(10)
print("Weather sequence for 10 days:")
print(weather_sequence)
print(f"Number of rainy days: {rainy_days}")

# Calculate probability of at least 3 rainy days
prob = calculate_probability_at_least_3_rainy_days()
print(f"\nProbability of at least 3 rainy days in 10 days: {prob:.3f}") 