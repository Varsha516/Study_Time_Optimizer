def optimize_study_time(subjects, difficulties, hours):

    weight_map = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    weights = []

    for diff in difficulties:
        weights.append(weight_map[diff])

    total_weight = sum(weights)

    study_plan = []

    for i in range(len(subjects)):
        allocated_time = (weights[i] / total_weight) * hours
        study_plan.append((subjects[i], round(allocated_time, 2)))

    return study_plan