def fusion(cnn, lstm, nlp):
    return (cnn * 0.4) + (lstm * 0.3) + (nlp * 0.3)