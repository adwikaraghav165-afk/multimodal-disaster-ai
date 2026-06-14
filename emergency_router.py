# emergency_router.py

def emergency_routing(risk_score):

    if risk_score > 80:
        return [
            "🚨 NDMA Activated",
            "🪖 Army Response Team",
            "🚒 Fire & Rescue Department"
        ]

    elif risk_score > 50:
        return [
            "⚠ Local Emergency Team",
            "🚑 Ambulance Services",
            "👮 Police Department"
        ]

    else:
        return [
            "🟢 Monitoring Mode",
            "📡 Situation Under Observation"
        ]