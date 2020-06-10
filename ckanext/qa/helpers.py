import copy
from ckan.plugins import toolkit as tk
import lib


def qa_openness_stars_resource_html(resource):
    qa = resource.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    if not qa:
        return tk.literal('<!-- No qa info for this resource -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')

    # Take a copy of the qa dict, because weirdly the renderer appears to add
    # keys to it like _ and app_globals. This is bad because when it comes to
    # render the debug in the footer those extra keys take about 30s to render,
    # for some reason.
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars.html',
                  extra_vars=extra_vars))


def qa_openness_stars_dataset_html(dataset):
    qa = dataset.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    print(dataset)
    print(qa)
    if not qa:
        return tk.literal('<!-- No qa info for this dataset -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars_brief.html',
                  extra_vars=extra_vars))


def qa_openness_stars_dataset2_html(dataset):
    qa = dataset.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    #Pregunta si es de tipo dataset
    field_name = getattr(dataset, 'type')
    files_ = lib.resource_format_scores()
    for item in files_:
       print item
    if not qa:
        return tk.literal('<!-- No qa info for this dataset -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')

    # Take a copy of the qa dict, because weirdly the renderer appears to add
    # keys to it like _ and app_globals. This is bad because when it comes to
    # render the debug in the footer those extra keys take about 30s to render,
    # for some reason.
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars.html',
                  extra_vars=extra_vars))
