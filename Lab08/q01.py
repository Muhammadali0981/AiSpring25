def calculate_probabilities():
    # Total cards
    total_cards = 52
    red_cards = 26  # Hearts (13) + Diamonds (13)
    hearts = 13
    face_cards = 12  # 3 face cards (J, Q, K) * 4 suits
    diamond_face_cards = 3  # J, Q, K of diamonds
    spade_face_cards = 3  # J, Q, K of spades
    queens = 4  # One queen from each suit
    
    # P(Red card)
    p_red = red_cards / total_cards
    
    # P(Heart | Red card)
    p_heart_given_red = hearts / red_cards
    
    # P(Diamond | Face card)
    p_diamond_given_face = diamond_face_cards / face_cards
    
    # P(Spade or Queen | Face card)
    spade_or_queen_face = spade_face_cards + queens - 1  # Subtract 1 to avoid counting Queen of Spades twice
    p_spade_or_queen_given_face = spade_or_queen_face / face_cards
    
    return {
        "P(Red card)": p_red,
        "P(Heart | Red card)": p_heart_given_red,
        "P(Diamond | Face card)": p_diamond_given_face,
        "P(Spade or Queen | Face card)": p_spade_or_queen_given_face
    }

probabilities = calculate_probabilities()
for event, prob in probabilities.items():
    print(f"{event}: {prob:.3f}") 