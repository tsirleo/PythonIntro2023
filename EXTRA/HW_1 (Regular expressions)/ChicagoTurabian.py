import re


def match_bibliographic_reference(bib_ref):
    pattern_b = re.compile(r"^(?P<author>[A-Z][a-z]*(-[A-Z][a-z]*)?),(?P<name>( (([A-Z]\.)+|[A-Z][a-z]*))+)("
                           r"?P<additional>(,( (([A-Z]\.)+|[A-Z][a-z]*))+)*, and( (([A-Z]\.)+|[A-Z][a-z]*))+)?\. ("
                           r"?P<title>.*)\. (?P<city>.*?): (?P<publisher>[a-zA-Z ]*?), (?P<date>\d+)\.$")
    return pattern_b.match(bib_ref)


def match_in_text_reference(text_ref):
    pattern_b = re.compile(r"^\d+\. ((?P<name>( ?[A-Z].|[A-Za-z])+(-[A-Z][a-z]*)?){1,2} (?P<author>([A-Z].|["
                           r"A-Za-z])+(-[A-Z][a-z]*)?))(?P<additional> et al.|(,(( ?[A-Z].|[A-Za-z])+(-[A-Z]["
                           r"a-z]*)?),)+ and (( ?[A-Z].|[A-Za-z])+(-[A-Z][a-z]*)?)| and (( ?[A-Z].|[A-Za-z])+(-[A-Z]["
                           r"a-z]*)?))?, (?P<title>.*) \((?P<city>.*?): (?P<publisher>[a-zA-Z ]*?), (?P<date>\d+)\), "
                           r"(\d+(–[0-9]*)?)\.$")
    return pattern_b.match(text_ref)


def are_references_matching(text_ref, bib_ref):
    match_n = match_in_text_reference(text_ref)
    match_b = match_bibliographic_reference(bib_ref)
    if not bool(match_n) or not bool(match_b):
        return False
    else:
        for key in match_n.groupdict():
            match key:
                case "additional":
                    if match_n[key] and match_b[key]:
                        match len(match_b[key][1:].split(',')):
                            case 1:
                                if match_n[key] != match_b[key][1:]:
                                    return False
                            case 2:
                                if match_n[key] != match_b[key]:
                                    return False
                            case 3:
                                if match_n[key] != match_b[key] and match_n[key] != " et al.":
                                    return False
                    elif (match_n[key] and not match_b[key]) or (not match_n[key] and match_b[key]):
                        return False
                case "name":
                    value = match_b[key][1:] if len(match_b[key][1:].split()[-1]) > 1 else match_b[key][1:] + '.'
                    if match_n[key] != value:
                        return False
                case _:
                    if match_n[key] != match_b[key]:
                        return False

    return True


text_reference = input()
bibliographic_reference = input()
print(are_references_matching(text_reference, bibliographic_reference))
