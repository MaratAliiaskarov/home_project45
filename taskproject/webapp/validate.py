def article_validate(project, content, author):
    errors = {}
    if not project:
        errors["project"] = "Obyazatelnoe pole"
    elif len(project) > 50:
        errors["project"] = "Doljen byt menshe 200 simvolov"
    if not content:
        errors["content"] = "Obyazatelnoe pole"
    elif len(content) > 3000:
        errors["content"] = "Doljen byt menshe 3000 simvolov"
    if not author:
        errors["author"] = "Obyazatelnoe pole"
    elif len(author) > 50:
        errors["author"] = "Doljen byt menshe 50 simvolov"
    return errors