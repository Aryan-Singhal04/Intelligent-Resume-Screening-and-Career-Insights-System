from utilitis.career_data import career_data


def get_career_details(selected, compare_selected=None):

    data = career_data.get(selected) if selected else None

    compare_data = None

    if compare_selected and compare_selected != selected:
        compare_data = career_data.get(compare_selected)

    return {
        "data": data,
        "selected": selected,
        "compare_data": compare_data,
        "compare_selected": compare_selected,
        "categories": career_data
    }


def answer_question(career, question):

    career_info = career_data.get(career)

    if not career_info:
        return {"error": "Career not found."}

    answer = career_info["questions"].get(question)

    if not answer:
        return {"error": "Answer not available for this question."}

    return {"answer": answer}