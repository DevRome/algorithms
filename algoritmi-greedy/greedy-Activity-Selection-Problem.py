# .:: Activity Selection Problem ::.
# algoritmo Greedy

def activity_selection(start_times, end_times):
    # Accoppia ciascuna attività con il suo tempo di fine
    activities = sorted(zip(end_times, start_times))
    
    # Lista per memorizzare le attività selezionate
    selected_activities = []
    
    # L'attività iniziale
    last_end_time = 0
    
    for end, start in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end
    
    return selected_activities

# Esempio di utilizzo
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start_times, end_times)
print("Attività selezionate:", selected)
# Output: Attività selezionate: [(1, 2), (3, 4), (5, 7), (8, 9)]
